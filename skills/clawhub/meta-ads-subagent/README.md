# 📊 Meta Ads Autonomous Subagent ($49 USD Value Engine)

[![Habilis Gateway](https://img.shields.io/badge/Habilis_Gateway-xvix.com.br-2563eb.svg)](https://xvix.com.br)
[![ClawHub](https://img.shields.io/badge/ClawHub-Skill-10b981.svg)](https://clawhub.ai)
[![Zero Storage](https://img.shields.io/badge/Security-Zero_Storage_Stateless-blueviolet.svg)](https://xvix.com.br)
[![Author](https://img.shields.io/badge/Author-Rafa_Martins-orange.svg)](https://portal.sthub.com.br)

Autonomous AI Marketing & Meta Ads Management Skill for Hermes Agent and MCP Clients. Provides 3-level naming hierarchy, high-converting SVG 1080x1080 ad creative generation, real-time bid tuning, CPA audit, and batch orchestration.

---

## 🏛️ Architecture & Habilis SaaS MCP Gateway

```
┌─────────────────────────────────────────────────────────────┐
│                    AI Agent (Hermes / Claude)               │
└──────────────────────────────┬──────────────────────────────┘
                               │ MCP JSON-RPC 2.0 (Bearer Auth)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│             Habilis SaaS Gateway (xvix.com.br)              │
│       • High-Converting SVG 1080x1080 Ad Generator Engine   │
│       • Automatic Bid Auditing & CPA Triage                 │
│       • Stateless Zero-Storage Authorization                │
└──────────────────────────────┬──────────────────────────────┘
                               │ Graph API v24.0 (Client Token)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    Meta Ads Platform                        │
│          Campaigns • Ad Sets • Creatives • Insights         │
└─────────────────────────────────────────────────────────────┘
```

- **Obtain Habilis Token / API Access**: [https://xvix.com.br](https://xvix.com.br)
- **Support & Developer Portal**: [https://portal.sthub.com.br](https://portal.sthub.com.br)

---

## ⚡ Key Capabilities

1. **3-Level Hierarchical Nomenclature**:
   - **Campaign**: `[STATUS] {ID} [{OBJECTIVE}] {STRUCTURE}_{BUDGET}_[{OFFER}] – {DATE}`
   - **Ad Set**: `{CAMPAIGN}.{SUB}_{CREATIVE}_{AUDIENCE}_{PLACEMENT}_{DATE}`
   - **Ad**: `Ad01 - {Headline} | {Price} | {Variant}`
2. **Automated Vector Creative Generation**: Modern 1080x1080 SVG banners with badge, headline, and call-to-action rendered on the fly.
3. **Budget & Bid Tuning**: Proactive CPA auditing and automated bid adjustments across active ad sets.
4. **Zero-Storage Compliance**: Graph API access tokens are processed ephemerally in RAM and never persisted.

---

## 🛠️ MCP Tools Reference

| Tool Name | Description |
|---|---|
| `meta_ads_create_campaign` | Create structured Meta Ads campaign with budget, objective, and targeting |
| `meta_ads_generate_creative_1080` | Generate high-converting 1080x1080 SVG ad creative with custom typography & badge |
| `meta_ads_audit_and_tune_bids` | Audit performance, CPA, and optimize automatic bid adjustments across ad sets |

---

## 👤 Author & Support

- **Author**: Rafa Martins
- **Email**: rafacpti@gmail.com
- **WhatsApp Support**: [wa.me/5527999082624](https://wa.me/5527999082624)
- **Website**: [portal.sthub.com.br](https://portal.sthub.com.br)
- **Token & Platform**: [xvix.com.br](https://xvix.com.br)
