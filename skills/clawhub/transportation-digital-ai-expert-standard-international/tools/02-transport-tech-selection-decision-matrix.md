# Transportation Technology Selection Decision Matrix
## Transportation Technology Selection Decision Matrix

---

## 1. Tool Overview

This tool provides a systematic decision framework for selecting transportation technologies. It covers 7 evaluation dimensions, 50+ indicators, and a complete tool chain including a vendor scorecard, PoC design guide, TCO calculator, and contract-negotiation checklist. It applies to procurement decisions for signal control systems, big-data platforms, AI platforms, Traffic Management Centers (TMC), MaaS platforms, V2X / cooperative-ITS equipment, cloud platforms, digital-twin platforms, and similar transportation technologies.

### Use Cases
- Selecting transportation technology products / platforms / solutions
- Vendor evaluation and comparison
- Make vs. Buy decision analysis
- Technology architecture review
- Procurement decision briefing materials

---

## 2. Seven-Dimension Framework & Weight Configuration

### 2.1 Dimension Definitions & Default Weights
| Code | Dimension | Default Weight | Description |
|------|-----------|----------------|-------------|
| T | Technical Fit | 25% | Architecture, performance, compatibility, scalability |
| F | Functional Coverage | 20% | Business-function satisfaction, scenario coverage |
| V | Vendor Strength | 15% | Qualification, industry experience, R&D capability |
| C | Cost-Effectiveness | 15% | TCO, ROI, licensing model |
| S | Service & Support | 10% | Implementation, O&M, training, responsiveness |
| R | Risk Control | 10% | Technical, lock-in, and compliance risk |
| I | Innovation & Foresight | 5% | Technical advancement, roadmap evolution, ecosystem |

### 2.2 Weight Calibration Workshop
Adjust dimension weights by project type:
| Project Type | T | F | V | C | S | R | I |
|--------------|---|---|---|---|---|---|---|
| Core platform (e.g., big-data platform) | 30% | 15% | 20% | 10% | 10% | 10% | 5% |
| Business application (e.g., signal control) | 15% | 30% | 15% | 15% | 10% | 10% | 5% |
| Innovation pilot (e.g., digital twin) | 20% | 10% | 10% | 10% | 10% | 10% | 30% |
| Large program (e.g., TMC) | 15% | 20% | 20% | 10% | 15% | 15% | 5% |
| Infrastructure (e.g., cloud platform) | 25% | 10% | 15% | 20% | 10% | 15% | 5% |

---

## 3. 50+ Indicators Explained

### Dimension T: Technical Fit (12 items)
| # | Indicator | Weight | Scoring (1–5) |
|---|-----------|--------|---------------|
| T1 | Architecture advancement | 10% | 1=monolith; 3=microservices / distributed; 5=cloud-native + Serverless + service mesh |
| T2 | System performance | 10% | 1=unsatisfactory; 3=meets current needs; 5=exceeds with 3-yr headroom |
| T3 | Reliability | 10% | 1=availability < 99%; 3=99.9%; 5=99.99%+ (< 53 min/yr downtime) |
| T4 | Scalability | 10% | 1=none; 3=horizontal scaling; 5=elastic autoscaling |
| T5 | Local-stack / sovereignty compatibility | 8% | 1=no local-stack support; 3=partial (e.g., local OS/DB); 5=full local-stack adaptation (local chips+OS+DB+middleware) where mandated |
| T6 | Standardized interfaces | 8% | 1=no standard API; 3=RESTful API; 5=full API + GraphQL + messaging + standards-compliant (DATEX II / NTCIP / ISO) |
| T7 | Integration capability | 8% | 1=standalone; 3=common systems connected; 5=open platform + low-code + 300+ connectors |
| T8 | Data security | 8% | 1=no measures; 3=ISO 27001 / basic compliance; 5=ISO 27001 + strong crypto (FIPS 140-2 / AES) end-to-end |
| T9 | Technology autonomy / control | 8% | 1=fully third-party dependent; 3=partial in-house + open-source control; 5=full in-house + source-code delivery |
| T10 | Deployment flexibility | 7% | 1=single deployment only; 3=private/public cloud options; 5=hybrid + edge + on-prem appliance |
| T11 | Operability / manageability | 7% | 1=no O&M tools; 3=basic monitoring/alerting; 5=AIOps + automated + self-healing |
| T12 | Tech-stack maturity | 6% | 1=obscure; 3=mainstream; 5=industry standard + large-scale proven |

