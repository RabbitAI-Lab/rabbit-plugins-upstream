# Case 08: AI Optimization of a City Bus Network

## Case Overview

| Dimension | Detail |
|-----------|--------|
| City type | Mid-sized US city ( metro population 1.5M) |
| Operator | Municipal transit authority (public) |
| Fleet | 1,180 buses (65% electric) |
| Lines | 80 (before) → 72 (after) + 3 DRT zones |
| Daily ridership | 280,000 (before, declining ~5%/yr) |
| Annual revenue | $40M (fare $15M + public subsidy $25M) |
| Total investment | $62 million (AI network optimization + digital upgrade) |
| Delivery period | 2021–2022 |
| Operator | Municipal transit authority |

---

## 1. Where Did the Riders Go? — The Bus's "Slow Death"

### 1.1 A Decade of Decline

The transit authority has a 65-year history as the city's mobility lifeline. But since the 2010s, the curve turned down:

| Year | Daily ridership (k) | YoY | Cumulative (vs 2012) |
|------|--------------------|-----|------------------------|
| 2012 | 520 | — | — (peak) |
| 2015 | 440 | −5.1% | −15.4% |
| 2018 | 360 | −6.2% | −30.8% |
| 2020 | 280 | −11.1% (pandemic) | −46.2% |

**In a decade, ridership halved.** Meanwhile car ownership rose from 180k to 550k; bike-share >30k; ride-hail 150k orders/day.

### 1.2 Fatal Structural Problems

1. **Aging network:** 60%+ of 80 lines planned >10 yrs ago, when the built-up area was 40% of today's. E.g., 3 lines still served a relocated old terminal, while new CBDs and residential districts were under-served.
2. **Misallocated resources:** 20% of "hot" lines (high load) carried 55% of riders but got 35% of vehicles; many "cold" lines ran <30% load, yet cutting them met resident/advocate opposition.
3. **Failed rail competition:** after light-rail Line 1 opened (2018), parallel Bus 8 fell 60% in a year, but the authority failed to reposition it (from trunk to feeder).
4. **Subsidy dependence:** public subsidy rose from $8M (2012) to $25M (2020) — 30% → 61% of revenue. Funder patience was thinning.

### 1.3 The Turning Point

Early 2021, a new CEO declared "look inward, let data speak" and decided to apply AI to a full network optimization — the authority's first, replacing "old experts drawing lines by experience."

---

## 2. AI Network-Optimization Methodology

### 2.1 Data Foundation: Multi-Source Fusion OD

AI needs precise OD (origin–destination). Traditional "ride-check" surveys are slow, low-accuracy, costly. This project fused:

| Source | Covers | Provides | Limit |
|--------|--------|----------|-------|
| Smart-card (EMV/contactless) | Card riders (~60%) | Boarding stop + time | No alight/ purpose |
| Mobile-ticket app | App riders (~30%) | Board/alight + chain | App users only |
| Mobile network data | Residents (~70%) | All-mode OD + purpose | 100–300 m accuracy; mode unknown |
| LBS data | Residents (~40%) | High-acc OD + purpose + profile | Young-user bias |
| Bike-share data | Cyclists | Bus feeder OD | Bike-share users only |

**Fusion:** a hidden-Markov-model chain-reconstruction fused card, signaling trajectories, and POI sequences into full trip chains — ~120k OD records/day at stop-level accuracy.

### 2.2 AI Network Model

**Step 1 — Demand analysis:** identify high-OD corridors (>400 pax/h); service gaps.

**Step 2 — Network generation:** multi-objective genetic algorithm (NSGA-II):
- Maximize OD coverage
- Minimize total travel time (walk+wait+ride+transfer)
- Minimize operating cost ($/veh-km)
- Maximize fare revenue
- Constraints: length (5–16 mi), directness (<1.6), headway (3–15 min), fleet (≤1,180)

**Step 3 — Evaluation:** agent-based micro-simulation (MATSim): 1M+ agents; outputs ridership, cost, experience.

**Step 4 — Comparison:** 3–5 candidate plans with adjustments, forecasts, cost, subsidy need for board/funder decision.

### 2.3 Optimization Plan

| Adjustment | Count | Example |
|-----------|-------|---------|
| Cancel | 8 | Duplicated rail, <100 pax/day |
| Reroute | 15 | Serve new residential/industrial; skip-stop speed-up |
| Add | 5 | Underserved new districts / employment areas |
| Headway optimize | 28 | Hot lines 5→3 min peak; cold lines lengthen |
| DRT | 3 zones | Low-density suburbs, flexible |

