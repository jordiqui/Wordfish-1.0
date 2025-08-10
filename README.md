# Wordfish Chess Engine

<div align="center">
  <img src="[https://ijccrl.com/wp-content/uploads/2025/08/wordfish.png]" 
  <h3>Wordfish</h3>
  
  A free and open-source UCI chess engine combining classical algorithms with neural network innovations.
  <br>
  <strong><a href="#">Explore Wordfish Documentation »</a>
  
</div>

## Overview

**Wordfish** is a free, open-source UCI chess engine implementing cutting-edge search algorithms combined with neural network evaluation. Derived from fundamental chess programming principles, Wordfish analyzes positions through parallelized alpha-beta search enhanced with null-move pruning and late move reductions.

As a UCI-compliant engine, Wordfish operates through **standard chess interfaces** without an integrated graphical interface. Users must employ compatible chess GUIs (Arena, Scid vs PC, etc.) for board visualization and move input. Consult your GUI documentation for implementation details.

## Technical Architecture

Wordfish's architecture features:

- Hybrid evaluation system combining classical heuristics with NNUE networks
- SMP parallelization with YBWC (Young Brothers Wait Concept)
- Advanced pruning techniques (Reverse Futility Pruning, Late Move Pruning)
- Efficient move ordering with history heuristics and killer moves
- Tuned search parameters through reinforcement learning

## Files

The distribution includes:

- `README.md` (this documentation)
- `COPYING.txt` ([GNU GPL v3 license][gpl-link])
- `AUTHORS` (contributor acknowledgments)
- `src/` (source code with platform-specific Makefiles)
- Neural network weights (`wordfish.nnue`)

## Contributing

### Development Guidelines
Contributions must adhere to:
- Clean, documented C++17 implementations
- Benchmark validation through perft testing
- Elo measurement via [OpenBench][openbench-link]
- Compatibility with UCI protocol standard

### Testing Infrastructure
Improvements require extensive testing:
- Install the [Wordfish Test Worker][worker-link]
- Participate in active tests on [Wordfish Test Suite][testsuite-link]
- Verify ELO gains through SPRT validation

### Community
Technical discussions occur primarily through:
- [Wordfish Discord Server][discord-link]
- [GitHub Discussions][discussions-link]
- [Chess Programming Wiki][chesswiki-link]

## Compilation

Compile from source using included Makefiles:
```bash
cd src
make -j ARCH=x86-64-modern
```

Supported architectures:
- `x86-64`: Modern x86 processors
- `armv8`: ARMv8+ architectures
- `ppc64`: PowerPC systems

Full compilation guides available in [documentation][doc-link].

## License

Wordfish is licensed under the **[GNU General Public License v3][gpl-link]** (GPL v3). This grants permission to:
- Use, modify, and distribute the software
- Incorporate into larger projects
- Conduct commercial utilization

**Distribution Requirements**:
1. Include original license text (`COPYING.txt`)
2. Provide complete corresponding source code
3. Disclose all modifications under GPL v3

## Acknowledgements

Wordfish incorporates:
- Neural networks trained on [Lichess open database][lichess-db]
- Search techniques from [CCC testing community][ccc-link]
- Positional analysis concepts from [CPW research][cpw-link]

[gpl-link]: https://www.gnu.org/licenses/gpl-3.0.html
[doc-link]: #
[discord-link]: #
[openbench-link]: #
[worker-link]: #
[testsuite-link]: #
[discussions-link]: #
[chesswiki-link]: https://www.chessprogramming.org
[lichess-db]: https://database.lichess.org
[ccc-link]: https://www.chess.com/computer-chess-championship
[cpw-link]: https://www.chessprogramming.org
