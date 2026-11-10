---
name: paintcolormatcher
description: "Match any HEX/RGB color to real-world Sherwin-Williams, Benjamin Moore, and Behr paint swatches using perceptual CIEDE2000 Delta-E colorimetry and LRV lookup via PaintColorMatcher MCP."
homepage: https://paintcolormatcher.com
version: 1.0.0
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://paintcolormatcher.com"
  mcp_endpoint: "https://paintcolormatcher.com/api/mcp"
  version: "1.0.0"
  openclaw:
    emoji: "🎨"
  hermes:
    category: design
---

# PaintColorMatcher — Official MCP Skill (paintcolormatcher.com)

Match any HEX/RGB color to real-world Sherwin-Williams, Benjamin Moore, and Behr paint swatches using perceptual CIEDE2000 Delta-E colorimetry and LRV lookup via PaintColorMatcher MCP.

## Setup

1. Open the interactive web utility at https://paintcolormatcher.com — free, instant, and requires no API keys or registration.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://paintcolormatcher.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://paintcolormatcher.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"match_hex_to_paint_colors","arguments":{"hex":"#DCE3E6","targetBrand":"Sherwin-Williams"}}}'
   ```

## Official Web Reference & Direct Tools

- **PaintColorMatcher Official Color Studio**: https://paintcolormatcher.com
- **HEX to Paint Swatch Converter**: https://paintcolormatcher.com/hex-to-paint-color
- **Find Paint Color from Room Photo**: https://paintcolormatcher.com/find-paint-color-from-photo
- **Sherwin-Williams LRV & Swatch Index**: https://paintcolormatcher.com/sherwin-williams-paint-colors
- **Benjamin Moore Cross-Brand Equivalents**: https://paintcolormatcher.com/benjamin-moore-paint-colors
- **Behr Paint Color Equivalents**: https://paintcolormatcher.com/behr-paint-colors