### Dimension F: Functional Coverage (10 items)
| # | Indicator | Weight | Scoring (1–5) |
|---|-----------|--------|---------------|
| F1 | Core-function satisfaction | 20% | 1=<50%; 3=80%; 5=100%+ value-add |
| F2 | Scenario coverage | 15% | 1=1–2 scenarios; 3=mainstream scenarios; 5=full coverage |
| F3 | User experience | 10% | 1=hard to use; 3=usable; 5=intuitive + NPS>50 |
| F4 | Customization | 10% | 1=none; 3=config-based; 5=low-code / no-code |
| F5 | Mobile support | 8% | 1=none; 3=responsive / PWA; 5=native app + unified multi-device |
| F6 | Reporting & analytics | 8% | 1=none; 3=fixed reports; 5=self-service BI + AI + wall display |
| F7 | Multi-tenancy | 7% | 1=none; 3=logical tenancy; 5=physical tenancy + isolation + elastic quota |
| F8 | Internationalization / multilingual | 5% | 1=single language; 3=bilingual; 5=multilingual + localization |
| F9 | Offline / disconnected operation | 5% | 1=network dependent; 3=partial cache; 5=edge autonomy + normal offline ops |
| F10 | Domain-specific features | 12% | 1=generic; 3=has transport edition; 5=deep transport-domain heritage |

### Dimension V: Vendor Strength (8 items)
| # | Indicator | Weight | Scoring (1–5) |
|---|-----------|--------|---------------|
| V1 | Scale & stability | 15% | 1=<50 staff / startup; 3=500–2,000 staff; 5=>5,000 or listed / government-backed |
| V2 | Transport industry experience | 20% | 1=no transport cases; 3=5–10 cases; 5=50+ cases across sub-sectors |
| V3 | R&D spend ratio | 12% | 1=<5%; 3=10%–20%; 5=>30% |
| V4 | Certifications | 10% | 1=none; 3=CMMI3 / ISO 27001; 5=CMMI5 + multiple certs + local-content certified |
| V5 | Reference satisfaction | 15% | 1=no references; 3=2–3 verifiable; 5=10+ benchmark clients, NPS>70 |
| V6 | Delivery capability | 12% | 1=outsourced; 3=in-house delivery team; 5=PMO + national service network |
| V7 | Partner ecosystem | 8% | 1=none; 3=basic ecosystem; 5=open platform + 200+ ISV/SI |
| V8 | Financial health | 8% | 1=severe losses; 3=breakeven; 5=sustained profit + high growth (see Section 10) |

### Dimension C: Cost-Effectiveness (7 items)
| # | Indicator | Weight | Scoring (1–5) |
|---|-----------|--------|---------------|
| C1 | License / subscription fee | 15% | 1=far over budget; 3=within budget; 5=well below budget |
| C2 | Implementation service fee | 12% | 1=>30% over; 3=within ±10%; 5=>20% under |
| C3 | Custom dev cost | 10% | 1=costly per change; 3=fair pricing; 5=config-based, no custom dev |
| C4 | O&M cost | 12% | 1=heavy dedicated O&M; 3=standard O&M suffices; 5=automated, minimal effort |
| C5 | Upgrade / expansion cost | 10% | 1=upgrade=re-purchase; 3=smooth w/ discount; 5=subscription includes upgrades |
| C6 | 5-yr TCO | 25% | 1=much higher than peers; 3=market average; 5=clearly better than peers |
| C7 | ROI / payback | 16% | 1=>5 yrs; 3=~3 yrs; 5=<1 yr |

### Dimension S: Service & Support (6 items)
| # | Indicator | Weight | Scoring (1–5) |
|---|-----------|--------|---------------|
| S1 | Implementation methodology | 20% | 1=none; 3=standard process; 5=agile + DevOps + best-practice library |
| S2 | Training system | 15% | 1=none; 3=basic; 5=certification + knowledge transfer + enablement |
| S3 | Response speed | 20% | 1=no SLA; 3=5×8; 5=7×24×365 + 30-min response |
| S4 | Technical support | 18% | 1=outsourced; 3=dedicated team; 5=TAC + source-level support |
| S5 | Documentation completeness | 12% | 1=none; 3=basic; 5=full docs + video + community |
| S6 | Local service | 15% | 1=remote only; 3=regional center; 5=on-site resident + spare-parts depot |

