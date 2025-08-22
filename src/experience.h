#ifndef EXPERIENCE_H_INCLUDED
#define EXPERIENCE_H_INCLUDED

#include <optional>
#include <string>

#include "position.h"
#include "types.h"

namespace Stockfish {

namespace Experience {

struct Entry {
    Key       key;
    Move      move;
    Value     value;
    uint64_t  visits;
};

void init(const std::string& path);
std::optional<Entry> probe(const Position& pos);
void update(const Position& pos, Move move, Value value);
void save();

} // namespace Experience

} // namespace Stockfish

#endif // EXPERIENCE_H_INCLUDED
