# Digital ROI Quick Calculator (Transportation)
## Digital ROI Calculator for Transportation Projects

---

## 1. Tool Overview

This tool provides a systematic ROI (return on investment) methodology for transportation digitalization projects, covering three layers: economic, social, and safety benefits. It includes 5 typical project calculation cases (city ITS platform / TMC, smart motorway, V2X corridor, smart transit, smart parking), with parameters re-based to globally representative market data.

### Use Cases
- Investment justification for transport digitalization projects
- Economic evaluation in feasibility studies
- Materials for funder / oversight review
- PPP Value-for-Money (VfM) assessment
- Project post-evaluation

### Methodology Framework
```
Total Benefit = Economic Benefit + Social Benefit + Safety Benefit
Economic Benefit = Travel-time saving + O&M cost reduction + Accident-cost reduction + Congestion-cost reduction
Social Benefit   = Employment pull + Accessibility uplift + Equity improvement + Regional development
Safety Benefit   = Value of lives saved + Value of injuries avoided + Property-loss avoided
```

> **Currency note:** All monetary figures in this tool are re-based to US$ (illustrative rate 1 RMB ≈ $0.14). Adjust to local currency / FX as needed.

---

## 2. Economic Benefit Calculation

### 2.1 Travel-Time Saving Benefit

#### Formula
```
B_time = Σ(ΔT_i × VOT_i × Q_i × 365)

where:
  ΔT_i = per-trip time saved for user type i (hours / trip)
  VOT_i = value of time for user type i ($ / hour)
  Q_i = average daily trips for user type i (trips / day)
  365 = annualization factor
```

#### Value of Time (VOT) Reference (global)
| User Type | Work VOT ($/hr) | Non-work VOT ($/hr) | Source |
|-----------|-----------------|---------------------|--------|
| Car driver | 18–36 | 10–20 | Transport authority |
| Car passenger | 14–28 | 9–16 | World Bank |
| Bus passenger | 10–22 | 6–12 | Local standards |
| Truck driver | 20–40 | – | Logistics association |
| Freight (value of time) | 35–70 / ton-equiv | – | Logistics association |
| Taxi / rideshare passenger | 16–30 | 10–18 | Industry report |
| Walk / cycle | 6–12 | 5–9 | WHO guidance |

**Note:** Use higher values for high-income metro areas, lower for smaller cities. Prefer local income data where available.

#### Typical Time Savings
| Digital Measure | Per-trip Saving | Note |
|-----------------|----------------|------|
| Adaptive signal control | 2–5 min / trip | 50+ intersections |
| MaaS route optimization | 3–8 min / trip | Multi-modal transfer |
| Real-time info publish | 1–3 min / trip | Avoid congestion |
| Smart parking guidance | 5–15 min / parking | Less search time |
| Free-flow tolling (ETC) | 0.5–1 min / pass | No stop at plaza |
| Transit signal priority | 1–3 min / trip | Transit riders |

### 2.2 O&M Cost Reduction

#### Formula
```
B_op = labor saving + maintenance saving + energy saving + management saving
```

#### Cost-Reduction Reference by Measure
| Digital Measure | Reduction | Main Source |
|-----------------|-----------|-------------|
| Automated inspection (UAV + AI) | 60–80% | Labor replacement, efficiency |
| Contactless tolling | 70–90% | Toll-collector replacement |
| Predictive maintenance | 20–30% | Fewer unplanned repairs |
| AI scheduling | 10–15% | Transit / metro optimization |
| Remote O&M | 30–50% | Fewer site visits |
| Paperless operations | 50–70% | Replaces paper workflow |
| Digital asset management | 15–25% | Longer asset life |

#### Labor Cost Saving
```
Labor saving = positions eliminated × avg annual salary × 1.4 (employer burden)

Reference (annual, all-in):
  Tier-1 city transport IT engineer: $35K–$63K
  Tier-2 city transport IT engineer: $21K–$35K
  Transport enforcement officer (all-in): $14K–$28K
  Toll collector (all-in): $8.4K–$14K
  Inspector (all-in): $11K–$21K
```