### Dimension R: Risk Control (5 items)
| # | Indicator | Weight | Scoring (1–5) |
|---|-----------|--------|---------------|
| R1 | Lock-in risk | 25% | 1=strong (proprietary protocol/format); 3=partially open; 5=fully open standards + replaceable |
| R2 | Compliance risk | 25% | 1=non-compliant; 3=basically compliant; 5=beyond-compliant + forward-looking |
| R3 | Supply continuity risk | 20% | 1=single-vendor dependent; 3=has backup; 5=open-source alternative + source escrow |
| R4 | Data migration risk | 15% | 1=data not exportable; 3=exportable but complex; 5=standard format one-click migration |
| R5 | IP risk | 15% | 1=unclear ownership; 3=clearly contracted; 5=source shared / joint IP |

### Dimension I: Innovation & Foresight (4 items)
| # | Indicator | Weight | Scoring (1–5) |
|---|-----------|--------|---------------|
| I1 | Roadmap foresight | 30% | 1=obsolete soon; 3=mainstream; 5=industry-leading direction |
| I2 | AI / intelligence | 25% | 1=no AI; 3=has AI module; 5=deep LLM / AIGC integration |
| I3 | Ecosystem openness | 25% | 1=closed; 3=API open; 5=open platform + developer community |
| I4 | Release velocity | 20% | 1=annual or slower; 3=quarterly; 5=monthly + continuous delivery |

---

## 4. Vendor Scorecard Template

### 4.1 Scorecard Summary
| Dimension | Weight | Vendor A | Vendor B | Vendor C |
|-----------|--------|----------|----------|----------|
| T Technical Fit | __% | __/5 = __ | __/5 = __ | __/5 = __ |
| F Functional Coverage | __% | __/5 = __ | __/5 = __ | __/5 = __ |
| V Vendor Strength | __% | __/5 = __ | __/5 = __ | __/5 = __ |
| C Cost-Effectiveness | __% | __/5 = __ | __/5 = __ | __/5 = __ |
| S Service & Support | __% | __/5 = __ | __/5 = __ | __/5 = __ |
| R Risk Control | __% | __/5 = __ | __/5 = __ | __/5 = __ |
| I Innovation & Foresight | __% | __/5 = __ | __/5 = __ | __/5 = __ |
| **Weighted Total** | **100%** | **____** | **____** | **____** |
| **Rank** | | **#__** | **#__** | **#__** |

### 4.2 Scoring Formula
```
Dimension Score = SUM(indicator score × indicator weight)
Weighted Total   = SUM(dimension score × dimension weight)
```

### 4.3 Grade Bands
| Weighted Total | Grade | Conclusion |
|---------------|-------|------------|
| 4.0 – 5.0 | A | Strongly recommended — preferred vendor |
| 3.5 – 3.9 | B+ | Recommended — shortlist for negotiation |
| 3.0 – 3.4 | B | Considerable — watch specific risks |
| 2.5 – 2.9 | C | Backup — only after major improvement |
| < 2.5 | D | Not recommended |

### 4.4 Radar Comparison Notes
Plot each vendor's score on the seven axes to compare strengths/weaknesses. Rules of thumb:
- **Large overlap** = capabilities are close; price / service become the differentiators
- **A vendor leads on T** = prioritize for technology-led projects
- **Weak on F but strong on T** = caution for customization-heavy projects; OK for standardized ones

---

## 5. PoC Design Guide

### 5.1 PoC Decision Flow
```
Is a PoC needed?
├── Investment > $7M        → Strongly recommended
├── Investment $2.8M–$7M    → Recommended
├── Investment $1.4M–$2.8M  → Lite PoC (tech validation)
├── Investment < $1.4M      → Optional
├── Low maturity / high novelty → Mandatory PoC (regardless of amount)
└── Proven same-scale case exists → May skip (reference validation only)
```

