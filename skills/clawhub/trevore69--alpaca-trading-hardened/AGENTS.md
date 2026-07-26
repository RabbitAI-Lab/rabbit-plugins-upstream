## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## memory

Durable user facts live in /root/memory/ (knowledge/, decisions/, people/, projects/) with an INDEX.md.

Rules:
- Before saying you do not know something, or that a fact was never mentioned, first read /root/memory/knowledge/remembered-facts.md and check INDEX.md. The answer may be stored from an earlier session even if it is not in the current transcript.
- When the user asks you to remember a durable fact, append it to /root/memory/knowledge/remembered-facts.md with the date.
- OpenClaw session notes also live at /root/.openclaw/workspace/memory/ if you need recent conversation context.