### 2.3 Accident-Cost Reduction

#### Formula
```
B_accident = Σ(N_i_before − N_i_after) × Cost_i

where:
  N_i = annual count of accident type i
  Cost_i = average comprehensive cost of accident type i
  i = fatal / serious injury / minor injury / property-only
```

#### Traffic Accident Cost Reference (global, USD)
| Type | Tier-1 | Tier-2 | Tier-3 | Note |
|------|--------|--------|--------|------|
| Fatality | $2.5M–3.5M | $1.7M–2.5M | $1.1M–1.7M | Compensation + social cost |
| Serious injury | $0.4M–0.7M | $0.25M–0.45M | $0.12M–0.3M | Medical + lost wages + disability |
| Minor injury | $40K–110K | $25K–70K | $15K–40K | Medical + short lost wages |
| Property only | $7K–28K | $4K–21K | $3K–14K | Vehicle + infrastructure |

**Sources:** National injury-compensation regulations, transport safety statistics, traffic-police records.

#### Accident Reduction by Measure
| Digital Measure | Expected Reduction | Main Type Avoided |
|-----------------|-------------------|-------------------|
| Adaptive signal control | 10–20% | Intersection collisions |
| Safety-risk warning | 15–25% | Speeding / fatigue-related |
| Video AI event detection | 15–20% | Secondary crashes |
| V2X safety warning | 30–50% | Collision / rear-end |
| Driving-behavior analysis | 15–25% | Commercial-vehicle crashes |
| Adverse-weather warning | 10–20% | Weather-related |

### 2.4 Congestion-Cost Reduction

#### Formula
```
B_congestion = ΔDelay × VOT_avg × Q_daily × 365

where:
  ΔDelay = per-person delay reduction (hours)
  VOT_avg = average value of time
  Q_daily = daily affected trips
```

#### Congestion Cost Reference (annual, per city)
| City Size | Annual Congestion Cost | Per-capita Annual | Annual Hours / Person |
|-----------|------------------------|-------------------|-----------------------|
| Megacity (>10M) | $280M–$700M | $350–700 | 150–250 |
| Large city (5–10M) | $70M–$280M | $210–420 | 80–150 |
| Big city (3–5M) | $28M–$112M | $140–280 | 50–100 |
| Mid-size city (1–3M) | $7M–$28M | $70–140 | 30–60 |

**Sources:** Major navigation providers' congestion reports (e.g., TomTom, INRIX), transport-authority statistics.

---

## 3. Social Benefit Quantification

### 3.1 Employment Pull
| Benefit | Method | Coefficient |
|--------|--------|-------------|
| Direct jobs | new positions × avg wage | D_jobs = N_new × Wage_avg |
| Indirect jobs | direct × multiplier | 1.5–2.0 (smart mobility) |
| Supply-chain pull | investment × chain factor | smart mobility: 1.8–2.5 |

### 3.2 Accessibility Value
```
B_accessibility = newly covered population × per-capita accessibility value

Reference:
  New urban transit coverage: $40–110 / person·yr
  New rural feeder coverage: $70–210 / person·yr
  Accessibility improvement (disability): $140–420 / person·yr (for PWD)
```

### 3.3 Equity Value
```
B_equity = Σ(B_low_income_group)
Indicators: lower transit cost for low-income groups; narrower urban-rural mobility gap;
            higher digital-mobility penetration among elderly.
```

### 3.4 Regional Development
```
B_regional = surrounding land-value uplift × contribution factor + commercial vitality uplift × quantification
```

---

## 4. Safety Benefit (VSL Method)

