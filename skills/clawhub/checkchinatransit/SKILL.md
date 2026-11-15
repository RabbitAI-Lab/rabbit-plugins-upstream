---
name: checkchinatransit
description: "Verify China 240-hour and 24-hour visa-free transit (TWOV) passport eligibility across 54 nationalities, validate A-B-C third-country routing rules, compute midnight stay deadlines, and inspect 60 eligible entry/exit port zones via CheckChinaTransit MCP."
homepage: https://checkchinatransit.com/
version: 1.0.1
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://checkchinatransit.com/"
  mcp_endpoint: "https://checkchinatransit.com/api/mcp"
  version: "1.0.1"
  openclaw:
    emoji: "✈️"
  hermes:
    category: travel
---

# CheckChinaTransit — Official MCP Skill (checkchinatransit.com)

Verify China 240-hour and 24-hour visa-free transit (TWOV) passport eligibility across 54 nationalities, validate A-B-C third-country routing rules, compute midnight stay deadlines, and inspect 60 eligible entry/exit port zones via CheckChinaTransit MCP.

## Setup

1. Open the interactive web studio at https://checkchinatransit.com/ and explore https://checkchinatransit.com/countries/ — 100% free, public, and requires no API key or sign-in.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://checkchinatransit.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://checkchinatransit.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"check_china_twov_nationality_eligibility","arguments":{"nationality":"United States"}}}'
   ```

## Official Web Reference & Deep Endpoints

- **CheckChinaTransit 24/240-Hour TWOV Compliance Checker**: https://checkchinatransit.com/
- **54 Qualifying Countries for China Visa-Free Transit**: https://checkchinatransit.com/countries/
- **60 Approved Entry/Exit Ports & Cross-Province Zones**: https://checkchinatransit.com/ports/
- **240-Hour (Formerly 144-Hour) Transit Policy Breakdown**: https://checkchinatransit.com/144-hour/
- **Step-by-Step Airport Arrival & Check-In Guide**: https://checkchinatransit.com/guide/
- **China Visa & Arrival Photo Specification Checker**: https://checkchinatransit.com/visa-photo/
