# Case 3: Supply Chain Digitization for a Tea Beverage Chain

## Background

| Item | Detail |
|------|--------|
| **Brand** | Tea-X (pseudonym) |
| **Type** | Tea beverage chain / predominantly franchised |
| **Scale** | 200+ franchised locations, 12 company-owned |
| **Positioning** | Mid-market tea beverages, primarily tier-2/3/4 cities |
| **Avg. Monthly Revenue per Location** | $11K--$21K |
| **Annual Revenue (Brand)** | ~$28M (including supply chain revenue) |

## Pre-Digital Pain Points

### Scene 1: Franchisees Secretly Sourcing Elsewhere
Core ingredients (tea leaves, creamer powder, boba pearls) should be centrally sourced, but franchisees kept finding cheaper substitutes -- inconsistent taste, negative reviews, brand damage. Headquarters could not detect it until dozens of bad Yelp reviews had already accumulated.

### Scene 2: Inventory -- Always Too Much or Too Little
Franchisees ordered by gut feel -- overstocked in peak season (afraid of running out, leading to expiry) and understocked in the off-season (afraid of waste, then ran out during promotions). Headquarters warehouse had the same problem: too much stock tied up capital; too little stock meant angry franchisees.

### Scene 3: New Product Launches Were a Battle
One new drink: HQ sets pricing, notifies 200 franchisees, ships samples, waits for feedback, finalizes recipe, coordinates distribution -- all via WhatsApp groups and Excel. End-to-end from decision to in-store sale took at least 1 month. Competitors launched in 2 weeks.

### Scene 4: Invisible Food Safety Risks
Shelf-life of ingredients in franchisee back-of-house? Refrigeration temperatures? Headquarters had zero visibility. Food safety was the owner's single greatest anxiety.

## Digital Solution

### Core Strategy: Supply Chain Before Store-Front Digitization

**Why supply chain first?**
- Franchisees are most willing to use digital tools that "save them money" (supply chain adoption beats POS adoption every time)
- Supply chain is the brand's lifeline (taste consistency + food safety)
- Headquarters earns revenue from supply chain (this is the foundation of the business model)

### System Architecture

```
Supplier -> Central Warehouse (owned + leased) -> Regional Hubs -> Stores
   |                   |                            |             |
   +-------------------+---- Supply Chain System (SCM) ------------+
                       |
                       +-- Procurement: supplier price comparison + auto-PO + quality traceability
                       +-- Warehouse Management: WMS (central + regional)
                       +-- Ordering Platform: franchisee app/web portal, one-click ordering
                       +-- Logistics: TMS cold-chain tracking
                       +-- Shelf-Life: IoT temperature tags + expiry alerts
                       +-- Data Center: procurement analytics + demand forecasting + franchisee ordering behavior
```

### Phased Implementation

| Phase | Timing | Action | Investment |
|-------|:------:|--------|:----------:|
| **1. Ordering Platform** | M1--M3 | Franchisee ordering app goes live, replacing WhatsApp-based ordering | $42K |
| **2. WMS Warehouse** | M2--M4 | Central warehouse WMS go-live, barcode-based inbound/outbound | $35K |
| **3. Shelf-Life IoT** | M4--M6 | Cold storage temperature sensors + shelf-life tags (50-store pilot) | $56K |
| **4. TMS Logistics** | M5--M7 | Cold-chain real-time tracking + proof of delivery | $42K |
| **5. AI Forecasting** | M7--M12 | AI demand forecasting (central warehouse + top 50 franchisees) | $49K |

## Results

### Data After 18 Months

| Metric | Before | After | Change |
|--------|:------:|:-----:|:------:|
| Core Ingredient Off-Book Sourcing Rate | ~15% (estimated) | <3% (system-tracked) | **-80%** |
| Franchisee Ordering Efficiency | Hours on WhatsApp | 2 minutes in app | **-95% time** |
| Central Warehouse Inventory Turnover | 45 days | 28 days | **-38%** |
| Store Stockout Rate | 12% | 3% | **-75%** |
| New Product Launch Cycle | 4--6 weeks | 1--2 weeks | **-67%** |
| Ingredient Waste Rate | 8% | 3.5% | **-56%** |
| Food Safety Violations (random audit) | 8/year | 1/year | **-87%** |
| Franchise Renewal Rate | 72% | 88% | **+16pp** |
| HQ Supply Chain Revenue | $16.8M | $22.4M | **+33%** (more core ingredient sales) |

### Franchisee Sentiment
- "Ordering is like shopping on Amazon now -- so easy." -- Franchisee
- "Before, I guessed my order. Now the app tells me what to order." -- Franchisee
- "The app auto-alerts me when stock is about to expire." -- Franchisee

## Lessons Learned

### What Went Right
1. **Supply chain before POS**: Franchisees embrace supply chain first (it saves them money). Zero resistance.
2. **IoT for food safety**: Sensors are more reliable than humans and work 24/7 without fatigue.
3. **Data transparency for franchisees**: Franchisees see their own ordering history, peer benchmarks, and suggested order quantities.
4. **Phased AI rollout**: Stabilized on top-50 stores before full deployment.

### If We Could Do It Again
1. Should have built regional transit hubs earlier -- direct central-warehouse-to-franchisee cold chain was too expensive.
2. Shelf-life IoT should have started with temperature monitoring first, then added full label traceability (all-in-one approach was too costly upfront).

## Universal Takeaway

> For chains that earn their margin from supply chain, **supply chain digitization is not an IT project -- it is a business model upgrade**. Get franchisees to feel "supply chain saves me money" first, and every subsequent system rollout will face far less resistance. The most important first digital system for headquarters may not be the POS -- it may be the supply chain.