### 4.1 Value of Statistical Life (VSL) — Global Reference
| Method | VSL (USD / person) | Use |
|--------|--------------------|-----|
| Human-capital method | $1.1M–2.1M | Conservative |
| Willingness-to-pay | $3.5M–5.6M | Domestic standard |
| International benchmark | $4.9M–7.0M | Aligned with global norms |
| Transport-project recommended | $2.8M–4.9M | Suggested for transport projects |

### 4.2 Safety Benefit Formula
```
B_safety = VSL × N_death_prevented
         + Cost_injury_severe × N_severe_prevented
         + Cost_injury_slight × N_slight_prevented
         + Cost_damage × N_damage_prevented
```

### 4.3 Injury Cost Tiers
| Injury Level | Comprehensive Cost (USD) | Composition |
|--------------|--------------------------|-------------|
| Severe (disabling) | $0.7M–1.4M | Medical + rehab + lost wages + disability + care |
| Moderate | $140K–420K | Medical + short lost wages |
| Minor | $14K–70K | Outpatient + 1–2 weeks lost wages |

### 4.4 Property-Loss Reference
| Loss Type | Avg per Event (USD) | Note |
|-----------|---------------------|------|
| Vehicle (minor) | $280–700 | Vehicle only |
| Vehicle (moderate) | $700–2,800 | Repairable |
| Vehicle (severe) | $2.8K–14K+ | Major repair / total |
| Transport infrastructure | $420–2,100 | Barrier / signal, etc. |
| Cargo loss | case-by-case | At actual value |

---

## 5. Input Parameter Reference

### 5.1 Key Economic Parameters
| Parameter | Recommended | Range | Note |
|-----------|-------------|-------|------|
| Social discount rate | 8% | 6%–10% | Economic evaluation |
| Financial discount rate | 5%–7% | per financing | Financial evaluation |
| Evaluation period | 10–15 yr | 5–20 yr | Transport usually 10 yr |
| Salvage rate | 5% | 0%–10% | Infrastructure |
| VAT | 6% (services) / 13% (goods) | local rate | Software services 6% — adjust to jurisdiction |
| Corporate income tax | 25% (15% high-tech) | 15%–25% | Adjust to jurisdiction |

### 5.2 Shadow-Price Conversion Factors
| Item | Financial→Economic Factor | Note |
|------|---------------------------|------|
| Unskilled labor | 0.5–0.8 | True social labor cost |
| Skilled labor | 0.8–1.0 | Near market |
| Land | by city / location | Use alternative cost |
| Cement / steel | 0.9–1.1 | Key materials |
| Imported equipment | 1.05–1.15 | Duties etc. |
| Local equipment | 0.9–1.0 | Near market |

### 5.3 IT Equipment Depreciation
| Equipment / System | Life | Salvage |
|--------------------|------|---------|
| Server / storage | 5 yr | 5% |
| Network gear | 5 yr | 5% |
| Cameras | 5–8 yr | 5% |
| IoT sensors | 5–8 yr | 3% |
| Signal / edge compute | 8–10 yr | 5% |
| Software | 3–5 yr | 0% |
| Fiber cable | 15–20 yr | 5% |
| Civil works (poles / cabinets) | 20 yr+ | 5–10% |

---

## 6. Sensitivity Analysis Engine

### 6.1 Framework
```
Uncertain factors (one variable at a time, others fixed):
  1. Capex change: ±10%, ±20%
  2. O&M cost change: ±10%, ±20%
  3. Benefit change: ±10%, ±20%
  4. Discount rate: 6% / 8% / 10%
  5. Schedule slip (6 / 12 months delay)
  6. Worst combined (capex +20% + benefit −20%)
```

### 6.2 Three-Scenario Template
| Metric | Pessimistic | Base | Optimistic | Note |
|--------|-------------|------|------------|------|
| Capex | +20% | Base | −10% | |
| Annual O&M | +15% | Base | −10% | |
| Annual benefit | −20% | Base | +15% | |
| Discount rate | 10% | 8% | 6% | |
| ENPV | ____ | ____ | ____ | |
| EIRR | __% | __% | __% | |
| B/C | ____ | ____ | ____ | |
| Payback | ____ yr | ____ yr | ____ yr | |

