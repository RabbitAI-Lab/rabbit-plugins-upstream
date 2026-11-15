---
name: taofind
description: "China cross-border sourcing workbench: clean wrapped 1688/Taobao/Weidian links, compute international LxWxH/5000 volumetric haul shipping, compare 18 shopping agents' FX fees, and convert Asian apparel sizes via TaoFind."
homepage: https://taofind.com
version: 1.0.0
license: MIT
compatibility: "Works with Claude Code, Cursor, Windsurf, Cline, OpenClaw, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://taofind.com"
  mcp_endpoint: "https://taofind.com/api/mcp"
  version: "1.0.0"
---

# TaoFind — 1688 Link Cleaner, Volumetric Shipping & Agent Cost Matrix

Connects AI coding assistants and cross-border sourcing researchers to [**TaoFind**](https://taofind.com) via its stateless `streamable-http` Model Context Protocol endpoint (`https://taofind.com/api/mcp`).

## Available MCP Tools

- **`unwrap_and_clean_china_marketplace_link`**: Extract clean canonical product IDs and native raw URLs from wrapped Taobao, 1688, Weidian, or third-party shopping agent redirect links (Superbuy, CNFans, Mulebuy, AllChinaBuy), stripping tracking tokens.
- **`calculate_volumetric_haul_shipping`**: Calculate chargeable shipping weight comparing actual scale weight vs dimensional volumetric weight (L x W x H / 5000 for DHL/FedEx, /6000 for Tax-Free Line, /8000 for EUB) and recommend box removal savings.
- **`compare_china_shopping_agents`**: Compare verified Chinese purchasing agents (Basetao, CSSBuy, Kakobuy, Sugargoo, Superbuy, Mulebuy, AllChinaBuy, CNFans) by hidden USD/CNY exchange rate markup (4.8% to 6.8%), parcel weight freight, and total landed cost.
- **`convert_asian_apparel_and_shoe_size`**: Convert Chinese/Asian apparel labels (M, L, XL, 2XL, 175/92A) and Chinese EU shoe sizes to US/UK standards with exact centimeter chest/shoulder ranges, flagging Asian slim-fit sizing allowances.
- **`estimate_customs_declaration_strategy`**: Compute standard weight-based customs declaration benchmarks ($12-$14/kg reference for North America vs Tax-Free Triangle IOSS lines for EU/UK) and ideal parcel split thresholds (<10kg).
- **`list_verified_china_sourcing_tools`**: Retrieve direct landing endpoints for TaoFind 1688 link cleaner, Weidian unwrapper, shipping calculator, Asian size converter, and agent fee matrix.

## Official Web Workbenches & Reference

- [**1688 & Taobao Link Cleaner**](https://taofind.com/tools/1688-link-converter)
- [**Weidian Raw Link Unwrapper**](https://taofind.com/tools/weidian-link-converter)
- [**Volumetric Haul Shipping Calculator**](https://taofind.com/tools/shipping-calculator)
- [**18-Agent FX Spread & Freight Comparison**](https://taofind.com/tools/agent-comparison)
- [**Asian to US/EU Size Chart Converter**](https://taofind.com/tools/size-converter)
- [**Machine-Readable Corpus**](https://taofind.com/llms.txt)
