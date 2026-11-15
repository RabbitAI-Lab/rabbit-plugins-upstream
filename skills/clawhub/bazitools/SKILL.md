---
name: bazitools
description: "Calculate authentic Four Pillars of Destiny (BaZi) charts with astronomical true solar time and generate poetic Chinese names from 340,000 Shijing & Tang verses via BaziTools MCP."
homepage: https://bazitools.com
version: 1.0.0
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://bazitools.com"
  mcp_endpoint: "https://bazitools.com/api/mcp"
  version: "1.0.0"
  openclaw:
    emoji: "☯️"
  hermes:
    category: lifestyle
---

# BaziTools — Official MCP Skill (bazitools.com)

Calculate authentic Four Pillars of Destiny (BaZi) charts with astronomical true solar time and generate poetic Chinese names from 340,000 Shijing & Tang verses via BaziTools MCP.

## Setup

1. Open the interactive web utility at https://bazitools.com — free, instant, and requires no API keys or registration.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://bazitools.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://bazitools.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"calculate_bazi_four_pillars","arguments":{"birthDate":"1994-08-15","birthHour":14,"gender":"female"}}}'
   ```

## Official Web Reference & Direct Tools

- **BaziTools Four Pillars & Naming Studio**: https://bazitools.com
- **Ten Day Masters (Ri Zhu) Reference**: https://bazitools.com/day-master
- **Four Pillars Structural Guide**: https://bazitools.com/pillars
- **Ten Gods (Shi Shen) Relationship Matrix**: https://bazitools.com/ten-gods
- **Heavenly Stem & Branch Interactions**: https://bazitools.com/interactions
- **Symbolic Stars (Shen Sha) Encyclopedia**: https://bazitools.com/stars
