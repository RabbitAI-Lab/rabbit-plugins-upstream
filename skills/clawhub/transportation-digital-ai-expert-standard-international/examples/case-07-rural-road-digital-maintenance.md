# Case 07: Digital Maintenance of Rural Roads

## Case Overview

| Dimension | Detail |
|-----------|--------|
| Area type | County (mountainous, Mountain West, USA) |
| Maintained road length | 832 km (county 185 km, township 312 km, village 335 km) |
| Bridges | 186 (incl. 23 structurally deficient) |
| Terrain | 75% mountainous; 1,800 m elevation range |
| Total investment | $11 million (three years) |
| Delivery period | 2021–2023 |
| Policy backdrop | FHWA Transportation Asset Management (TAM) / local-road modernization |
| Operator | County Public Works — Road Maintenance Division |

---

## 1. "Dust in Sun, Mud in Rain" — The Traditional Maintenance Dilemma

### 1.1 Guardians of Mountain Roads

Cloud County (a pseudonymized composite of real US rural-county programs) spans 832 km of rural roads across rugged terrain. The division has only 8 full-time staff maintaining 800+ km of road.

The traditional approach was disheartening:
- **Manual foot patrol:** each township road patrolled monthly by motorcycle or on foot with paper logs; coverage <40% due to access difficulty.
- **Paper ledgers:** all inspection, repair, and bridge records on paper — two filing cabinets; finding a road's history took 30+ minutes.
- **"Fix-when-broken" mode:** no condition forecasting; most repairs were reactive ("pavement failed, citizens complained"). Preventive maintenance near zero.
- **Funding black hole:** ~$1.7M/yr maintenance, but with no precise asset data or decision support, allocation was by "manager's gut" — likely under half truly well-spent.

### 1.2 An Inspection That Changed Everything

In 2020, a state TAM audit found:
- The road-supervisor ("road boss") program was "name only" — listed but no KPI, tools, or data
- Pavement condition (PCI) rating coverage was 12% (state avg 65%)
- Structurally deficient bridge rehabilitation badly lagged — only 5 of 23 rebuilt

The audit shook the county commission, which declared digital maintenance the year's top public-works priority.

---

## 2. "Doing Much in a Small Space" — How to Spend $11M

### 2.1 A Pragmatic Plan Under Budget Constraint

$11M over three years is modest for 800+ km. Core principle: **mobile-first, cloud-deployed, low-cost sensors, leverage existing resources.** No big video wall, no command-center fit-out, no high-end hardware — everything centered on "field crews can use it, afford it."

### 2.2 Investment Breakdown

| Item | Amount ($M) | Share | Note |
|------|-------------|-------|------|
| Road-supervisor app + mgmt platform | 1.65 | 15% | SaaS: patrol, report, KPI |
| Rural-road GIS database | 1.1 | 10% | Built on ESRI/OSM APIs, not a self-built engine |
| Smart pavement collection | 2.05 | 18.7% | Phone AI app + 2 drones + 3 vehicle kits |
| Bridge IoT monitoring | 2.5 | 22.5% | 20 key bridges: tilt + crack + water-level |
| Public reporting widget | 0.55 | 5% | Mobile web app, photo reporting |
| Maintenance decision support | 1.4 | 12.5% | AI fund-allocation optimization |
| Cloud + O&M (3 yrs) | 1.1 | 10% | Public cloud + ops |
| Training & rollout | 0.7 | 6.3% | 18 township supervisors + crews |
| **Total** | **11.0** | **100%** | — |

---

## 3. Core Systems

### 3.1 Road-Supervisor App — "Make the Supervisor Real"

The road-supervisor program had long been a "wall poster." The app tackles three problems:

**Problem 1: Did they patrol? What did they see?**
- Auto GPS-tracked patrol trails (start/end, mileage, path)
- Check-in at key nodes (bridges, cuts, blackspots) — ensures coverage, not a mere token check-in
- Issues reported in-app with photo + location + description + severity

**Problem 2: Who fixes it? Did they?**
- Workflow: supervisor finds → township accepts → works/contractors fix → supervisor verifies → close
- SLA per issue (e.g., pothole within 48 h)
- Auto-escalation (24 h → deputy; 48 h → director)
- Supervisor verifies; reject if unmet

**Problem 3: How to motivate?**
- Monthly auto performance report (mileage, findings, close-rate)
- Ranking published (top-10 / bottom-3)
- Linked to performance review

