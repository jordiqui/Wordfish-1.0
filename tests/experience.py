import os
import pathlib
import sys

from testing import Stockfish, MiniTestFramework, OrderedClassMembers

PATH = pathlib.Path(__file__).parent.resolve()
CWD = os.getcwd()

def get_path():
    return os.path.abspath(os.path.join(CWD, "src", "Wordfish"))

class TestExperience(metaclass=OrderedClassMembers):
    def test_experience_file(self):
        exp_path = os.path.join(PATH, "test.exp")

        # Obtain position key for start position
        sf = Stockfish([], get_path())
        sf.send_command("uci")
        sf.equals("uciok")
        sf.send_command("setoption name EvalFile value None")
        sf.send_command("setoption name EvalFileSmall value None")
        sf.send_command("isready")
        sf.equals("readyok")
        sf.send_command("position startpos")
        sf.send_command("d")
        holder = {}
        def grab(line):
            if line.startswith("Key:"):
                holder['k'] = line.split()[1]
                return True
        sf.check_output(grab)
        sf.send_command("quit")
        sf.close()
        key = int(holder['k'], 16)

        # Write experience entry suggesting move a2a3
        with open(exp_path, "w") as f:
            f.write(f"{key} 82 0 1\n")

        # Engine without experience
        sf = Stockfish([], get_path())
        sf.send_command("uci")
        sf.equals("uciok")
        sf.send_command("setoption name EvalFile value None")
        sf.send_command("setoption name EvalFileSmall value None")
        sf.send_command("isready")
        sf.equals("readyok")
        sf.send_command("ucinewgame")
        sf.send_command("position startpos")
        sf.send_command("go depth 1")
        best_without = []
        def cb1(line):
            if line.startswith("bestmove"):
                best_without.append(line.split()[1])
                return True
        sf.check_output(cb1)
        sf.send_command("quit")
        sf.close()

        # Engine with experience enabled
        sf = Stockfish([], get_path())
        sf.send_command("uci")
        sf.equals("uciok")
        sf.send_command("setoption name EvalFile value None")
        sf.send_command("setoption name EvalFileSmall value None")
        sf.send_command("setoption name Experience value true")
        sf.send_command(f"setoption name Experience File value {exp_path}")
        sf.send_command("isready")
        sf.equals("readyok")
        sf.send_command("ucinewgame")
        sf.send_command("position startpos")
        sf.send_command("go depth 1")
        best_with = []
        def cb2(line):
            if line.startswith("bestmove"):
                best_with.append(line.split()[1])
                return True
        sf.check_output(cb2)
        sf.send_command("quit")
        sf.close()

        assert best_with[0] == "b1c3"
        assert best_without[0] != "b1c3"

if __name__ == "__main__":
    framework = MiniTestFramework()
    framework.run([TestExperience])
    if framework.has_failed():
        sys.exit(1)
    sys.exit(0)
