---
name: labelqueue
description: "Look up exact Avery & thermal sheet label dimensions, pitch, margins, and batch CSV-to-PDF barcode print layouts via the stateless LabelQueue MCP server."
homepage: https://labelqueue.com
version: 1.0.0
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://labelqueue.com"
  mcp_endpoint: "https://labelqueue.com/api/mcp"
  version: "1.0.0"
  openclaw:
    emoji: "🏷️"
  hermes:
    category: productivity
---

# LabelQueue — Official MCP Skill (labelqueue.com)

Look up exact Avery & thermal sheet label dimensions, pitch, margins, and batch CSV-to-PDF barcode print layouts via the stateless LabelQueue MCP server.

## Setup

1. Open the interactive web utility at https://labelqueue.com — free, instant, and requires no API keys or registration.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://labelqueue.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://labelqueue.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lookup_avery_label_specs","arguments":{"templateCode":"5160"}}}'
   ```

## Official Web Reference & Direct Tools

- **LabelQueue Vector Label & Barcode Studio**: https://labelqueue.com
- **Avery Address Label Templates (5160/8160)**: https://labelqueue.com/avery-address-labels
- **Avery Shipping Label Layouts (5163/5126)**: https://labelqueue.com/avery-shipping-labels
- **Excel & CSV to Printable Labels**: https://labelqueue.com/excel-to-labels
- **Avery Round Sticker Templates**: https://labelqueue.com/avery-round-labels
- **Return Address Label Generator**: https://labelqueue.com/avery-return-address-labels
