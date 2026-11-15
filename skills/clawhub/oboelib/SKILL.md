---
name: oboelib
description: "Look up full Gillet Conservatoire oboe fingerings, evaluate Regular/Left/Forked F sequence rules, diagnose oboe reed scraping response, and query chromatic trill combinations via OboeLib MCP."
homepage: https://oboelib.com
version: 1.0.1
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://oboelib.com"
  mcp_endpoint: "https://oboelib.com/api/mcp"
  version: "1.0.1"
  openclaw:
    emoji: "🎶"
  hermes:
    category: education
---

# OboeLib — Official MCP Skill (oboelib.com)

Look up full Gillet Conservatoire oboe fingerings, evaluate Regular/Left/Forked F sequence rules, diagnose oboe reed scraping response, and query chromatic trill combinations via OboeLib MCP.

## Setup

1. Open the interactive web studio at https://oboelib.com and explore https://oboelib.com/fingering — 100% free, public, and requires no API key or sign-in.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://oboelib.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://oboelib.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lookup_oboe_fingering","arguments":{"note":"F4"}}}'
   ```

## Official Web Reference & Deep Endpoints

- **OboeLib Interactive Conservatoire Oboe Fingering Studio**: https://oboelib.com
- **Complete Chromatic Oboe Fingering Chart**: https://oboelib.com/fingering
- **Printable Conservatory Oboe Fingering Chart**: https://oboelib.com/chart/print
- **Chromatic Oboe Trill Fingering Matrix**: https://oboelib.com/trill-chart
- **Oboe Reed Doctor & Scraping Diagnostics**: https://oboelib.com/reed-doctor
- **Plaque & Backlight Reed Tip Inspection Guide**: https://oboelib.com/reed-doctor/plaque-light