### 6.3 Sensitivity Ranking
| Factor | Change | ENPV Δ% | EIRR Δ | Sensitivity | Rank |
|--------|--------|---------|--------|-------------|------|
| Benefit | ±20% | ±__% | ±__% | __ | 1 |
| Investment | ±20% | ±__% | ±__% | __ | 2 |
| O&M | ±20% | ±__% | ±__% | __ | 3 |
| Discount rate | ±2% | ±__% | ±__% | __ | 4 |

---

## 7. Break-Even Analysis

### 7.1 Benefit Break-Even
```
Benefit level where ENPV = 0
Break-even benefit = base benefit × (1 − BEP%)
BEP% = ENPV / PV_benefit   (PV_benefit = discounted benefit sum)
```

### 7.2 Investment Break-Even
```
Max investment where ENPV = 0
Break-even investment = base investment × (1 + BEP_invest%)
BEP_invest% = ENPV / PV_investment
```

### 7.3 Break-Even Reference
| Project Type | Typical BEP (benefit drop) | Comment |
|--------------|----------------------------|---------|
| Signal AI optimization | 40–60% | High margin |
| ITS platform / TMC | 20–35% | Medium margin |
| Smart motorway | 15–30% | Lower margin; caution |
| V2X cooperative-ITS | −5% to 10% | Low margin; high risk |
| Smart parking | 30–50% | High margin (commercial) |
| MaaS platform | 10–25% | Lower margin |

---

## 8. 5-Year Cash-Flow Template

### 8.1 Financial Cash Flow (USD)
```
============================================================
             5-Year Project Financial Cash-Flow Forecast
============================================================

Project: ____________________   Base date: ______ (mo/yr)

| Item                  | Y1 | Y2 | Y3 | Y4 | Y5 | Total |
|-----------------------|----|----|----|----|----|-------|
| A. Cash Inflow        |    |    |    |    |    |       |
| 1.1 Direct revenue    |    |    |    |    |    |       |
| 1.2 Cost savings      |    |    |    |    |    |       |
| 1.3 Public grant / funding | |    |    |    |    |       |
| 1.4 Other revenue     |    |    |    |    |    |       |
| Inflow subtotal       |    |    |    |    |    |       |
|                       |    |    |    |    |    |       |
| B. Cash Outflow       |    |    |    |    |    |       |
| 2.1 Capex             |    |    |    |    |    |       |
| 2.2 O&M cost          |    |    |    |    |    |       |
| 2.3 Personnel         |    |    |    |    |    |       |
| 2.4 Tax              |    |    |    |    |    |       |
| 2.5 Other             |    |    |    |    |    |       |
| Outflow subtotal      |    |    |    |    |    |       |
|                       |    |    |    |    |    |       |
| C. Net cash flow      |    |    |    |    |    |       |
| Cumulative net        |    |    |    |    |    |       |
| Discounted net (5%)   |    |    |    |    |    |       |
| Cumulative discounted |    |    |    |    |    |       |
```

### 8.2 Economic Indicator Summary
| Indicator | Value | Criterion | Conclusion |
|-----------|-------|-----------|------------|
| ENPV (USD) | ____ | > 0 acceptable | ☐ Accept ☐ Reject |
| EIRR (%) | ____% | > 8% acceptable | ☐ Accept ☐ Reject |
| B/C | ____ | > 1.0 acceptable | ☐ Accept ☐ Reject |
| Payback (yr) | ____ | < evaluation period | ☐ Accept ☐ Reject |
| FNPV (USD) | ____ | > 0 | ☐ Feasible ☐ Infeasible |
| FIRR (%) | ____% | > financing cost | ☐ Feasible ☐ Infeasible |

