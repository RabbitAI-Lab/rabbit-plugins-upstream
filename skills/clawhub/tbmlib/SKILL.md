---
name: tbmlib
description: "Look up tenor and F-attachment trombone 7 slide positions, analyze natural overtone series cent deviations, compare bore/mouthpiece pairings, and generate legato brass warmup routines via TbmLib MCP."
homepage: https://tbmlib.com
version: 1.0.1
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://tbmlib.com"
  mcp_endpoint: "https://tbmlib.com/api/mcp"
  version: "1.0.1"
  openclaw:
    emoji: "🎺"
  hermes:
    category: education
---

# TbmLib — Official MCP Skill (tbmlib.com)

Look up tenor and F-attachment trombone 7 slide positions, analyze natural overtone series cent deviations, compare bore/mouthpiece pairings, and generate legato brass warmup routines via TbmLib MCP.

## Setup

1. Open the interactive web studio at https://tbmlib.com and explore https://tbmlib.com/chart/print — 100% free, public, and requires no API key or sign-in.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://tbmlib.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://tbmlib.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lookup_trombone_slide_position","arguments":{"note":"Bb3","tromboneType":"f_attachment"}}}'
   ```

## Official Web Reference & Deep Endpoints

- **TbmLib Interactive Trombone Slide Position Chart**: https://tbmlib.com
- **Printable Trombone Slide Position Reference Sheet**: https://tbmlib.com/chart/print
- **Cello-Timbre Brass Intonation Drone Tuner**: https://tbmlib.com/tools/drone
- **Orchestral Trombone Audition Excerpts Library**: https://tbmlib.com/excerpts
- **Mozart Requiem Tuba Mirum Tenor Solo Guide**: https://tbmlib.com/excerpts/mozart-requiem-tuba-mirum
- **Ravel Bolero High-Register Trombone Solo Guide**: https://tbmlib.com/excerpts/ravel-bolero
