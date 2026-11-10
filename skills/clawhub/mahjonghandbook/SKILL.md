---
name: mahjonghandbook
description: "Query American Mahjong (NMJL card sections, Charleston passing strategy, Joker rules), Chinese Official MCR (81 Fan), and Japanese Riichi Yaku scoring rules via MahjongHandbook MCP."
homepage: https://mahjonghandbook.com
version: 1.0.0
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://mahjonghandbook.com"
  mcp_endpoint: "https://mahjonghandbook.com/api/mcp"
  version: "1.0.0"
  openclaw:
    emoji: "🀄"
  hermes:
    category: gaming
---

# MahjongHandbook — Official MCP Skill (mahjonghandbook.com)

Query American Mahjong (NMJL card sections, Charleston passing strategy, Joker rules), Chinese Official MCR (81 Fan), and Japanese Riichi Yaku scoring rules via MahjongHandbook MCP.

## Setup

1. Open the interactive web utility at https://mahjonghandbook.com — free, instant, and requires no API keys or registration.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://mahjonghandbook.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://mahjonghandbook.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lookup_mahjong_scoring_rules","arguments":{"variant":"american_nmjl","query":"2468"}}}'
   ```

## Official Web Reference & Direct Tools

- **MahjongHandbook Official Strategy Guide**: https://mahjonghandbook.com/
- **NMJL Card Section Breakdown**: https://mahjonghandbook.com/nmjl-card/
- **Consecutive Run Hand Patterns**: https://mahjonghandbook.com/nmjl-card/consecutive-run/
- **2468 Evens Strategy & Pivots**: https://mahjonghandbook.com/nmjl-card/2468-evens/
- **13579 Odds Hand Guide**: https://mahjonghandbook.com/nmjl-card/13579-odds/
- **369 Multiples Pattern Reference**: https://mahjonghandbook.com/nmjl-card/369-multiples/