**After launch:** monthly patrol mileage <10 km → 45 km; findings +300%; close time 7 days → 2.5 days.

### 3.2 Smart Pavement Collection — "A Phone Does It"

Traditional survey needs a $400k+ survey vehicle — unrealistic for a $1.7M/yr division. Cloud County used a low-cost approach:

| Approach | Tool | Accuracy | Cost | Use |
|----------|------|----------|------|-----|
| Phone AI capture | Crew phone app; drive + capture; AI detects crack/pothole/rut | Crack width ±2 mm | Free (existing phones) | Full daily coverage |
| Drone bridge inspect | DJI M300 RTK + HD cam, auto flight, AI defect ID | mm-level | 2 units ~$0.4M | Bridges / hard-to-reach |
| Vehicle light kit | Patrol-car sensors (accelerometer + cam), monthly county/township | ~80% of pro | 3 kits ~$0.35M | County monthly monitor |

**Key data:** PCI coverage 12% → 100% (quarterly full sweep); defects found 500/yr → 2,300/yr; collection cost $2.8/km (pro vehicle) → $0.11/km (phone).

### 3.3 Public Reporting Widget — "All Residents Are Inspectors"

A mobile web app "CloudRoads":
- Residents report potholes, missing covers, ponding, slides (photo + location + 30 s)
- Auto-dispatched to the responsible unit
- Reporter notified on completion with before/after photos
- Points/incentive: monthly "best road guardian" recognition

**Operations:** 12,000 registered (8% of population); 320 valid reports/month; 78% accuracy (human-verified); vastly reduced blind spots.

---

## 4. The "AI Brain" for Maintenance Decisions

### 4.1 From "Gut Funding" to "Data-Driven"

Traditional allocation: "county roads more, township less, village none" — ignoring that many township roads carry more traffic and damage.

The AI decision-support system weighs:
1. Condition (PCI, RQI)
2. Traffic (weigh-in-motion + mobile-signal estimates)
3. Road class/function (to town / school / industrial park)
4. Historical spend (avoid chronic over/under-funding)
5. Cost model
6. Budget constraint ($1.7M/yr)

Output: annual plan (priority segments, recommended treatment, estimated cost) for approval.

**Validation:** at equal budget, the AI plan improved network PCI 28% more than manual; "same money, more road maintained." By 2023 county rural PCI "good/fair" rose 58% → 73% (above state avg 71%).

---

## 5. Outcomes

| Metric | Before (2020) | After (2023) | Change |
|--------|---------------|--------------|--------|
| PCI rating coverage | 12% | 100% | +88pp |
| PCI good/fair rate | 58% | 73% | +15pp |
| Annual patrol mileage | ~32,000 km | ~130,000 km | +306% |
| Issue close time | 7 days avg | 2.5 days avg | −64.3% |
| Maintenance cost ($/km/yr) | 144 | 115 | −20.1% |
| Preventive share | <5% | 35% | +30pp |
| Deficient-bridge rehab | 22% (5/23) | 87% (20/23) | +65pp |
| Public reports | 0 | 320/month | — |
| Fund-use efficiency | baseline | +28% | AI contribution |
| Rural crash rate | 3.8/Mio veh-km | 2.5/Mio veh-km | −34.2% |

---

## 6. Core Lessons

1. **"Low cost ≠ low quality":** the phone-AI approach cost <1/10 of a survey vehicle, yet higher-frequency, everyone-used collection delivered broader coverage. Rural digitization should drop "equipment worship" for lightweight, existing-resource solutions.
2. **The supervisor program needs tooling:** without app + data platform it becomes a wall poster. The app is both tool and closed-loop accountability.
3. **The public is the cheapest "sensor":** 12,000 registrations = 12,000 free sensing nodes reaching every corner. $0.55M widget replaced dozens of inspectors.
4. **AI decisions need local data accumulation:** year-1 model accuracy 65% → year-3 (3-yr history) 85%. Start year-1 with "AI recommend + human adjust," gradually raising AI weight.
5. **Training beats technology:** $0.7M on training was the best spent — 5 rounds across 18 townships, 120 supervisors/crew. "Built it, someone can and will use it well."
6. **Interface with state platform:** designed from the start to report to the state TAM platform, avoiding duplicate entry and enabling regional analytics.

---

*Case authored: April 2024 | Sources: county Public Works annual report, state TAM audit results*
