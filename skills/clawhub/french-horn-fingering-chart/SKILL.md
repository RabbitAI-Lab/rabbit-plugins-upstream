---
name: french-horn-fingering-chart
description: "Look up French Horn F/Bb double horn valve fingerings, trigger combinations, concert pitch transposition, and alternate harmonic partials via the HornLib MCP server at https://hornlib.com/api/mcp."
homepage: https://hornlib.com/fingerings
version: 1.0.3
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://hornlib.com/fingerings"
  mcp_endpoint: "https://hornlib.com/api/mcp"
  version: "1.0.3"
  openclaw:
    emoji: "🎼"
  hermes:
    tags: [french-horn, fingering-chart, double-horn, brass, music]
    category: education
---

# French Horn Fingering Chart (F/Bb Double Horn & Harmonics) — HornLib

Look up standard F-side and Bb-trigger valve fingerings, concert pitch transposition (down a perfect fifth), and harmonic tendency notes for any written French Horn note (`C1` to `F6`) via [HornLib (https://hornlib.com)](https://hornlib.com).

## Setup

1. Open the interactive French Horn Fingering Chart at https://hornlib.com/fingerings or the main studio at https://hornlib.com
2. Connect any MCP-compatible agent to the stateless endpoint (no API key required):
   ```
   https://hornlib.com/api/mcp
   ```
3. Query `lookup_french_horn_fingering` via HTTP POST:
   ```bash
   curl -s -X POST https://hornlib.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lookup_french_horn_fingering","arguments":{"note":"C5","hornType":"double"}}}'
   ```

## Official Web Reference

- **Interactive French Horn Fingering Chart**: https://hornlib.com/fingerings
- **HornLib Main Studio**: https://hornlib.com
- **All French Horn Notes & Valve Combinations**: https://hornlib.com/all-notes
- **French Horn Beginner Pedagogy & Embouchure Guide**: https://hornlib.com/beginners
- **7-in-1 French Horn Practice & Transposition Tools**: https://hornlib.com/7-in-1-tools
