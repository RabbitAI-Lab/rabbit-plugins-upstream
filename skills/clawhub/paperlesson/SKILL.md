---
name: paperlesson
description: "Generate deterministic seeded K-12 arithmetic drill sets, query Zaner-Bloser and DNealian primary handwriting ruling specifications, configure custom name-tracing sheets, and look up cursive stroke-group progressions via PaperLesson MCP."
homepage: https://paperlesson.com/
version: 1.0.1
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://paperlesson.com/"
  mcp_endpoint: "https://paperlesson.com/api/mcp"
  version: "1.0.1"
  openclaw:
    emoji: "📐"
  hermes:
    category: education
---

# PaperLesson — Official MCP Skill (paperlesson.com)

Generate deterministic seeded K-12 arithmetic drill sets, query Zaner-Bloser and DNealian primary handwriting ruling specifications, configure custom name-tracing sheets, and look up cursive stroke-group progressions via PaperLesson MCP.

## Setup

1. Open the interactive web studio at https://paperlesson.com/ and explore https://paperlesson.com/name-tracing-generator — 100% free, public, and requires no API key or sign-in.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://paperlesson.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://paperlesson.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"generate_seeded_math_drill_set","arguments":{"operation":"multiplication","grade":3,"count":10,"seed":42}}}'
   ```

## Official Web Reference & Deep Endpoints

- **PaperLesson True-Vector Worksheet Studio**: https://paperlesson.com/
- **Custom Name Tracing Worksheet Generator**: https://paperlesson.com/name-tracing-generator
- **Primary Handwriting Ruled Worksheets**: https://paperlesson.com/handwriting-worksheets
- **Cursive Handwriting Stroke Worksheets**: https://paperlesson.com/cursive-handwriting-worksheets
- **Alphabet Letter Tracing Worksheets**: https://paperlesson.com/letter-tracing-worksheets
- **Early Math Number Tracing Worksheets**: https://paperlesson.com/number-tracing-worksheets