---

## 9. PPP Value-for-Money (VfM) Analysis

### 9.1 Qualitative VfM
| Indicator | Weight | Score (1–5) | Weighted | Note |
|-----------|--------|-------------|----------|------|
| Whole-life integration | 10% | | | |
| Risk identification & allocation | 15% | | | |
| Performance & innovation | 10% | | | |
| Potential competition | 10% | | | |
| Public-agency capacity | 10% | | | |
| Bankability | 15% | | | |
| Project scale | 5% | | | |
| Lifecycle-cost accuracy | 5% | | | |
| Legal / regulatory environment | 10% | | | |
| Asset utilization | 10% | | | |
| **Qualitative total** | **100%** | | **____** | ≥ 60 to pass |

### 9.2 Quantitative VfM (PSC method)
```
VfM = PSC_NPV − PPP_NPV

where:
  PSC_NPV = net present value of public-sector traditional procurement lifecycle cost
  PPP_NPV = net present value of public-sector cost under PPP

VfM > 0 → PPP is value for money
VfM < 0 → traditional is better
```

| Item | PSC | PPP | VfM | Conclusion |
|------|-----|-----|-----|------------|
| Base PSC | ____ | ____ | | |
| Risk-adjusted | ____ | ____ | | |
| Competition-neutral adj. | ____ | ____ | | |
| **Final** | **____** | **____** | **____** | ☐ Pass ☐ Fail |

---

## 10. Typical Project Cases

### Case 1: City ITS Platform / TMC
```
============================================================
   City ITS Platform (TMC) ROI Example
============================================================

[Overview]
  City: mid-size (pop. 5M)
  Scope: big-data platform + AI hub + digital twin + 50 scenarios
  Capex: $7.0M
  Annual O&M: $1.1M (cloud + O&M + labor)
  Period: 10 yr   Discount: 8%

[Benefits]
1. Travel-time saving:
   Affected trips: 1.0M / day
   Per-trip saving: 2 min (0.033 h)
   VOT: $4.2 / hr
   Annual = 1.0M × 0.033 × 4.2 × 365 = $50.6M
   Digital attribution: 0.3 → $15.2M/yr

2. O&M reduction:
   Labor: 50 monitoring staff × $16.8K = $0.84M/yr
   Maintenance: predictive maintenance −30% faults = $0.28M/yr
   Annual O&M saving = $1.12M/yr

3. Accident-cost reduction:
   Crashes: 5,000/yr → 4,000/yr
   Avg crash cost: $2.8K
   Annual = 1,000 × $2.8K = $2.8M; attribution 0.4 → $1.12M/yr

4. Congestion reduction:
   Current annual congestion cost: $560M
   Reduction: 8%; attribution 0.3
   Annual = $560M × 8% × 30% = $13.4M

[Benefit Summary] (USD/yr)
| Category        | Annual ($M) |
|-----------------|-------------|
| Time saving     | 15.2        |
| O&M saving      | 1.1         |
| Accident reduce | 1.1         |
| Congestion      | 13.4        |
| Total           | 30.8        |

[Indicators]
  Investment = $7.0M capex + $1.1M/yr O&M
  Net annual benefit = $30.8M − $1.1M = $29.7M
  ENPV (10 yr, 8%) ≈ $128.8M
  EIRR ≈ 420%   B/C ≈ 18.4   Payback < 1 yr
[Sensitivity] Benefit −50%: ENPV still > 0. Capex +50% & benefit −30%: ENPV still > 0.
Conclusion: Excellent economics; very high margin.
============================================================
```