**3 DRT zones:** tech park (18 km², dispersed), university town (12 km², tidal), exurb (25 km², high fixed-route cost). DRT: app request → AI pooling → dynamic route → 12–19 seat shuttle. Fare $3–5 vs $1–2 fixed, below ride-hail.

---

## 3. Implementation: Hardest Is Not the Algorithm, But People

### 3.1 The Line-Cancellation Storm

On announcement, riders on the 8 cancelled lines reacted fiercely:
- Residents of one senior community gathered at city hall
- A retiree wrote a 3,000-word letter to the mayor
- A council member filed an "urgent resolution to keep Route 33"

### 3.2 Response Strategy

1. **Open data:** QR codes at each affected stop — reason, ridership, alternative
2. **Hearings & community meetings:** one per cancelled line, led by a VP, face-to-face
3. **Transition:** not abrupt — first lengthen headway (30→60 min), observe 3 months, cancel only if no recovery
4. **Alternatives in place:** ensure each area had an alternative (other bus + bike-share + DRT)
5. **Vulnerable groups:** community shuttles (19-seat) for senior homes/schools

### 3.3 Driver Reassignment

~120 driver roles affected. "Reassign, don't lay off":
- 50 → new lines / DRT
- 30 → thickened hot lines
- 20 → custom/charter
- 20 → voluntary early retirement / negotiated exit (N+3)

Union involved throughout → "zero complaint, zero arbitration."

---

## 4. Digital Supporting Upgrade

### 4.1 Real-Time Bus App

$8M "CityBus" app:
- Real-time position + arrival prediction (±30 s)
- Multimodal trip planning (bus + bike-share + walk)
- Boarding alert; scan-to-ride; live crowding (red/yellow/green)
- DRT booking; lost-and-found; feedback
- 280k registrations (100% of daily riders); 150k MAU; 4.4/5 rating

### 4.2 Transit Signal Priority (TSP)

TSP at 82 intersections on 10 trunk corridors:
- Bus requests priority 200 m ahead via C-V2X/4G
- Green extension (max +10 s) or red truncation (max −8 s)
- Result: 10 corridors travel time −15%; on-time 72% → 88%

---

## 5. Outcomes

| Metric | Before | After (1 yr) | Change |
|--------|--------|-------------|--------|
| Daily ridership | 280k | 320k | +14.3% |
| Avg line ridership | 3,500/day | 4,445/day | +27.0% |
| Revenue / veh-km | $0.45 | $0.53 | +18.7% |
| Operating cost | $440M/yr | $374M/yr | −14.9% |
| Public subsidy | $25M/yr | $19.9M/yr | −20.6% |
| Daily veh-km | 115 | 127 | +10.8% |
| Avg travel time | 42 min | 35 min | −16.7% |
| Transfer coefficient | 1.15 | 1.28 | +11.3% |
| Satisfaction | 68 | 88 | +20 pts |
| DRT daily orders | 0 | 3,200 | — |

---

## 6. Lessons

1. **OD data is the root of network optimization:** no precise OD, AI is "garbage in, garbage out." This project spent 8 months / $7M on fusion — the most worthwhile spend. Collect ≥1 full annual cycle (seasons, weekdays/weekends/holidays).
2. **Network optimization is not pure tech:** AI finds the mathematical optimum, but that may mean "cancel the only bus an 80-year-old takes to buy groceries." Final plans need "humanized adjustment" — keep a few high-social, low-economic "equity lines."
3. **DRT cracks the "last mile":** 3 DRT zones, 3,200 orders/day, ~$9/order cost (fare $3–5 + subsidy $2–3) — high subsidy, but far below fixed-route cost (~$17/order) at equal density.
4. **Cancellation needs "soft landing":** give residents knowledge, participation, transition time. 5 months from notice to cut, 3 as transition — "wasted" but bought long-term stability.
5. **Plan rail competition early:** bus must be rail's "capillary" — feed riders to rail. One year post-optimization, bus-rail transfer share rose 12% → 28% (rail "brought" new bus riders).
6. **The bus industry's way out is digital:** this case proved ridership can be reversed — understand shifting demand with data, raise precision with tech. The authority's AI optimization is a positive signal for the sector.

---

*Case authored: March 2024 | Sources: authority annual report, OD survey, city mobility annual report*