### 5.2 PoC Design Template
```
============================================================
              PoC Design — [Project X]
============================================================

[PoC Basics]
Project: ____________________
Objective: ____________________
Duration: ____ weeks (suggest 2–8 by complexity)
Vendors: ☐ Single  ☐ 2–3 compared  ☐ Sequential

[Test Scenarios] (suggest 3–5 core scenarios)
Scenario 1: ____________________ (weight: ___%)
  - Description: ________________________________________
  - Input data: ________________________________________
  - Expected output: ____________________________________
  - Success criteria: ____________________________________

Scenario 2: ____________________ (weight: ___%)
  (same as above)

Scenario 3: ____________________ (weight: ___%)
  (same as above)

[Performance / Load Scenario]
  - Concurrent users: ______
  - Data volume: ______
  - Response-time requirement: ______ ms
  - Success-rate requirement: ______ %

[Integration Scenario]
  - Systems to integrate: ______
  - Protocols / interfaces: ______

[PoC Resource Needs]
  - Vendor effort: ______ person-days
  - Client effort: ______ person-days
  - Hardware / environment: ____________________
  - Data preparation: ____________________

[PoC Scoring]
| Item | Weight | Vendor A | Vendor B | Notes |
|------|--------|----------|----------|-------|
| Function satisfaction | 30% | /5 | /5 | |
| Performance | 20% | /5 | /5 | |
| Implementation efficiency | 15% | /5 | /5 | |
| Usability / UX | 10% | /5 | /5 | |
| Technical capability shown | 10% | /5 | /5 | |
| Integration | 10% | /5 | /5 | |
| Docs / training | 5% | /5 | /5 | |
| PoC Total | 100% | ____ | ____ | |

[Go / No-Go]
  - PoC total ≥ 3.5 → Go (formal procurement)
  - PoC total 3.0–3.4 → Conditional Go (supplemental validation needed)
  - PoC total < 3.0 → No-Go
  - Any veto item in a key scenario → No-Go

[PoC Pass Criteria — all must be met]
  ☐ All core scenarios pass
  ☐ Performance metrics met
  ☐ Integration tests pass
  ☐ Data security validated
  ☐ Team collaboration satisfactory
============================================================
```

### 5.3 PoC Timeline
| Week | Phase | Activity | Deliverable |
|------|-------|----------|-------------|
| W1 | Kickoff | Kick-off, environment, requirements | PoC plan |
| W2–3 | Deploy & Integrate | Deploy, data load, interface testing | Deployment report |
| W4–6 | Scenario Validation | Scenario-by-scenario test, tracking, tuning | Test report |
| W7 | Stress Test | Load, stability, security | Stress report |
| W8 | Review | Results review, scoring, Go/No-Go | PoC summary |

---

## 6. Reference-Customer Survey (10 questions)
```
============================================================
            Vendor Reference-Customer Survey
============================================================

[Basics]
Customer: ____________________
Contact / Title: ____________________
Phone: ____________________
Date: ____________________

1. How long have you used [Vendor X]'s [Product Y]?
   A: ________________________________________

2. What was the main reason you chose this vendor? In hindsight, was it right?
   A: ________________________________________

3. Gap between actual experience and pre-sales demo? (1–5, 1=large gap)
   Score: ___  Notes: ________________________________________

4. Biggest challenge during implementation? How did the vendor resolve it?
   A: ________________________________________

5. Post-launch stability & performance? (1–5, 1=frequent failures)
   Score: ___  Avg monthly incidents: ____  Notes: ________________________________________

6. Post-sales responsiveness & resolution? (1–5, 1=very poor)
   Score: ___  Avg response time: ____ hrs  Example: ________________________________________

7. Single most important improvement you'd suggest?
   A: ________________________________________

8. Any budget overrun from contract to go-live? If so, by how much?
   A: ________________________________________

9. If you chose again, would you pick this vendor? Why?
   A: ________________________________________

10. Advice for peers about to buy this product?
   A: ________________________________________

[Overall Recommendation] (1–5): ___  [Willing to be a reference?] ☐ Yes ☐ No
============================================================
```

---

