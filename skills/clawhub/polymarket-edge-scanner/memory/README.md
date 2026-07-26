# Memory System

## Files

- `MEMORY.md` — curated long-term memory. Distilled facts, preferences, lessons, projects.
- `memory/YYYY-MM-DD.md` — raw daily logs.
- `memory_graph.dot` — editable Graphviz source for the memory map.
- `memory_graph.svg` / `memory_graph.png` — rendered memory map.
- `memory_update.py` — helper to add entries and rebuild the graph.

## How to update

### Add a daily note
Create `memory/YYYY-MM-DD.md` with what happened. Keep it raw.

### Update long-term memory
Edit `MEMORY.md` directly, or run:
```bash
python3 memory_update.py --section "Projects" --entry "- New project..."
```

### Rebuild the memory graph
```bash
python3 memory_update.py --rebuild
```

## Review cadence
Every few days, review recent daily notes and distill anything worth keeping into `MEMORY.md`.
