# Core Methodology Library

> This document systematically presents the 10 core methodologies for transport digital and AI transformation. Each methodology includes a complete framework, operating procedure, scoring standard, worked example, and application guide. Methodology-driven delivery is the core differentiator of this Skill versus generic consulting.

---

## Table of Contents

1. [T-DMM Transportation Digital Maturity Model](#i-t-dmm-transportation-digital-maturity-model)
2. [RICE++ Six-Dimension Transport-AI Prioritization Scorecard](#ii-rice-six-dimension-transport-ai-prioritization-scorecard)
3. [Seven-Dimension Vendor Selection Matrix](#iii-seven-dimension-vendor-selection-matrix)
4. [Triple-Bottom-Line ROI Investment Model](#iv-triple-bottom-line-roi-investment-model)
5. [Vehicle–Infrastructure–Cloud (VIC) Five-Level Maturity Model](#v-vehicleinfrastructurecloud-vic-five-level-maturity-model)
6. [Four-Horizontal, Three-Vertical Cybersecurity Architecture](#vi-four-horizontal-three-vertical-cybersecurity-architecture)
7. [Six-Layer Data Governance Framework](#vii-six-layer-data-governance-framework)
8. [ADKAR Change Management](#viii-adkar-change-management)
9. [Ten-Phase Large-Project Lifecycle](#ix-ten-phase-large-project-lifecycle)
10. [Twelve-Country ITS Benchmark Framework](#x-twelve-country-its-benchmark-framework)

---

## I. T-DMM Transportation Digital Maturity Model

### 1.1 Model Overview

T-DMM (Transportation Digital Maturity Model) is a five-dimension digital-maturity assessment framework for transport organizations.

**Five dimensions:**

| Dimension | Code | Weight | Core Question | Sub-dimensions |
|----------|:----:|:------:|--------------|:--------------:|
| Infrastructure | D1 | 25% | Are sensing / communications / compute foundations complete? | 5 |
| Data intelligence | D2 | 25% | Are data collection / governance / analytics / AI strong? | 6 |
| Business application | D3 | 25% | How deep and broad is digitalization across core scenarios? | 5 |
| Organization & governance | D4 | 15% | Are org, talent, process, and funding in place? | 5 |
| Security assurance | D5 | 10% | Are cyber, data, and functional safety assured? | 5 |

### 1.2 Five Maturity Levels

| Level | Name | Score | Core Trait | Typical Profile |
|:----:|------|:----:|-----------|-----------------|
| **L1** | Initial | 0–20 | Fragmented IT, manual/experience-driven; no unified platform; data in Excel/paper | Early-stage local transport agency |
| **L2** | Standardized | 21–40 | Key businesses have standalone systems; data digitized; systems not interconnected | Most city-level transport agencies |
| **L3** | Integrated | 41–60 | Unified data platform / TOC built; core systems connected; point AI use | Mid-size city / capital |
| **L4** | Intelligent | 61–80 | Digital twin + broad AI; data flywheel; cross-agency data sharing | Singapore / Tokyo / Amsterdam class |
| **L5** | Leading | 81–100 | AI-native; transport LLM; data-asset operations; exports models | Global leader / national |

### 1.3 D1 Infrastructure Assessment (25%)

| Sub-dimension | Weight | L1(5) | L2(15) | L3(35) | L4(55) | L5(90) |
|--------------|:------:|:----:|:----:|:----:|:----:|:----:|
| Sensing coverage | 30% | <15% key points | 15–30% | 30–50% | 50–75% | >75% multi-source fused |
| Signal connectivity | 20% | <20% | 20–50% | 50–80% | 80–95% | >95% + adaptive |
| Communications | 20% | No dedicated net | Fiber backbone | +4G/WiFi | +5G/MEC | +5G-A / 6G trial |
| Cloud capability | 15% | None / rented | Virtualized | Private cloud | Hybrid + containers | Cloud-native + AI-native |
| Edge devices | 15% | Legacy | Partly smart | 50% digital | 80% smart terminals | IoT full + OTA |

**D1 formula:** D1 total = Σ(sub-score × sub-weight), sub-score interpolated within the level band.

**Sample questions (from 50+):**
| # | Question | Options | Score |
|---|---------|---------|:--:|
| D1.1 | Video coverage at key intersections / segments? | <15% / 15–30% / 30–50% / 50–75% / >75% | — |
| D1.2 | Deployed non-video sensors (radar / LiDAR)? | None / pilot / partial / wide | — |
| D1.3 | Signal connectivity (remote monitor + config)? | <20% / 20–50% / 50–80% / 80–95% / >95% | — |
| D1.4 | MEC edge nodes deployed? | None / planning / pilot / partial / wide | — |
| D1.5 | Cloud model? | None / rented / virtualized / private / hybrid / cloud-native | — |

### 1.4 D2 Data Intelligence (25%)

| Sub-dimension | Weight | L1 | L2 | L3 | L4 | L5 |
|--------------|:------:|:--:|:--:|:--:|:--:|:--:|
| Data aggregation | 20% | <15% | 15–30% | 30–55% | 55–80% | >80% |
| Data quality pass | 20% | <50% | 50–65% | 65–80% | 80–95% | >95% |
| AI model count | 15% | 0 | 1–2 pilot | 3–8 | 15+ | 40+ |
| Data-driven decisions | 15% | <8% | 8–20% | 20–45% | 45–70% | >70% |
| Data standard uniformity | 15% | None | Partial | Core unified | All-domain | Industry benchmark |
| Data assetization | 15% | None | Catalog | Governance | Asset on balance sheet | Data product trading |

### 1.5 D3 Business Application (25%)

| Sub-dimension | Weight | L1 | L2 | L3 | L4 | L5 |
|--------------|:------:|:--:|:--:|:--:|:--:|:--:|
| Core scenario coverage | 30% | <15% | 15–30% | 30–55% | 55–80% | >80% |
| Process automation | 25% | <8% | 8–20% | 20–45% | 45–70% | >70% |
| User penetration | 20% | <15% | 15–30% | 30–55% | 55–75% | >75% |
| Cross-agency coordination | 15% | None | 2–3 depts | 5+ depts | 10+ depts | All-domain |
| Mobility level | 10% | No app | Basic app | Core mobile | All mobile | Super-app |

### 1.6 D4 Organization & Governance (15%)

| Sub-dimension | L1 | L2 | L3 | L4 | L5 |
|--------------|----|----|----|----|----|
| Digital talent share | <1% | 1–3% | 3–6% | 6–15% | >15% |
| IT budget / total spend | <0.5% | 0.5–1.5% | 1.5–3% | 3–7% | >7% |
| CIO / CDO | None | Part-time | Dedicated CIO | CIO+CDO | CAIO+CDO+CIO |
| Process standardization | <15% | 15–30% | 30–55% | 55–80% | >80% |
| Innovation mechanism | None | Occasional | Fixed innovation budget | Innovation lab | External ecosystem |

### 1.7 D5 Security Assurance (10%)

| Sub-dimension | L1 | L2 | L3 | L4 | L5 |
|--------------|----|----|----|----|----|
| Compliance rate | <20% | 20–45% | 45–70% | 70–95% | 100% + CIP |
| Major annual incidents | >5 | 3–5 | 1–2 | 0–1 | 0 |
| SOC / SIEM | None | Basic logs | SOC build | SOC+SIEM | AI+SOAR |
| Drill frequency | None | Annual | Semi-annual | Quarterly | Monthly + red/blue |
| Data security | None | Basic | Classification | Full-lifecycle | Privacy compute + zero-trust |

### 1.8 Composite Scoring and Diagnosis

**Composite:** T-DMM total = D1×0.25 + D2×0.25 + D3×0.25 + D4×0.15 + D5×0.10

**Diagnosis rules:**

| Condition | Conclusion | Priority 1 | Priority 2 | Priority 3 |
|----------|-----------|:----------:|:----------:|:----------:|
| Total <25 | L1–L2 overall | Sensing gaps | Data digitization | Org assurance |
| D1 low (<30) + D3 high (>50) | Business on fragile base | Infrastructure | Reliability | — |
| D2 low (<30) + D1 high (>50) | Data but no intelligence | Data governance | AI pilot | Data standards |
| D4 low (<25) | Tech but no org | CIO role | Budget | Talent |
| D5 low (<20) | Security time-bomb | Risk classification | CIP designation | SOC build |
| Total >65, D2 <50 | L4 base, weak AI | AI platform | LLM intro | Deep governance |
| Total >80 | L4–L5 leader | AI-native explore | Data assetization | Model export |

### 1.9 Gap Analysis and Roadmap Derivation

**Gap matrix:** Current → Target → Gap → Action → Resource → Time.
Steps: (1) set target level; (2) compute per-dimension gaps; (3) rank by impact + feasibility; (4) design 1/3/5-yr milestones; (5) match projects + budget + owner.

**Roadmap algorithm:**
1. Fill D5 security gaps first (safety floor).
2. Fill D1 sensing-coverage gaps (data is foundational).
3. Then D2 data gaps (data → AI path).
4. Then D3 business (needs data + AI).
5. In parallel D4 org (ongoing assurance).

---

## II. RICE++ Six-Dimension Transport-AI Prioritization Scorecard

### 2.1 Dimensions and Scale

| Dimension | Code | Definition | 1–5 Meaning |
|----------|:----:|-----------|-------------|
| Reach | R | Users / business scope covered | 1=few; 3=core users; 5=whole domain |
| Impact | I | Effect on core KPI | 1=negligible; 3=significant; 5=transformative |
| Confidence | C | Delivery confidence | 1=concept; 3=proven case; 5=mature/repeatable |
| Effort | E | Difficulty / cost (inverse) | 5=easiest/cheapest; 3=medium; 1=hardest/costliest |
| Safety | S | Positive traffic-safety effect | 1=none; 3=medium; 5=clear fatality/injury reduction |
| Policy | P | Regulatory urgency / compliance | 1=none; 3=encouraged; 5=mandatory |

### 2.2 Formula

```
RICE++ = (R × I × C) / E + S + P
```
- `(R×I×C)/E` is base RICE (value/cost efficiency).
- `+S+P` adds transport-specific safety and policy bonuses.

### 2.3 Rationale

- Transport ROI is complex (indirect benefits: congestion → time value → economy); full ROI takes months. RICE++ scores in 1–2 hours, fit for screening.
- Safety (S) and Policy (P) are unique to large transport programs; classic commercial ROI omits them.
- Confidence (C) prevents over-optimism on immature tech.

### 2.4 25-Scenario RICE++ Example

| Scenario | R | I | C | E | S | P | Base | +S+P | Total | Priority |
|---------|:-:|:-:|:-:|:-:|:-:|:-:|:----:|:----:|:----:|:-------:|
| AI incident detection | 5 | 5 | 5 | 4 | 5 | 4 | 15.6 | 9 | **24.6** | P0 |
| AI signal optimization | 5 | 5 | 4 | 3 | 4 | 5 | 16.7 | 9 | **25.7** | P0 |
| AI safety-risk forecast | 4 | 5 | 4 | 3 | 5 | 4 | 13.3 | 9 | **22.3** | P1 |
| AI smart assistant | 5 | 3 | 5 | 5 | 1 | 3 | 15.0 | 4 | **19.0** | P1 |
| Transport LLM | 5 | 4 | 3 | 2 | 2 | 4 | 15.0 | 6 | **21.0** | P1 |
| AI maintenance decision | 4 | 4 | 4 | 3 | 3 | 3 | 10.7 | 6 | **16.7** | P2 |
| AV L4 | 4 | 5 | 3 | 1 | 5 | 5 | 60.0 | 10 | **70.0** | Long-term |
| AI low-altitude UTM | 3 | 4 | 2 | 2 | 4 | 5 | 12.0 | 9 | **21.0** | P2 |
| Digital-twin AI | 3 | 3 | 3 | 2 | 2 | 3 | 6.8 | 5 | **11.8** | P3 |

### 2.5 Sensitivity Analysis

RICE++ is most sensitive to C (product term). Guidance:
- C<3 → no large investment; run PoC first.
- E inverse scoring is volatile → average independent expert scores.
- S+P cap (+10) systematically favors safety/policy-driven programs — by design.

---

## III. Seven-Dimension Vendor Selection Matrix

### 3.1 Framework

| Dimension | Weight | Core Question | Evidence |
|----------|:------:|--------------|---------|
| F — Functionality | 25% | Meets needs? Gaps? | Requirements vs demo + PoC |
| T — Technology | 20% | Leading architecture? AI? openness? | White paper + architecture review |
| E — Ecosystem | 15% | Integration difficulty? standards? | Interface docs + integration test |
| S — Service & support | 15% | Local service? response? docs? | Client follow-up + SLA review |
| X — Sovereignty & Standards | 10% | Local-content / standards compliance? | Certification + supply-chain bill |
| R — Reliability & security | 10% | Stability? vulnerabilities? MTBF? | Security + reliability test |
| C — Commercial value | 5% | Price? TCO? license model? | Quotes + TCO |

### 3.2 Weight Calibration by Project Type

| Type | F | T | E | S | X | R | C | Reason |
|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|-------|
| CIP project | 20 | 15 | 15 | 10 | 20 | 15 | 5 | Security + sovereignty first |
| City platform | 25 | 20 | 20 | 10 | 10 | 10 | 5 | Function + tech + ecosystem |
| Signal equipment | 20 | 20 | 10 | 20 | 15 | 10 | 5 | Reliability + service |
| SaaS purchase | 25 | 15 | 15 | 15 | 5 | 5 | 20 | Commercial weight up |
| Research cooperation | 15 | 30 | 20 | 5 | 5 | 5 | 20 | Tech weight up |

### 3.3 PoC Design Methodology

**Goal:** validate core needs at minimal cost.
**Standard flow (4–8 weeks):** Week1 plan → W2–3 execute → W4 assess.
**Scenario selection:** expose weakness, not happy path; include normal (60%) + boundary (25%) + anomaly (15%); transport-specific: peak, low-light night, adverse weather, device failure.
**Metrics:**

| Class | Quantitative | Qualitative |
|-------|-------------|-----------|
| Function | Requirement coverage %, mandatory pass % | UX, config flexibility |
| Performance | Latency (P50/P95/P99), throughput, accuracy | — |
| Reliability | 168h no-error, recovery time | Exception handling, logs |
| Integration | API success %, import success % | Openness, docs |
| Security | Vuln-scan result, pentest pass % | Access control, encryption |

### 3.4 TCO Model

**TCO = CAPEX + 5-yr OPEX + exit cost + migration cost**
| Item | Note | Method |
|------|------|--------|
| CAPEX | HW + SW license + integration | Quote + effort estimate |
| 5-yr OPEX | Maintenance + upgrade + ops + cloud | Annual ×5 + 5–10%/yr growth |
| Exit cost | Replace / data migration / disruption | Migration hours × rate + loss |
| Lock-in premium | Post-lock-in price uplift | Delta vs alternative |

---

## IV. Triple-Bottom-Line ROI Investment Model

### 4.1 Framework

Transport value cannot be measured by economic ROI alone — evaluate economic, social, and safety benefits together.

| Benefit | Definition | Monetization | Why public sector cares |
|--------|-----------|:-------------:|------------------------|
| **Economic** | Direct financial gain + cost saving | High (precise) | Required for investment review |
| **Social** | Public / environment / city impact | Medium (shadow price) | Performance + livability + decarbonization |
| **Safety** | Fewer crashes / injuries / loss | Medium (VSL method) | Safety is the floor + duty |

### 4.2 Economic Benefit

**Total economic = Σ(direct_i) + Σ(indirect_j) − Σ(cost_k)**

| Source | Formula | Key Param |
|--------|---------|-----------|
| Congestion reduction | Δdelay(s/veh) × volume × time-value($/s) × 365 | Time value $4–9/h |
| Fuel saving | Δstops × fuel/stop × volume × fuel price × 365 | ~0.02–0.05 L/stop |
| Emission reduction | ΔCO2(t) × carbon price($/t) | $8–14/t (2025) |
| Ops efficiency | Δlabor hours × cost + Δutil × asset value | — |
| Maintenance saving | Original × reduction% | Preventive −15–30% |
| Toll revenue | New toll / evasion recovery / dynamic pricing | — |

### 4.3 Social Benefit (Shadow Pricing)

| Benefit | Method | Reference |
|--------|-------|---------|
| Travel-time saving | GDP/hour worked | $4–9/h |
| Emission reduction | Carbon market + social cost | $8–40/t CO2 |
| Air-pollution reduction | Health cost + mortality | NOx ~$10k/t, PM2.5 ~$50k/t |
| Transit improvement | Time value + equity | Time-value method |
| Employment | Direct × income + multiplier | Multiplier 1.5–2.5 |

### 4.4 Safety Benefit (VSL Method)

**VSL (value of a statistical life):** high-income economies ~$5–12M (scaled by income for other markets).
**Injury:** severity × VSL × coefficient (minor 0.005, serious 0.1–0.3).
**Property-only:** avg property loss × count.

```
Annual safety benefit = VSL × Δfatalities + VSL × Σ(coef_j × Δinjuries_j) + Δproperty loss
```

### 4.5 ROI Template

**Example: 50-intersection AI signal project (USD, annual):**

| Item | Amount ($k/yr) |
|------|:--------------:|
| **Investment** | |
| Hardware (one-off, 5-yr amortized) | 280 |
| Software + integration (amortized) | 220 |
| Annual O&M + optimization | 250 |
| **Total annual investment** | **750** |
| **Economic benefit** | |
| Congestion-time saving | 1,340 |
| Fuel saving | 310 |
| Carbon-trading revenue | 63 |
| **Subtotal economic** | **1,713** |
| **Social benefit** | |
| Experience (time value) | 670 |
| Environment (health) | 170 |
| **Subtotal social** | **840** |
| **Safety benefit** | |
| Crash reduction (−18%) | 390 |
| Secondary-crash prevention | 130 |
| **Subtotal safety** | **520** |
| **Total benefit** | **3,073** |
| **Benefit–cost ratio** | **4.10 : 1** |
| **Payback (economic only)** | **~2.0 yr** |

### 4.6 Sensitivity Analysis

±20% on key assumptions:

| Param | Base | −20% ROI | +20% ROI | Impact |
|------|:----:|:--------:|:--------:|:----:|
| Volume | 100% | 2.8:1 | 5.2:1 | High |
| Time value | $6.5/h | 3.3:1 | 4.8:1 | Medium |
| Crash-reduction | 18% | 3.7:1 | 4.5:1 | Medium |
| Hardware cost | 100% | 5.2:1 | 3.5:1 | Medium |
| Carbon price | $11/t | 3.9:1 | 4.2:1 | Low |

---

## V. Vehicle–Infrastructure–Cloud (VIC) Five-Level Maturity Model

> International terms: Cooperative Intelligent Transportation System (C-ITS) / V2X / Vehicle-Infrastructure-Cloud integration. Equivalent to the localized "车路云一体化" concept.

### 5.1 Five Levels

| Level | Name | Typical Scale | Core Capability | Typical Investment (per level) |
|:----:|------|--------------|----------------|:------------------------------:|
| L1 | Segment | 3–5 km highway / 5–10 intersections | Point sensing + basic comms + edge compute | $0.7–2.8M |
| L2 | Intersection | 10–50 intersections | Holo-intersection + local coordination + AI signal | $2.8–11M |
| L3 | District | 50–300 intersections / 50 km highway | District coordination + digital twin + C-ITS | $11–42M |
| L4 | Citywide | 300–3,000 intersections / citywide | City TOC + AI-native + VIC integrated | $42–210M |
| L5 | City-cluster | Cross-city / cross-province | Cross-domain coordination + data interop + national platform | $210M+ |

### 5.2 Detailed Criteria

**L1 Segment:** sensing video >80% key, radar >30%; 4G/LTE backhaul >50 Mbps; edge IPC; baseline security; apps: video + basic incident + flow.

**L2 Intersection:** holo-intersection (video+radar fusion); fiber + 4G/5G, <50 ms; edge AI box per 8–16 streams; apps: AI signal (point) + holo + green-wave.

**L3 District:** district-wide multi-source fusion; 5G + C-V2X PC5, <20 ms; edge MEC + private cloud; apps: district coordinated signal + digital twin + C-ITS L1–L2.

**L4 Citywide:** citywide coverage, radar-video fusion >50%; 5G + C-V2X full, NR-V2X trial; hybrid cloud + MEC cluster; apps: city TOC + transport LLM + full VIC.

**L5 City-cluster:** cross-city interop + low-altitude fusion; 5G-A/6G trial + LEO-sat backup; distributed cloud + federated learning; apps: cross-city control + national data platform + AI-native governance.

### 5.3 Progression and Investment

```
L1→L2: sensing fill + AI + connectivity, +100–300% / intersection
L2→L3: V2X + digital twin + district coord, +200–500%
L3→L4: city brain + LLM + full coverage, +300–800%
L4→L5: cross-domain + standards + national platform, +500–1000%
```
**No-skip principle:** L1→L3 cannot be skipped; L2→L4 may accelerate with strong backing; L3→L5 needs institutional break + org change, not just tech.

---

## VI. Four-Horizontal, Three-Vertical Cybersecurity Architecture

### 6.1 Overview

```
┌──────────────────────────────────────────────────────────────┐
│           Regulations & Standards System (Vertical 1)           │
├──────────────────────────────────────────────────────────────┤
│  Security Mgmt (H4) │ Policy │ Org │ Assessment │ Awareness     │
├──────────────────────────────────────────────────────────────┤
│  Security Ops (H3)   │ SOC monitor │ Response │ Drill │ Threat intel │
├──────────────────────────────────────────────────────────────┤
│  Security Tech (H2)  │ Access │ Encrypt │ IDS │ Vuln mgmt        │
├──────────────────────────────────────────────────────────────┤
│  Physical Security (H1)│ Access │ Video │ Env │ Fire │ Power     │
├──────────────────────────────────────────────────────────────┤
│  Data Security (V2)  │ Classification │ Encrypt │ Mask │ Review │ Backup │ Destroy │
├──────────────────────────────────────────────────────────────┤
│  Supply-Chain Security (V3)│ SBOM │ Vendor eval │ Code review │ Secure SDL │
└──────────────────────────────────────────────────────────────┘
```

### 6.2 NIST CSF 2.0 Mapping

| CSF Function | Transport Control | Example System |
|-------------|------------------|---------------|
| **IDENTIFY** | Asset inventory / risk assessment / supply chain | Toll-asset inventory + TOC risk register |
| **PROTECT** | Access control / encryption / training | Signal-system MFA + FIPS 140-3 crypto |
| **DETECT** | Logging / SIEM / anomaly | Toll anomalous-transaction AI detection |
| **RESPOND** | Incident response plan | Traffic-incident response SOP |
| **RECOVER** | Backup / continuity | Signal degrade-mode + geo-redundancy |

### 6.3 Compliance Checklist

See `references/07-transport-cybersecurity-and-critical-infra.md`.

---

## VII. Six-Layer Data Governance Framework

### 7.1 Layers

```
L6 Data Application — data products / services / trading / open sharing
L5 Data Operations — quality / security / standards / lifecycle
L4 Data Development — modeling / ETL / feature eng / API / lab
L3 Data Storage — lake / warehouse / real-time / graph / time-series
L2 Data Integration — batch / real-time / CDC / MQ / API gateway
L1 Data Source — structured / semi / unstructured / stream / IoT / external
```

### 7.2 Quality Scoring

| Dimension | Weight | Metric | Target |
|---------|:------:|-------|:----:|
| Completeness | 30% | Missing % | <3% |
| Accuracy | 25% | Error % | <1% |
| Consistency | 15% | Cross-source diff % | <2% |
| Timeliness | 15% | Transfer latency (min) | <5 |
| Uniqueness | 10% | Dup % | <0.5% |
| Validity | 5% | Format non-conform % | <1% |

### 7.3 Data Product Development

Path: data resource → data asset → data product → data capital.
1. **Resource**: catalog, aggregation, basic governance.
2. **Asset**: clarify ownership, capitalize per accounting standard (e.g., local data-asset rules).
3. **Product**: standardized products (e.g., "city mobility index", "segment risk", "transit OD").
4. **Capital**: listed trading / financing / equity.

---

## VIII. ADKAR Change Management

### 8.1 Model

| Stage | Public-sector adaptation | Key Action |
|------|--------------------------|-----------|
| **Awareness** | Secure top-down mandate / directive support | ① Benchmark-site visits ② Expert briefings ③ Agency backing |
| **Desire** | Dissolve "more work = more risk" fear | ① Error-tolerance list ② Peer success cases ③ Performance KPI |
| **Knowledge** | Tiered training (decision/mid/frontline) | ① Decision: value+risk+outcome ② Mid: process+coord ③ Frontline: skill+flow |
| **Ability** | Pilot + escort + continuous enablement | ① Pilot then scale ② On-site support ③ Fast-response channel |
| **Reinforcement** | Assessment + incentive + iterate | ① Digital KPI in annual review ② Recognize leaders ③ Feedback loop |

### 8.2 Stakeholder Communication Plan

| Stakeholder | Role | Concern | Channel | Frequency |
|------------|------|--------|---------|:--:|
| Executive sponsor | Sponsor | Outcome / safety / big picture | Written + face-to-face | Key nodes |
| Transport agency head | Owner | Results / no incidents | Formal + site visit | Monthly |
| Finance / budget | Gatekeeper | Reasonable / compliant | Finance-language report | By node |
| Operations manager | User | Congestion / crash / enforcement | Data + cases | Monthly |
| Data office | Coordinator | Sharing / coherence | Architecture + standards | Bi-weekly |
| Funding authority | Approver | Budget / procurement compliance | ROI + econ eval | By node |
| Frontline officer | End-user | Ease / no burden | Training + manual | During impl. |

### 8.3 Golden Rules of Multi-Party Communication

1. Secure executive support first — major programs need written mandate / minutes.
2. Speak the funder's language — economics / ROI, not tech jargon.
3. Data + case dual drive — every recommendation carries a number + a peer case.
4. Documentation is armor — record and sign off key decisions.
5. Never bypass the middle layer — "top sponsor + executing owner" both matter.
6. Manage the "vertical–horizontal" relationship — functional regulator + local authority are dual decision-makers.

---

## IX. Ten-Phase Large-Project Lifecycle

### 9.1 Panorama

```
Phase 01      Phase 02      Phase 03      Phase 04      Phase 05
Biz Dev &      Current-State  Strategy &    Tech Selection  Financing &
Opp Identify   Diagnosis      Top Design   & Vendor Eval  Investment Review
    │             │             │             │             │
    ▼             ▼             ▼             ▼             ▼
Phase 06      Phase 07      Phase 08      Phase 09      Phase 10
Tech Procure   System Dev &   Deployment &  Ops Optimize  Post-Review &
& Contract     Integration   Change Mgmt   & Value Track  Continuous Iteration
```

### 9.2 Deliverables and Gates

| Phase | Core Deliverable | Gate Condition | Typical Duration |
|------|-----------------|----------------|:--------------:|
| 01 | Project initiation, needs analysis | Clear client intent | 1–3 mo |
| 02 | T-DMM diagnosis, gap analysis | Gap accepted by client | 1–3 mo |
| 03 | Strategy, 3-yr roadmap, estimate | Approved by exec | 2–4 mo |
| 04 | Tech selection, vendor eval, PoC | Tech frozen | 2–4 mo |
| 05 | Feasibility, affordability, plan | Funding approved + review passed | 2–6 mo |
| 06 | Procurement docs, SOW contract | Contract signed | 2–6 mo |
| 07 | Design, test, deploy plan | Preliminary verification | 6–18 mo |
| 08 | UAT, training, go-live report | Final verification, live | 1–3 mo |
| 09 | Ops monthly, KPI board, health dash | — | Ongoing |
| 10 | Post-review, phase-2 proposal | Review complete | 6–12 mo post |

### 9.3 Risk Register

| Risk | Prob | Impact | Mitigation |
|------|:----:|:------:|-----------|
| Approval delay | High | High | Start 6 mo early, keep funding comms |
| Investment review fail | Med | Extreme | Conservative econ, multiple financing |
| Leadership change disrupts | Med | High | Continuity clause, mid-term plan |
| Data-sharing fails | High | Med | Higher-level directive, sharing agreement |
| Vendor under-delivers | Med | High | ≥3 shortlist, phased delivery |
| User resistance / low adoption | Med | Med | ADKAR, training, incentives |

---

## X. Twelve-Country ITS Benchmark Framework

### 10.1 Country-by-Country

| Country | Core Route | Governance | Comms Std | Data Open | Strength | Weakness |
|--------|-----------|----------|---------|:--------:|---------|---------|
| **China** | New infra + VIC | State-led + SOE | C-V2X | 25% | Scale / speed / scenarios | Fragmented std / local protection |
| **USA** | AV-first + PPP | State-led + federal | C-V2X (shifting) | 65% | Innovation / open data | Weak federal coord / aging infra |
| **EU** | Standards + C-ITS | Supranational | ITS-G5→C-V2X | 70% | Unified std / cross-border | Divergent national pace |
| **Japan** | ETC 2.0 + ITS Connect | Public + industry alliance | ITS Connect 760 MHz | 35% | Mature ETC / craftsmanship | Insular / weak internationalization |
| **Korea** | 5G-V2X + AV test | Strong public push | C-V2X | 45% | 5G lead / dense testbeds | Small market |
| **Singapore** | City TOC + ERP 2.0 | Strong public lead | C-V2X + DSRC | 85% | Highest data openness / ITS intensity | Too small to replicate |
| **UK** | Open data + congestion charge | Devolved + agency | ITS-G5 | 85% | Data API / congestion charge | Under-investment / slow update |
| **Germany** | Industry 4.0 + AV act | Federal + standards | ITS-G5→C-V2X | 60% | Auto industry + standards | Lagging digital infra |
| **UAE** | Future city + oil fund | Public + sovereign fund | Multi | 55% | Ample funds / bold pilots | Talent dependence / smalll scale |
| **Netherlands** | Cycling + transit + smart city | PPP | ITS-G5 | 75% | Innovation culture / MaaS | Small market |
| **Sweden** | Vision Zero safety | Public + academia | ITS-G5 | 70% | World #1 traffic safety | Small market |
| **Israel** | Tech innovation + AI startup | Startup ecosystem | Hybrid | 60% | Innovation / Mobileye | Small local market |

### 10.2 How to Use

1. Pick 2–3 most similar reference countries by project profile.
2. Compare across governance / tech / investment / data / operations.
3. Quantify gaps (openness / ETC rate) and assess qualitative (governance) gaps.
4. Separate "transferable" vs "reference-only"; localize.
5. Refresh benchmark data every 12 months.

---

> **Legal Notice**: This document is a reference file of the *Transportation Digital & AI Transformation Expert (Standard Edition)* Skill. Methodologies are for learning reference; apply with professional judgment. T-DMM / RICE++ / Seven-Dimension Matrix are original methodologies — cite the source when referencing.

> **Last updated**: July 2025 | **Version**: v1.0