## 7. Contract Negotiation Checklist (24 items)
```
============================================================
            Contract Negotiation Checklist
============================================================

[Product / Service Definition]
☐ 1. Product name, version, module list, license type & quantity
☐ 2. Service scope (implementation, dev, training, O&M boundaries)
☐ 3. Function delivery standard (key feature list + acceptance criteria)
☐ 4. Exclusions (what is out of scope)

[Price & Payment]
☐ 5. Total price breakdown (software/hardware/implementation/training/O&M)
☐ 6. Payment milestones tied to deliverables (not time-only)
☐ 7. Whether all third-party licenses included (DB, middleware, etc.)
☐ 8. Annual maintenance fee & cap on increase (suggest ≤ 5%/yr)
☐ 9. Discount rate for expansion / add-ons (lock future price)
☐ 10. Price validity period

[Implementation & Delivery]
☐ 11. Project plan & milestones (with key dependencies)
☐ 12. Both parties' effort & responsibilities (RACI matrix)
☐ 13. Acceptance criteria & process (initial / final)
☐ 14. Late-delivery penalties (suggest weekly escalating, cap 15–20%)

[Quality & Assurance]
☐ 15. SLA metrics (availability, response time, recovery time)
☐ 16. SLA breach penalties / compensation mechanism
☐ 17. Warranty period & free-fix scope

[IP & Security]
☐ 18. IP ownership (especially custom development)
☐ 19. Source-code escrow arrangement
☐ 20. Data-security responsibility & confidentiality obligations

[Supplementary]
☐ 21. Force majeure & liability limits
☐ 22. Termination conditions & exit mechanism (data migration obligation)
☐ 23. Dispute resolution (arbitration / litigation & venue)
☐ 24. Team-stability guarantee (key-person lock, change notice)

============================================================
Checked by: ____________  Date: ____________
============================================================
```

---

## 8. 5-Year TCO Calculator

### 8.1 TCO Model
```
============================================================
            5-Year Total Cost of Ownership (TCO)
            All figures in US$ millions
============================================================

[One-time]                                          Vendor A    Vendor B
1. Software license                                 ________    ________
2. Hardware / servers                               ________    ________
3. System integration / implementation              ________    ________
4. Data migration / initialization                  ________    ________
5. Custom development                               ________    ________
6. Third-party software / middleware licenses       ________    ________
   One-time subtotal (A)                            ________    ________

[Annual O&M] (unit price × 5 yrs)
7. Annual maintenance / subscription (×5)           ________    ________
8. Hardware O&M / data-center (×5)                  ________    ________
9. Leased line / bandwidth (×5)                     ________    ________
10. System O&M labor (×5)                           ________    ________
11. Upgrade / expansion (est.)                      ________    ________
12. Training (est.)                                 ________    ________
13. Security & compliance (×5)                      ________    ________
   Annual subtotal (B)                              ________    ________

[Hidden Costs]
14. Internal labor (coordination, management)       ________    ________
15. System switch / migration                       ________    ________
16. Reserved for lock-in / switch risk              ________    ________
   Hidden subtotal (C)                              ________    ________

============================================================
5-Year TCO = A + B + C =                             ________    ________
============================================================
```

### 8.2 TCO Comparison Template
| Dimension | Vendor A | Vendor B | Diff |
|-----------|----------|----------|------|
| Initial investment | $___M | $___M | +/−$___M |
| 5-yr O&M | $___M | $___M | +/−$___M |
| 5-yr TCO | $___M | $___M | +/−$___M |
| TCO as % of total investment | ___% | ___% | |
| Avg annual TCO | $___M | $___M | |
| Unit cost (per user / per device) | $___ | $___ | |
| Initial : TCO ratio (lower better) | ___ | ___ | |

---

## 9. Make vs. Buy Decision Tree

### 9.1 Flow
```
              ┌─── Is it a differentiating core capability?
              │
          ┌───┤
          │   └─── Yes → In-house R&D capability?
          │              ├── Yes → Enough R&D resources (30+ team)?
          │              │         ├── Yes → [MAKE]
          │              │         └── No  → [PARTNER] (joint R&D / source buy)
          │              └── No  → [BUY + deep customization]
          │
          └─── No → Mature commercial product on market?
                       ├── Yes → Meets 80%+ of needs?
                       │         ├── Yes → [BUY]
                       │         └── No  → [BUY + config / low-code]
                       └── No → Reliable open-source option?
                                  ├── Yes → [OPEN SOURCE] (OSS + services)
                                  └── No → [MAKE / rebuild]
```