### Case 2: Smart Motorway
```
============================================================
   Smart Motorway ROI Example
============================================================
[Overview]
  Section: dual 6-lane, 100 km
  Scope: holographic sensing + edge + active management + V2X + digital twin
  Capex: $11.2M   Annual O&M: $1.7M   Period: 15 yr

[Benefits]
1. Throughput:
   AADT: 50K veh/day
   Avg speed +10 km/h (80→90)
   VOT: $7.0/hr
   Annual = 50K × (100/80 − 100/90) × 7.0 × 365 ≈ $8.9M

2. Accidents:
   200/yr → 140/yr; avg cost $4.2K → $0.25M/yr

3. O&M saving:
   Auto-inspection: $0.28M/yr; predictive maint.: $0.42M/yr; energy: $0.21M/yr → $0.91M/yr

4. All-weather operation:
   Closure days: 15/yr → 5/yr; loss $0.42M/day
   Annual = 10 × $0.42M = $4.2M; attribution 0.6 → $2.5M/yr

[Benefit Summary] (USD/yr)
| Category     | Annual ($M) |
|--------------|-------------|
| Throughput   | 8.9         |
| Accidents    | 0.25        |
| O&M saving   | 0.91        |
| Closure cut  | 2.5         |
| Total        | 12.6        |

[Indicators] ENPV (15 yr, 8%) ≈ $59M; EIRR ≈ 112%; B/C ≈ 5.3; Payback ≈ 1.5 yr
============================================================
```

### Case 3: V2X Cooperative-ITS Corridor
```
============================================================
   V2X Cooperative-ITS Corridor ROI Example
============================================================
[Overview]
  Corridor: 50 km urban arterial (100 intersections)
  Scope: RSU + edge + sensing + C-V2X platform
  Capex: $35M   Annual O&M: $7M   Period: 10 yr

[Key Assumptions]
  V2X penetration: 5% (Y1) → 30% (Y5)
  Daily volume: 500K trips
  Scenarios: green-wave, safety warning, info push

[Year-5 Benefits]
  1. Throughput: 500K × 30% × 3 min × $4.9/hr × 365 ≈ $13.4M
  2. Accidents: 1,000 avoided/yr × $2.1K = $2.1M
  3. Emissions: 5,000 t CO2/yr × $7/t = $35K (low carbon price)

  Year-5 annual benefit ≈ $15.5M
  10-yr cumulative grows with penetration.

[Indicators] ENPV (10 yr, 8%) ≈ $21M; EIRR ≈ 14%; B/C ≈ 1.6; Payback ≈ 6 yr
[Sensitivity] Penetration stalls at 15%: EIRR drops to 6%, ENPV negative.
Conclusion: Highly sensitive to V2X penetration; needs OEM fitment push.
============================================================
```

### Case 4: Smart Transit
```
============================================================
   Smart Transit ROI Example
============================================================
[Overview]
  Fleet: 1,000 buses, 50 routes
  Scope: smart dispatch + OD analytics + AI scheduling + real-time info
  Capex: $2.8M   Annual O&M: $0.56M   Period: 10 yr

[Benefits]
1. O&M reduction:
   Fleet cut 1,000 → 920 (−80 buses); $21K/bus/yr → $1.68M/yr
   Staff optimization (5 dispatchers × $14K) → $0.07M/yr
   Annual O&M saving = $1.75M/yr

2. Passenger time saving:
   Daily ridership: 500K; wait −2 min; VOT $2.8/hr
   Annual = 500K × (2/60) × 2.8 × 365 ≈ $8.5M; attribution 0.5 → $4.25M/yr

3. Ridership growth (service quality):
   +5% riders; fare $0.28; annual = 500K × 365 × 5% × $0.28 ≈ $2.56M; attribution 0.4 → $1.02M/yr

[Benefit Summary] (USD/yr)
| Category        | Annual ($M) |
|-----------------|-------------|
| O&M reduction   | 1.75        |
| Passenger time  | 4.25        |
| Ridership gain  | 1.02        |
| Total           | 7.02        |

[Indicators] ENPV (10 yr, 8%) ≈ $30.8M; EIRR ≈ 250%; B/C ≈ 11.5; Payback < 1 yr
============================================================
```

