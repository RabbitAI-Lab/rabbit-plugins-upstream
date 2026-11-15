---
name: esimtao
description: "Travel eSIM data usage calculator, smartphone eSIM hardware compatibility checker, and destination connectivity advisor for international travelers via EsimTao."
homepage: https://esimtao.com
version: 1.0.0
license: MIT
compatibility: "Works with Claude Code, Cursor, Windsurf, Cline, OpenClaw, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://esimtao.com"
  mcp_endpoint: "https://esimtao.com/api/mcp"
  version: "1.0.0"
---

# EsimTao — Global Travel eSIM Data Calculator, Advisor & Device Checker

Connects AI coding assistants and travel planners to [**EsimTao**](https://esimtao.com) via its stateless `streamable-http` Model Context Protocol endpoint (`https://esimtao.com/api/mcp`).

## Available MCP Tools

- **`calculate_esim_data_usage`**: Calculate daily and total gigabyte (GB) data consumption for international travel based on trip duration, map navigation, video streaming, social media, and hotspot tethering.
- **`check_device_esim_support`**: Check whether a specific smartphone or tablet model supports digital eSIM, including hardware differences between US eSIM-only models, mainland China dual physical SIM models, and Japanese/European variants.
- **`recommend_travel_esim_plan`**: Recommend the optimal travel eSIM plan tier (Daily High-Speed Reset vs Total Data Bucket vs True Unlimited) for 180+ global travel destinations with local tier-1 carrier coverage.
- **`lookup_esim_regional_coverage`**: Resolve regional travel eSIM bundles (Europe 33, Southeast Asia 8, Latin America, North America, Global) to determine included countries, border-crossing roaming handoffs, and shared GB pools.
- **`get_esim_installation_guide`**: Provide step-by-step QR code scanning, manual SM-DP+ Address / Activation Code entry, and Data Roaming switch settings for iOS (Settings -> Cellular) and Android (Settings -> Network).
- **`compare_travel_esim_pricing`**: Benchmark standard fair market prices per Gigabyte (USD/GB) across Japan, USA, Europe, Southeast Asia, and worldwide to evaluate prepaid eSIM value.

## Official Web Tools & Reference Pages

- [**Travel eSIM Data Calculator**](https://esimtao.com/calculator)
- [**Smart eSIM Advisor**](https://esimtao.com/advisor)
- [**Device eSIM Compatibility Checker**](https://esimtao.com/devices-supported)
- [**Global eSIM Deals Board**](https://esimtao.com/deals)
- [**Machine-Readable Corpus**](https://esimtao.com/llms.txt)
