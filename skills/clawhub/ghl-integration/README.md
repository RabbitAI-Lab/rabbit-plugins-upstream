# 🚀 GoHighLevel (GHL) API v2 Integration & CRM Automation Engine

[![Habilis Gateway](https://img.shields.io/badge/Habilis_Gateway-xvix.com.br-2563eb.svg)](https://xvix.com.br)
[![ClawHub](https://img.shields.io/badge/ClawHub-Skill-10b981.svg)](https://clawhub.ai)
[![Zero Storage](https://img.shields.io/badge/Security-Zero_Storage_Stateless-blueviolet.svg)](https://xvix.com.br)
[![Author](https://img.shields.io/badge/Author-Rafa_Martins-orange.svg)](https://portal.sthub.com.br)

Production-grade autonomous integration skill for **GoHighLevel (GHL) API v2**, multi-channel CRM automation (Email, SMS, WhatsApp), pipeline & Kanban synchronization, and lead qualification via AI Agents.

---

## 🏛️ Architecture & Habilis MCP Gateway

This skill integrates seamlessly with the **Habilis SaaS MCP Gateway** (`https://xvix.com.br/api/mcp`).

```
┌─────────────────────────────────────────────────────────────┐
│                    AI Agent (Hermes / Claude)               │
└──────────────────────────────┬──────────────────────────────┘
                               │ MCP JSON-RPC 2.0 (Bearer Auth)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│             Habilis SaaS Gateway (xvix.com.br)              │
│       • Zero-Storage Security (Stateless Authorization)     │
│       • Dynamic Plan Quotas & Telemetry Engine              │
└──────────────────────────────┬──────────────────────────────┘
                               │ Direct GHL API v2 Calls
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   GoHighLevel CRM (v2)                      │
│     Contacts • Opportunities • Workflows • Pipelines        │
└─────────────────────────────────────────────────────────────┘
```

- **Obtain Habilis Token / API Access**: [https://xvix.com.br](https://xvix.com.br)
- **Support & Developer Portal**: [https://portal.sthub.com.br](https://portal.sthub.com.br)

---

## ✨ Features

- **Automated Lead Ingestion**: Instant sync with inbound webhooks and Meta Ads campaigns.
- **Unanswered Leads Triaging**: Smart categorization (Billing, Inbound Lead, System Alert, False Positive).
- **Kanban & Pipeline Sync**: Automated card movements across opportunity stages.
- **Direct Multi-Channel Dispatch**: Send Email, SMS, and WhatsApp messages via certified connectors.
- **Zero-Storage Privacy**: High-security stateless credentials handling.

---

## 🛠️ MCP Tools Reference

| Tool Name | Description |
|---|---|
| `ghl_list_contacts` | Fetch, filter, and search contacts with tag matching and pagination |
| `ghl_create_or_update_contact` | Create or update CRM contact records with custom fields |
| `ghl_get_pipeline_opportunities` | Inspect Kanban stages and lead opportunity states |
| `ghl_trigger_workflow` | Enroll contacts into automated GoHighLevel nurture sequences |

---

## 👤 Author & Support

- **Author**: Rafa Martins
- **Email**: rafacpti@gmail.com
- **WhatsApp Support**: [wa.me/5527999082624](https://wa.me/5527999082624)
- **Website**: [portal.sthub.com.br](https://portal.sthub.com.br)
- **Token & Platform**: [xvix.com.br](https://xvix.com.br)
