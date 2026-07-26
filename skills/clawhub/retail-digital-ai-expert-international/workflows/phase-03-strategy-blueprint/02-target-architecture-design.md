# 02 — Target Architecture Design

> **Trigger**: Digital strategy confirmed
> **Deliverables**: Target architecture diagram + system boundary definitions + integration strategy + data architecture outline

---

## 1. Four Architecture Design Principles

1. **Cloud-First**: New systems default to SaaS / cloud-native; avoid building on-premise data centers
2. **API-First**: All systems must provide standard RESTful APIs; no point-to-point database connections
3. **Mobile-First**: The primary interaction interface for staff / managers / store managers is the mobile phone
4. **Data as an Asset**: All system data must be aggregatable, analyzable, and migratable (no vendor lock-in)

---

## 2. Retail Layered Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Customer Touchpoints (Frontend)          │
│  In-Store POS │ Mini-App │ Mobile App │ Amazon │ TikTok  │
│              │ Shopify │ Instagram │ Uber Eats           │
├─────────────────────────────────────────────────────────┤
│                  Business Applications                    │
│  POS │ ERP │ WMS │ OMS │ CRM │ eCommerce │ BI │ AI Apps  │
├─────────────────────────────────────────────────────────┤
│                  Middle Platform (Shared Services)        │
│  Product Center │ Order Center │ Inventory Center         │
│  Member Center │ Pricing Center                           │
├─────────────────────────────────────────────────────────┤
│                  Data Platform                            │
│  Data Lake │ CDP │ BI │ AI/ML Platform │ Data Governance  │
│  Master Data Management (MDM)                             │
├─────────────────────────────────────────────────────────┤
│                  Infrastructure                           │
│  Cloud Platform │ Network │ IoT │ Security │ Ops │ Edge   │
└─────────────────────────────────────────────────────────┘
```

---

## 3. Layer-by-Layer Design Guidance

### 3.1 Customer Touchpoint Layer

| Touchpoint | Design Principle | Key Capabilities |
|------|------|------|
| In-Store POS | Offline-capable, sub-second response, simple enough for anyone to learn in 30 min | Checkout + membership + inventory + payments |
| Mobile Mini-App | WhatsApp/WeChat ecosystem native experience | Storefront + membership + live shopping + group buying |
| Mobile App | Only for large brands / high-frequency scenarios | Personalization + push notifications |
| Third-Party eCommerce | Amazon / Shopify / TikTok Shop | Product sync + order integration + inventory allocation |

### 3.2 Business Application Layer

| System | Boundary & Responsibility | Does NOT Do |
|------|------|------|
| POS | Checkout, member ID, inventory lookup, payments | Procurement planning, financial general ledger |
| ERP | Purchasing, inventory, finance, reporting | Real-time personalized recommendations |
| WMS | Warehouse receiving, put-away, picking, shipping, cycle counts | Store-level inventory management (that's POS/ERP) |
| OMS | Omnichannel order aggregation, routing, fulfillment tracking | Product management |
| CRM / CDP | Member profiles, tagging, segmentation, marketing automation | Transaction processing |

### 3.3 Middle Platform (Shared Services) Layer

| Shared Service | Responsibility | Key APIs |
|------|------|------|
| Product Center | Unified omnichannel product information | Product query / create / update |
| Order Center | Unified omnichannel order management | Order create / query / status update |
| Inventory Center | Real-time omnichannel inventory | Inventory query / reserve / release |
| Member Center | Unified member ID / tier / benefits | Member query / register / tier change |
| Pricing Center | Unified price management + promo engine | Price lookup / promotion calculation |

---

## 4. System Boundary Definition (Example: ERP)

```
Within ERP Boundary:
  ✓ Procurement management (PR → PO → Receiving → Payment)
  ✓ Inventory management (warehouse + store inventory + transfers)
  ✓ Financial management (GL / AR / AP / Cost Accounting)
  ✓ Reporting & analytics

Outside ERP Boundary (handled by other systems):
  ✗ Checkout (handled by POS)
  ✗ Member marketing (handled by CRM/CDP)
  ✗ Real-time recommendations (handled by AI engine)
  ✗ eCommerce front-end display (handled by eCommerce platform)

ERP Interactions with External Systems:
  ERP ←→ POS (sales data / inventory sync)
  ERP ←→ WMS (inbound/outbound / inventory)
  ERP ←→ Financial System (journal entries / reports)
```

---

## 5. Integration Strategy

### Integration Pattern Selection

| Integration Scenario | Recommended Pattern | Technology |
|------|------|------|
| Real-time transactions (e.g., inventory lookup) | Synchronous API call | REST / gRPC |
| Async data sync (e.g., product info) | Message queue | Kafka / RabbitMQ |
| Large data volume (e.g., historical transactions) | Batch ETL | Data sync tools |
| Cross-system workflows (e.g., order create → inventory → notification) | Event-driven | Event Bus / Webhooks |

### Integration Inventory Template

| System A | System B | Direction | Data Type | Frequency | Priority |
|------|------|------|------|:---:|:---:|
| POS | ERP | POS → ERP | Sales transactions | Real-time | P0 |
| ERP | WMS | ERP → WMS | Inbound/outbound orders | Real-time | P0 |
| WMS | ERP | WMS → ERP | Inventory changes | Real-time | P0 |
| CRM | CDP | CRM → CDP | Member data | T+1 | P1 |

---

## 6. Data Architecture Outline

### Master Data Management (MDM)

| Master Data Domain | Data Owner | Authoritative Source | Distribution Targets |
|------|------|------|------|
| Product (SKU) | Merchandising | PIM / ERP | POS / WMS / eCommerce / BI |
| Store / Warehouse | Operations | ERP | POS / WMS / OMS |
| Supplier | Procurement | ERP / SRM | WMS / Finance |
| Member | CRM | CDP | POS / eCommerce / WeCom / Slack |
| Organization / Employee | HR | HR System | All systems |

---

## 7. Common Pitfalls

1. **Over-engineering**: Designing a full microservices + event bus architecture for 50 stores → start with SaaS and integrate
2. **Ignoring integration complexity**: Assuming "they all have APIs so they'll work together" → API format / semantics / performance are all pitfalls
3. **No MDM ownership**: Each system maintains its own product / store data → data will never reconcile
4. **"Middle Platform" obsession**: Treating "middle platform" as a silver bullet → without sufficient data volume and use cases, it's just added complexity
