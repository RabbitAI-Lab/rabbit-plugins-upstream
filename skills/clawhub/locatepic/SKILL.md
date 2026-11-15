---
name: locatepic
description: "Calculate solar shadow azimuth and latitude geometry, query regional driving sides, road markings, calling codes and electrical grid standards, and inspect EXIF GPS metadata tag definitions via LocatePic MCP."
homepage: https://locatepic.com/
version: 1.0.1
license: MIT
compatibility: "Works with OpenClaw, Hermes Agent, Claude Code, Cursor, Windsurf, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://locatepic.com/"
  mcp_endpoint: "https://locatepic.com/api/mcp"
  version: "1.0.1"
  openclaw:
    emoji: "📍"
  hermes:
    category: utilities
---

# LocatePic — Official MCP Skill (locatepic.com)

Calculate solar shadow azimuth and latitude geometry, query regional driving sides, road markings, calling codes and electrical grid standards, and inspect EXIF GPS metadata tag definitions via LocatePic MCP.

## Setup

1. Open the interactive web studio at https://locatepic.com/ and explore https://locatepic.com/solar-shadow-calculator — 100% free, public, and requires no API key or sign-in.
2. Connect any MCP-compatible agent or OpenClaw client directly to the stateless Streamable HTTP endpoint:
   ```
   https://locatepic.com/api/mcp
   ```
3. Or invoke via JSON-RPC 2.0 HTTP POST:
   ```bash
   curl -s -X POST https://locatepic.com/api/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lookup_driving_side_and_road_lines","arguments":{"countryOrRegion":"Japan"}}}'
   ```

## Official Web Reference & Deep Endpoints

- **LocatePic Visual Geolocation & EXIF Studio**: https://locatepic.com/
- **Solar Shadow Latitude & Azimuth Calculator**: https://locatepic.com/solar-shadow-calculator
- **Global Visual Geolocation Clues Encyclopedia**: https://locatepic.com/clues
- **Driving Side & Road Line Markings by Country**: https://locatepic.com/clues/driving-side-by-country
- **International Phone Calling Codes & ccTLD Reference**: https://locatepic.com/clues/phone-calling-codes
- **Interactive Route & Coordinate Trace Utility**: https://locatepic.com/route-trace