### Case 5: Smart Parking
```
============================================================
   City Smart Parking ROI Example
============================================================
[Overview]
  Citywide platform: 500 lots / 100K spaces
  Scope: parking platform + guidance signs + space detection + app
  Capex: $4.2M   Annual O&M: $0.84M   Period: 10 yr

[Benefits]
1. Search-time saving:
   Daily parking: 200K; search −5 min; VOT $4.2/hr
   Annual = 200K × (5/60) × 4.2 × 365 ≈ $25.6M; attribution 0.5 → $12.8M/yr

2. Utilization uplift:
   55% → 70%; revenue = 100K × 15% × 365 × $1.4 avg × 50% platform commission ≈ $3.8M/yr

3. Labor saving:
   1,000 lots × 1 person × $11K = $11M/yr; attribution 0.5 → $5.5M/yr

4. Congestion reduction:
   5,000 fewer circling trips/day × 1 km × 365 → ≈ $0.7M/yr

[Benefit Summary] (USD/yr)
| Category       | Annual ($M) |
|----------------|-------------|
| Time saving    | 12.8        |
| Utilization    | 3.8         |
| Labor saving   | 5.5         |
| Congestion     | 0.7         |
| Total          | 22.8        |

[Indicators] ENPV (10 yr, 8%) ≈ $105M; EIRR ≈ 545%; B/C ≈ 25.2; Payback < 1 yr
============================================================
```

---

## 11. ROI Calculation Worksheet
```
============================================================================
                  Project ROI Calculation Worksheet
============================================================================

Project: ____________________   Date: ____________________

==================================================================
PART A: Base Parameters
==================================================================
Discount rate: ____%    Evaluation period: ____ yr
Total investment: $ ________
Annual O&M: $ ________
Construction period: ____ yr

==================================================================
PART B: Benefit Breakdown
==================================================================
B1. Travel-time saving
   Affected users: ________ trips/day
   Per-trip saving: ________ min
   VOT: $ ________ /hr
   Attribution: ____%
   Annual B1 = $ ________

B2. O&M reduction
   Labor: ________ people × $ ________/yr = $ ________
   Maintenance: $ ________
   Energy: $ ________
   Annual B2 = $ ________

B3. Accident-cost reduction
   Crashes avoided: ________
   Avg crash cost: $ ________
   Attribution: ____%
   Annual B3 = $ ________

B4. Congestion reduction
   Base annual congestion cost: $ ________
   Reduction: ____%
   Attribution: ____%
   Annual B4 = $ ________

B5. Other
   Description: ____________________
   Annual B5 = $ ________

Total annual benefit = B1+B2+B3+B4+B5 = $ ________

==================================================================
PART C: Economic Evaluation
==================================================================
Net annual benefit = total − O&M = $ ________
ENPV = $ ________
EIRR = ____%
B/C = ____
Payback = ____ yr

==================================================================
PART D: Sensitivity
==================================================================
Pessimistic (BENPV): $ ________
Base (ENPV): $ ________
Optimistic (OENPV): $ ________

Conclusion: ☐ Invest   ☐ Invest with conditions   ☐ Do not invest

==================================================================
Prepared by: ____________   Reviewed by: ____________
============================================================================
```

---

## 12. Usage Instructions
1. **Define scope**: Clarify the digital project's boundary and contents.
2. **Collect parameters**: Use Section 5 reference tables.
3. **Compute economic benefits**: Section 2, item by item.
4. **Add social benefits**: Section 3.
5. **Assess safety**: Section 4 VSL method.
6. **Aggregate & evaluate**: Use Section 8 cash-flow template for indicators.
7. **Sensitivity**: Section 6 three-scenario analysis.
8. **PPP projects**: Also complete Section 9 VfM.
9. **Benchmark**: Validate against Section 10 peer cases.
10. **Report**: Follow your organization's standard economic-evaluation report format.