### 9.2 Make vs. Buy Scoring Matrix
| Dimension | Weight | Make | Buy | Notes |
|-----------|--------|------|------|-------|
| Core differentiation | 20% | /5 | /5 | More core → Make |
| In-house R&D capability | 20% | /5 | /5 | Stronger → Make |
| Time-to-market urgency | 15% | /5 | /5 | More urgent → Buy |
| Market maturity | 15% | /5 | /5 | Mature → Buy |
| Long-term ownership cost | 15% | /5 | /5 | |
| IP protection need | 10% | /5 | /5 | |
| Continuous iteration need | 5% | /5 | /5 | |
| **Weighted Total** | **100%** | **____** | **____** | |

**Rules:**
- Make > Buy by 20%+ → strongly recommend in-house
- Make ≈ Buy (gap < 10%) → recommend joint development (Buy + source + co-build)
- Buy > Make by 20%+ → strongly recommend procurement

---

## 10. Vendor Financial-Health Checklist
| Item | Method | Warning Signs |
|------|--------|---------------|
| Registered & paid-in capital | Business registries (D&B, Companies House, national registers) | Capital far below industry scale |
| 3-yr revenue trend | Annual reports / prospectuses / research | Decline > 20% for 3 yrs |
| Profitability | Financial statements | 3 consecutive years of loss |
| Cash flow | Filings / industry analysis | Sustained negative operating cash flow |
| Funding / listing | Public info | Last round > 24 months ago |
| Customer concentration | Prospectus / research | Single client > 50% |
| Staff stability | LinkedIn / Glassdoor | Major loss of exec / R&D talent |
| Litigation / disputes | Court records (PACER / national registers) | Multiple pending contract disputes |
| IP | Patent databases (USPTO / EPO / WIPO) | Core product has no patents / copyrights |
| Related-party risk | Equity-structure analysis | Complex affiliated-company network |

---

## 11. Selection Decision Report Template
```
============================================================================
                  Technology Selection Decision Report — [Project X]
============================================================================

[Background]
Project: ____________________
Investment scale: ____________________
Time requirement: ____________________

----------------------------------------------------------------------------
1. Selection Overview
----------------------------------------------------------------------------
Category: ____________________
Vendors evaluated: A/B/C (___ total)
Period: _______ to _______

----------------------------------------------------------------------------
2. Results
----------------------------------------------------------------------------
[Scorecard — see Section 4]

----------------------------------------------------------------------------
3. Technical Validation (PoC)
----------------------------------------------------------------------------
☐ PoC performed; summary:
   Vendor A: ________________________________________
   Vendor B: ________________________________________
   Conclusion: ________________________________________
☐ No PoC; reason: ________________________________________

----------------------------------------------------------------------------
4. TCO Comparison
----------------------------------------------------------------------------
[TCO table — see Section 8]

----------------------------------------------------------------------------
5. Risk Analysis
----------------------------------------------------------------------------
| Risk | Vendor A | Vendor B | Vendor C | Mitigation |
|------|----------|----------|----------|------------|
| Lock-in | | | | |
| Delivery delay | | | | |
| Team stability | | | | |
| Hidden cost | | | | |

----------------------------------------------------------------------------
6. Recommendation
----------------------------------------------------------------------------
Primary: Vendor ____
Backup: Vendor ____
Rationale:
  1. ________________________________________
  2. ________________________________________
  3. ________________________________________

Key risks:
  1. ________________________________________
  2. ________________________________________

Next steps:
  1. Negotiation focus: ________________________________________
  2. Contract focus: ________________________________________
  3. Implementation note: ________________________________________

============================================================================
Decision team sign-off: ________________  Date: ________________
============================================================================
```

---

## 12. Usage Instructions
1. **Set dimension weights**: Use the table in Section 2 by project type.
2. **Filter indicators**: Pick 30–40 key indicators from the 50+ by product type.
3. **Score vendors**: Assemble a team (5–7) to score independently, then aggregate.
4. **PoC validation**: Run PoC on core vendors (Section 5).
5. **Reference due diligence**: Survey at least 2–3 existing customers (Section 6).
6. **TCO calculation**: Compute full 5-year TCO (Section 8).
7. **Contract negotiation**: Confirm item-by-item per checklist (Section 7).
8. **Decision report**: Write the selection report per template (Section 11).
