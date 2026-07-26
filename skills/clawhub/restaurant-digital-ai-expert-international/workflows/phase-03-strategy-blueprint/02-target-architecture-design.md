# 02-Target Architecture Design

## Triggers
- After strategic direction is confirmed, design the 3-year target system architecture

## Architecture Design Guide

### Recommended Architecture Patterns by Format & Scale

| Scale | Recommended Architecture | Core Philosophy |
|-------|--------------------------|-----------------|
| 1-10 locations | SaaS composition (2-4 systems) | Pick the best individual SaaS products, lightweight integration |
| 10-100 locations | Core SaaS platform + satellite SaaS | Select 1 main platform (POS/CRM), others integrate into it |
| 100-1,000 locations | Middle-platform architecture | Business middle-platform + data middle-platform, decouple frontend and backend |
| 1,000+ locations | In-house platform + open ecosystem | Unified PaaS foundation, pluggable application layer |

### Target Architecture Design Steps

**Step 1: Draw the Target System Architecture Diagram**

Use the restaurant industry layered architecture:

```
+----------------------------------------------------------+
| Engagement | Mobile App | Web | Kiosk | UberEats | DoorDash |
+----------------------------------------------------------+
| Business   | Store POS | KDS | CRM | Delivery Agg | Inventory | Scheduling |
+----------------------------------------------------------+
| Platform   | Order Center | Product Center | Member Center | Marketing Center | Data Center |
+----------------------------------------------------------+
| Data       | Data Warehouse | BI Reports | AI Models | Real-time Stream | Data Governance |
+----------------------------------------------------------+
| Foundation | Cloud Services | IoT | Network | Security | Operations |
+----------------------------------------------------------+
```

**Step 2: Define System Boundaries & Interfaces**

| System | Core Responsibility | Upstream Systems | Downstream Systems | Key Interface |
|--------|--------------------|-----------------|--------------------|---------------|
| POS | Payment, ordering, order management | -- | KDS, CRM, Inventory | REST API |
| KDS | Kitchen order display, production management | POS | -- | WebSocket |
| CRM | Member data, tiers, points | POS, Mobile App | BI | REST API |
| ... | ... | ... | ... | ... |

**Step 3: Design the Data Architecture**

- Master data standards: menu item codes / location codes / supplier codes / member IDs
- Data flows: POS -> Data Warehouse -> BI / Predictive Models
- Data governance: who is responsible for what data, data quality standards

**Step 4: Define Technical Standards**

| Standard | Requirement |
|----------|-------------|
| API Protocol | RESTful HTTPS / gRPC |
| Authentication | OAuth 2.0 / JWT |
| Data Format | JSON / Protobuf |
| Logging Standards | Unified format + centralized collection |
| Deployment | Containerized (K8s) / SaaS / Hybrid |

## Deliverables
- Target system architecture diagram (draw.io source file)
- System boundary & interface matrix
- Data architecture design overview
- Technical standards document

## Quality Checks
- [ ] Architecture diagram answers "what does this system do, and what does it connect to"
- [ ] No over-engineering (10 locations don't need K8s + microservices + Service Mesh)
- [ ] Data architecture addresses data quality and governance
- [ ] Architecture principles are consistent with the client's maturity stage
