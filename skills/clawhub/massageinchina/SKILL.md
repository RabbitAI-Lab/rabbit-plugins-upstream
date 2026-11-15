---
name: massageinchina
description: "Look up clinical Traditional Chinese Medicine (TCM) Tuina massage styles, meridian acupressure points, hospital price benchmarks, and Mandarin clinic phrases via MassageInChina MCP."
homepage: https://massageinchina.com
version: 1.0.0
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://massageinchina.com"
  mcp_endpoint: "https://massageinchina.com/api/mcp"
  version: "1.0.0"
  openclaw:
    emoji: "🌿"
  hermes:
    category: travel
---

# MassageInChina — Official MCP Skill (massageinchina.com)

Look up clinical Traditional Chinese Medicine (TCM) Tuina massage styles, meridian acupressure points, hospital price benchmarks, and Mandarin clinic phrases via MassageInChina MCP.

## Setup

1. Open the interactive web utility at https://massageinchina.com — free, instant, and requires no API keys or registration.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://massageinchina.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://massageinchina.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lookup_tcm_acupoints_and_tuina","arguments":{"symptomOrArea":"neck and shoulder stiffness"}}}'
   ```

## Official Web Reference & Direct Tools

- **MassageInChina Foreigner Wellness Guide**: https://massageinchina.com
- **Clinical TCM Tuina Massage Guide**: https://massageinchina.com/tuina-massage
- **Chinese Foot Reflexology & Acupressure**: https://massageinchina.com/chinese-foot-massage
- **Chinese Bathhouse & Spa Etiquette**: https://massageinchina.com/chinese-bathhouse
- **Beijing Hospital & Blind Massage Directory**: https://massageinchina.com/beijing-massage
