#include "experience.h"

#include <fstream>
#include <mutex>
#include <unordered_map>

namespace Stockfish {

namespace Experience {

namespace {
std::unordered_map<Key, Entry> table;
std::string                   filePath;
std::mutex                    mtx;
} // namespace

void init(const std::string& path) {
    std::lock_guard<std::mutex> lk(mtx);
    filePath = path;
    table.clear();
    std::ifstream in(path);
    if (!in)
        return;
    uint64_t key;
    unsigned move;
    int value;
    uint64_t visits;
    while (in >> key >> move >> value >> visits) {
        table[key] = Entry{key, Move(static_cast<uint16_t>(move)), Value(value), visits};
    }
}

std::optional<Entry> probe(const Position& pos) {
    std::lock_guard<std::mutex> lk(mtx);
    Key k = pos.key();
    auto it = table.find(k);
    if (it != table.end())
        return it->second;
    return std::nullopt;
}

void update(const Position& pos, Move move, Value value) {
    std::lock_guard<std::mutex> lk(mtx);
    if (filePath.empty())
        return;
    Key k      = pos.key();
    Entry& ent = table[k];
    ent.key    = k;
    ent.move   = move;
    ent.value  = value;
    ent.visits++;
}

void save() {
    std::lock_guard<std::mutex> lk(mtx);
    if (filePath.empty())
        return;
    std::ofstream out(filePath, std::ios::trunc);
    for (const auto& [k, e] : table)
        out << e.key << ' ' << e.move.raw() << ' ' << e.value << ' ' << e.visits << '\n';
}

} // namespace Experience

} // namespace Stockfish
