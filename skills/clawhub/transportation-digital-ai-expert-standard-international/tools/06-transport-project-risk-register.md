# Transportation Project Risk Register
## Transportation Project Risk Register

---

## 1. Tool Overview

This risk register provides a systematic risk-management tool for transportation digitalization projects. It covers 10 risk categories and 100+ pre-identified risk items; each item includes probability / impact scores, mitigation strategy, contingency plan, owner, and trigger conditions. It applies across the full lifecycle from kickoff to acceptance.

### Risk Scoring Standard

#### Probability (1–5)
| Score | Description | Quant. Ref |
|-------|-------------|-----------|
| 1 | Very low | < 5% chance |
| 2 | Low | 5%–15% |
| 3 | Medium | 15%–35% |
| 4 | High | 35%–60% |
| 5 | Very high | > 60% |

#### Impact (1–5)
| Score | Description | Schedule | Cost | Quality |
|-------|-------------|----------|-------|--------|
| 1 | Minimal | < 1 wk delay | < 5% over | Negligible |
| 2 | Small | 1–2 wk delay | 5%–10% over | Slight drop |
| 3 | Medium | 2–4 wk delay | 10%–20% over | Partial degradation |
| 4 | Large | 1–2 mo delay | 20%–30% over | Core function impaired |
| 5 | Severe | > 2 mo / project halted | > 30% over | Project failure |

#### Risk Level
- **Score = Probability × Impact**
- **High (H):** Score ≥ 15 (focus, detailed response plan)
- **Medium (M):** Score 8–14 (continuous monitoring, response ready)
- **Low (L):** Score ≤ 7 (periodic check)

---

## 2. 100+ Pre-Identified Risks

### Category A: Technical Risk (15 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| A1 | Wrong technology selection | 3 | 5 | 15 | H | Multi-vendor comparison + PoC + expert review | Backup plan, switch window reserved | Tech Lead | Major review disagreement |
| A2 | System performance below target | 3 | 4 | 12 | M | Early perf test, clear SLA | Scale-out plan, defer non-critical | Architect | Load test fail (>10% deviation) |
| A3 | Data quality unfit for AI | 4 | 4 | 16 | H | Pre-assess data, preprocessing plan | Synthetic data, lower accuracy target | Data Lead | Data availability < 70% |
| A4 | Integration with legacy fails | 3 | 4 | 12 | M | Interface spec first, joint dev/test | Standalone mode, manual import | Integration Lead | > 3 failed joint tests |
| A5 | Low stability (frequent faults) | 3 | 5 | 15 | H | Reliability design (redundancy / degrade), chaos eng. | Auto-failover, stronger on-call | Ops Lead | > 3 faults / month |
| A6 | Tech stack obsolete / EOL | 2 | 4 | 8 | M | Forward-looking roadmap, open-source first | Upgrade budget, alternatives | Tech Lead | Vendor EOL notice |
| A7 | Data migration failure / loss | 2 | 5 | 10 | M | Migration + rollback + validation | Run old system in parallel | Data Lead | Migration diff > 1% |
| A8 | Security hole → data breach | 2 | 5 | 10 | M | Security + pentest + code review | Take down–fix–notify plan | Security Lead | Critical vuln found in pentest |
| A9 | AI model accuracy below expectation | 4 | 3 | 12 | M | Phased train/eval, min-acceptable line | Degrade to rules engine / MVP | AI Lead | Val-set accuracy < target by >10% |
| A10 | Third-party API / SDK dependency | 3 | 3 | 9 | M | SLA + degrade + multi-source | Switch to backup API / offline | Tech Lead | 3rd-party API avail < 99.5% |
| A11 | Tech-debt accumulation | 4 | 2 | 8 | M | Code standards + review + debt tracking | Dedicated refactor sprints | Tech Lead | Coverage drop > 10% |
| A12 | Open-source vuln / license issue | 3 | 3 | 9 | M | OSS scan + license review | Replace / upgrade affected | Security Lead | Scan finds critical vuln |
| A13 | Cloud / data-center failure | 2 | 4 | 8 | M | Multi-AZ / multi-cloud, DR drill | DR switch + manual takeover | Ops Lead | Cloud status anomaly |
| A14 | Insufficient compute (AI) | 4 | 3 | 12 | M | Compute planning first, elastic scale | Smaller / lighter model | AI Lead | GPU util > 90% for 7 days |
| A15 | Large-scale edge-device failure | 3 | 4 | 12 | M | Device admission test, spare stock, OTA | Manual patrol + spare swap | HW Lead | Online rate drop > 5% |

### Category B: Management Risk (15 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| B1 | Unclear / frequent change req. | 5 | 4 | 20 | H | Freeze period + change control + prototype | Prioritize, defer low-priority | PM | > 5 changes / month |
| B2 | Scope creep | 4 | 3 | 12 | M | Scope baseline + change board | Split into phases | PM | New scope > 20% of original |
| B3 | Schedule slip | 4 | 4 | 16 | H | Critical-path mgmt + buffer + agile | Fast-track + add resources | PM | SPI < 0.85 for 2 wks |
| B4 | Budget overrun | 3 | 4 | 12 | M | 10–15% reserve + monthly cost track | Cut non-core / phase | PM | CPI < 0.9 and >10% over |
| B5 | Key person leaving | 3 | 4 | 12 | M | Knowledge capture + A/B backup | External consultant + hiring | HR + PM | Core member departs |
| B6 | Team capability gap | 3 | 3 | 9 | M | Onboarding + upskilling + experts | Outsource / buy solution | PM | Code-quality review fails |
| B7 | Poor communication / info gap | 3 | 2 | 6 | L | Weekly + daily / weekly report + IM | Escalate comms level | PM | Key info > 24h late |
| B8 | Project priority downgraded | 3 | 4 | 12 | M | Regular value sync with exec, secure sponsor | Shrink scope, accelerate | Sponsor | Exec reschedule |
| B9 | Over-reliance on consultants | 3 | 3 | 9 | M | Knowledge-transfer + internal training | Extend contract / replace | PM | Consultant leaves before internal ready |
| B10 | Cross-dept coordination resistance | 4 | 3 | 12 | M | Charter clarifies R&R + exec backing | Escalate to steering committee | PM | Key resource > 2 wks late |
| B11 | Vendor / partner non-cooperation | 3 | 3 | 9 | M | Contract obligations + regular forum | Commercial escalation + contract | Procurement + PM | > 48h late response ×3 |
| B12 | Insufficient testing → defects | 3 | 3 | 9 | M | Test-plan review + automation + UAT | Rollback + hotfix + extend pilot | Test Lead | Defect density > 2× target |
| B13 | Ambiguous acceptance criteria | 3 | 3 | 9 | M | Contract / spec states acceptance | 3rd-party eval + negotiate | PM + Commercial | Major dispute at acceptance |
| B14 | Cutting corners under schedule pressure | 3 | 4 | 12 | M | Code review + quality gate + independent test | Delay non-core go-live | Tech Lead | Unit coverage below standard |
| B15 | Pandemic / major-event shutdown | 2 | 4 | 8 | M | Remote-work plan + flexible schedule | Remote + delayed delivery | PM | Public shutdown notice |

### Category C: Vendor Risk (10 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| C1 | Vendor bankruptcy / acquisition | 2 | 5 | 10 | M | Financial assessment + source escrow | Take over source + backup vendor | Procurement | Sudden financial / negative news |
| C2 | Vendor core-team attrition | 3 | 3 | 9 | M | Contract key-person + backup clause | Require supplemental staff | Procurement | Personnel change rate > 50% |
| C3 | Vendor delivery incapacity | 3 | 4 | 12 | M | Phased delivery assessment + penalties | Cut scope / terminate / partial in-house | PM + Procurement | Milestone > 30 days late |
| C4 | Vendor IP dispute | 2 | 5 | 10 | M | Clear IP ownership + IP review | Replace infringing module | Legal + Procurement | 3rd-party infringement notice |
| C5 | Vendor roadmap change / EOL | 2 | 4 | 8 | M | Lock-in risk assessment + open standards | Migrate to alternative | Tech Lead | Product EOS / EOL notice |
| C6 | Vendor data-security issue | 2 | 5 | 10 | M | Data-security clause + review + audit right | Recover data + legal action | Security Lead | Data-breach incident |
| C7 | Vendor subcontracting out of control | 3 | 3 | 9 | M | Master contract limits subcontracting + approval | Replace unqualified subcontractor | Procurement | Subcontractor quality / schedule issue |
| C8 | Vendor contract dispute | 2 | 4 | 8 | M | Rigorous clauses + regular commercial comms | Legal support + backup vendor | Legal + Procurement | Negotiation deadlock |
| C9 | Weak local service capability | 4 | 3 | 12 | M | Assess local team + service SLA | Find local 3rd-party service | PM | Service response > 3× SLA |
| C10 | Single-vendor lock-in | 4 | 3 | 12 | M | Open standards + avoid proprietary + multi-source | Gradual decoupling + backup build | Tech Lead | Irreplaceable proprietary tech found |

### Category D: Regulatory & Compliance Risk (10 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| D1 | Sudden regulatory change | 3 | 4 | 12 | M | Track regs + flexible arch + compliance review | Emergency compliance + redesign | Legal / GR | New draft regulation published |
| D2 | Data compliance / cross-border data | 3 | 5 | 15 | H | Data classification + compliance review + local storage | Data isolation + system rectification | Data Protection Officer | Compliance check fails |
| D3 | Local-content / sovereignty mandate | 4 | 4 | 16 | H | Forward-looking local-stack design + adaptation plan | Parallel local-stack adaptation / transition | Tech Lead | Local-content mandate issued |
| D4 | PPP / concession regulation change | 2 | 5 | 10 | M | Contract change-of-law clause + multi-party comms | Renegotiate / terminate | Legal + GR | Relevant regulation published |
| D5 | Public-funding delay / cut | 3 | 4 | 12 | M | Milestone billing + independent reserve | Shrink scope / pause | Finance Lead | Budget adjustment notice |
| D6 | Audit / inspection requirement | 3 | 3 | 9 | M | Process compliance trail + doc standards | Cooperate, supply materials | PM | Audit notice |
| D7 | Stricter environmental regulation | 2 | 2 | 4 | L | EMC / noise / EMF compliant design | Add environmental measures | Tech Lead | New emission / radiation standard |
| D8 | Labor / social-security law change | 2 | 2 | 4 | L | Compliant employment + flexible staffing | Adjust staffing | HR | New labor law published |
| D9 | Emergency / public-safety regulation | 2 | 3 | 6 | L | Built-in emergency function + drills | Emergency compliance response | Security Lead | New emergency requirement |
| D10 | Standard change / new standard | 3 | 2 | 6 | L | Join SDO + decouple architecture | Adapt to standard | Tech Lead | New international / national standard |

### Category E: Information Security Risk (10 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| E1 | External attack (DDoS / APT) | 3 | 5 | 15 | H | Protection + situational awareness + pentest | IR process + attribution + hardening | Security Lead | Security alert anomaly |
| E2 | Insider data leak | 2 | 5 | 10 | M | Least-privilege + audit + DLP | Forensics + accountability + notice | Security Lead | Abnormal data access |
| E3 | Ransomware / malware | 3 | 5 | 15 | H | Endpoint + mail filter + backup + training | Isolate + disinfect + restore | Security Lead | AV alert |
| E4 | Third-party interface risk | 3 | 4 | 12 | M | Interface auth + encryption + rate-limit + review | Cut suspicious interface + fix | Security Lead | Abnormal interface call |
| E5 | IoT / edge device security | 4 | 3 | 12 | M | Device auth + firmware security + comms encryption | Isolate infected + firmware upgrade | IoT Lead | Abnormal device behavior |
| E6 | Identity / access flaw | 3 | 4 | 12 | M | MFA + permission review + unified IDM | Revoke urgently + harden | Security Lead | Abnormal permission use |
| E7 | Incomplete logging / audit | 3 | 2 | 6 | L | Standardized logging + SIEM + retention | Supplement log collection | Ops Lead | Incident not traceable |
| E8 | Security certification non-compliance (ISO 27001 / FIPS) | 3 | 4 | 12 | M | Compliance first + periodic assessment | Add measures + rectify | Security Lead | Assessment finds issues |
| E9 | Supply-chain attack | 2 | 5 | 10 | M | Vendor security review + software supply-chain security | Cut affected supply + announce | Security Lead | Vendor security incident |
| E10 | Slow security incident response | 3 | 4 | 12 | M | IR plan + drills + on-call | Escalate + external security service | Security Lead | Incident > 1h unresponded |

### Category F: Financial Risk (8 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| F1 | Insufficient budget approval | 3 | 5 | 15 | H | Solid feasibility + reserve + multiple sources | Shrink scope + phase | Finance / PM | Budget < 70% of feasibility |
| F2 | FX volatility (imported equipment) | 3 | 3 | 9 | M | Lock rate + local-currency settlement | Replace with local equipment | Procurement | FX move > 5% |
| F3 | ROI below expectation | 3 | 4 | 12 | M | Strict feasibility + sensitivity + post-review | Optimize ops + new revenue | Finance Lead | Benefit < 70% of forecast |
| F4 | Funding disbursement delay | 4 | 3 | 12 | M | Plan milestones early + track payment | Advance + commercial coord | Finance Lead | Due payment > 30 days late |
| F5 | Tax / finance cost over | 2 | 2 | 4 | L | Tax planning + advisor | Apply preferential policy | Finance Lead | New tax policy |
| F6 | O&M cost over budget | 3 | 3 | 9 | M | Cost monitor + elastic + energy mgmt | Optimize ops + seek support | Ops Lead | Monthly O&M > 20% over |
| F7 | Revenue / toll below expectation | 3 | 4 | 12 | M | Market analysis + pilot + elastic pricing | Add services + marketing | Ops Lead | Monthly revenue < 70% forecast |
| F8 | Insufficient insurance coverage | 2 | 3 | 6 | L | Risk insurance + advisor | Apply for additional cover | Finance Lead | New risk scenario |

### Category G: Operations & Maintenance Risk (8 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| G1 | Poor O&M handover | 4 | 4 | 16 | H | O&M manual + training + parallel transition | Vendor extended support + urgent hire | PM + Ops | O&M onboarding < 80% |
| G2 | High long-term O&M cost | 3 | 3 | 9 | M | TCO assessment + automation + OSS | Optimize + cloudize | Ops Lead | Annual O&M > 50% over budget |
| G3 | Equipment aging / EOL parts | 3 | 3 | 9 | M | Spare stock + lifecycle plan + alternative | Urgent purchase + upgrade | HW Lead | Device EOL / EOS notice |
| G4 | Low business-user adoption | 4 | 3 | 12 | M | User research + training + pilot + UX | Mandate + tie to KPI | Business Lead | Post-launch DAU < 50% expected |
| G5 | Process change makes system unfit | 3 | 3 | 9 | M | Track process change + configurable system | Fast iterate + reconfigure | PM | Business publishes new process |
| G6 | Scaling cannot meet growth | 3 | 3 | 9 | M | Elastic arch + capacity plan + periodic review | Urgent scale + rate-limit | Architect | Resource util > 85% |
| G7 | Stale content / knowledge base | 3 | 2 | 6 | L | Content mgmt + periodic review | Urgent update + manual fallback | Content Lead | Content age > 6 months |
| G8 | Catastrophic failure → outage | 1 | 5 | 5 | L | DR + active-active + plan + drills | DR switch + degraded operation | Ops Lead | Primary system fully unavailable |

### Category H: Stakeholder Risk (10 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| H1 | Weak executive support | 3 | 5 | 15 | H | Value comms + regular report + demo | Seek more exec attention + shrink scope | Sponsor | Repeated absence from reviews |
| H2 | Business unit resistance | 4 | 3 | 12 | M | Show business value + cultivate early adopters | Exec push + enforce | PM | Low cooperation in research |
| H3 | Key stakeholder change | 3 | 3 | 9 | M | Relationship care + decision log + onboard new | Re-align + supplement report | PM | Stakeholder list change |
| H4 | Conflicting stakeholder needs | 4 | 3 | 12 | M | Prioritize + coordination meeting | Exec decision + compromise | PM + Sponsor | Deadlock at requirement review |
| H5 | Negative public / media sentiment | 2 | 4 | 8 | M | Sentiment monitor + PR plan + user comms | Announce + adjust | PR / GR | Negative sentiment spreads |
| H6 | End-user resistance | 3 | 3 | 9 | M | User-in-design + training + transition | Dual-track + guide usage | PM | Complaints surge / very low use |
| H7 | Union / industry-association opposition | 2 | 3 | 6 | L | Early comms + balance interests + pilot first | Dialogue + adjust | GR + HR | Union / association opposes |
| H8 | Departments passing the buck | 3 | 3 | 9 | M | RACI matrix + clear boundaries | Escalate + clarify assessment | PM | Key work unclaimed |
| H9 | Policy / election-cycle impact | 2 | 5 | 10 | M | Document value + align to policy goals | Accelerate key delivery + handover docs | GR + Sponsor | Major stakeholder personnel change |
| H10 | Lengthy approval process | 4 | 3 | 12 | M | Pre-analyze path + parallel + pre-comms | Escalate + interim authorization | PM | Key approval > 2 wks overdue |

### Category I: Data Risk (8 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| I1 | Incomplete / inaccurate collection | 4 | 4 | 16 | H | Data-quality assessment + validation + redundant capture | Re-collect + manual check | Data Lead | Completeness < 90% |
| I2 | Insufficient timeliness | 3 | 3 | 9 | M | Capture-frequency design + real-time channel | Estimate + lower timeliness need | Data Lead | Data delay > tolerance |
| I3 | Data silos cannot be linked | 4 | 4 | 16 | H | Unified standard + data-sharing platform | Manual aggregation as interim | Data Lead | Core source cannot connect |
| I4 | Data-privacy compliance risk | 3 | 5 | 15 | H | Privacy impact assessment + minimize + anonymize | Delete non-compliant data + compliance fix | DPO | Privacy review finds issue |
| I5 | Poor labeling quality (AI) | 4 | 4 | 16 | H | Labeling spec + QA + platform | Re-label + professional labeling | AI Lead | Label consistency < 90% |
| I6 | Historical data unavailable | 3 | 3 | 9 | M | Start early + alternative sources | Shorten window + external data | Data Lead | Needed history absent |
| I7 | Insufficient volume (AI) | 3 | 4 | 12 | M | Data augmentation + synthetic + few-shot | Simpler model + transfer learning | AI Lead | Training samples < minimum |
| I8 | Unclear data rights / authorization | 3 | 4 | 12 | M | Data rights + authorization + compliance review | Pause disputed data + negotiate | DPO | Authorization dispute |

### Category J: External Environment Risk (6 items)
| ID | Risk | P | I | Score | Level | Mitigation | Contingency | Owner | Trigger |
|----|------|---|---|-------|-------|-----------|-------------|-------|---------|
| J1 | Macroeconomic downturn | 3 | 3 | 9 | M | Flexible budget + value-first delivery | Cut non-core investment | Finance Lead | GDP / PMI sharp drop |
| J2 | Intensified competition (innovation) | 3 | 3 | 9 | M | Differentiation + moat + fast iterate | Accelerate commercial + ecosystem | Business Lead | Competitor launches similar product |
| J3 | Disruptive tech shift | 2 | 4 | 8 | M | Track trends + incremental architecture | Refactor + upgrade | Tech Lead | Disruptive tech goes mainstream |
| J4 | Major natural disaster (flood / quake / pandemic) | 1 | 5 | 5 | L | BCP + remote work | Activate BCP + recover | Security Lead | Public emergency response activated |
| J5 | Chip / supply-chain shortage | 2 | 3 | 6 | L | Multi-vendor + local alternative + safety stock | Adjust + find alternative HW | Procurement | Lead time > 2× standard |
| J6 | Power / energy supply issue | 2 | 3 | 6 | L | UPS + generator + multi-feed | Lower non-core power | Ops Lead | Power-rationing / outage notice |

---

## 3. Risk Heat-Map Guide

### 3.1 Heat-Map Matrix
```
Impact
 5 │ ░░  ░░  ██  ██  ██
   │ L   L   H   H   H
 4 │ ░░  ░░  ██  ██  ██
   │ L   M   M   H   H
 3 │ ░░  ░░  ░░  ██  ██
   │ L   M   M   M   H
 2 │ ░░  ░░  ░░  ░░  ░░
   │ L   L   M   M   M
 1 │ ░░  ░░  ░░  ░░  ░░
   │ L   L   L   L   M
   └───────────────────
     1   2   3   4   5  Probability

██ = High (H): Score ≥ 15
░░ = Medium (M): Score 8–14
░░ = Low (L): Score ≤ 7
```

### 3.2 Usage
1. Place each identified risk at its P×I position.
2. Red (H) risks need a detailed response plan; review weekly.
3. Yellow (M) risks need continuous monitoring; review monthly.
4. Green (L) risks periodic check; review quarterly.

### 3.3 Typical Distribution of 100+ Risks
| Level | Count (est.) | Share | Strategy |
|-------|--------------|-------|----------|
| High (H) | 15–25 | ~15–25% | Detailed plan, weekly tracking |
| Medium (M) | 45–55 | ~50% | Monitor metrics, monthly review |
| Low (L) | 20–30 | ~25% | Periodic check, quarterly review |

---

## 4. Risk Review Meeting Template
```
============================================================================
                 Project Risk Review Minutes
============================================================================

Date: ____________________   Attendees: ____________________

----------------------------------------------------------------------------
1. Prior-Meeting Risk Tracking
----------------------------------------------------------------------------
| Risk ID | Last Decision | Status | State | Escalate? |
|---------|--------------|--------|-------|-----------|
| XX | | | ☐ Closed ☐ Monitoring ☐ Worsening | ☐ Yes ☐ No |

----------------------------------------------------------------------------
2. New Risks Identified
----------------------------------------------------------------------------
| ID | Description | P | I | Score | Level | Mitigation | Owner | Due |
|----|-------------|---|---|-------|-------|-----------|-------|-----|
| | | | | | | | | |

----------------------------------------------------------------------------
3. Risk Status Change
----------------------------------------------------------------------------
| ID | Risk | Old P/I | New P/I | Reason | Adjustment |
|----|------|---------|---------|--------|------------|
| | | / | / | | |

----------------------------------------------------------------------------
4. High-Risk Deep Dive
----------------------------------------------------------------------------
Risk ID: ________
Current state: ____________________
Decision: ____________________
Next action: ____________________

----------------------------------------------------------------------------
5. Risk Trend Analysis
----------------------------------------------------------------------------
High-risk count: ___ → ___
Avg score: ___ → ___
Trend: ☐ Down ☐ Flat ☐ Up

----------------------------------------------------------------------------
6. Action Items
----------------------------------------------------------------------------
| Action | Owner | Due | Priority |
|--------|-------|-----|----------|
| | | | |

============================================================================
Next meeting: ____________________
============================================================================
```

---

## 5. Historical Failure Cases & Risk Mapping

### 5.1 Typical Failures
| Case | Failure Cause | Risk Type | Risk IDs | Lesson |
|------|--------------|-----------|----------|--------|
| A city ITS platform (Phase 1) | Poor data quality, AI model untrainable | Data | I1, I5 | Data assessment must come first |
| A regional smart motorway | Regulatory change → inconsistent V2X standard | Regulatory | D1, D10 | Regulation-sensitive projects need flexible design |
| A city transit digitalization | Business unit non-cooperation, system unused | Stakeholder | H2, G4 | Business change management matters |
| A public-agency big-data platform | Vendor bankruptcy, no source code | Vendor | C1 | Source escrow is non-negotiable |
| A city parking platform | Insufficient budget, project halted | Financial | F1 | Phased delivery beats all-in |
| A motorway toll system | Failed cutover, toll booths paralyzed | Technical + Ops | A3, G8 | Adequate transition + rollback plan |
| A city MaaS platform | User growth far below forecast | Ops + Market | G4 | Promotion & operations matter equally |
| An AI signal project | Model effect below expectation, poor ROI | Technical | A9, F3 | AI projects need a failure plan |

### 5.2 Industry Lessons
| Lesson | Applies To |
|--------|-----------|
| Data governance before AI | All AI & big-data projects |
| Don't launch all features at once; phase delivery | Large platform projects |
| Business units must participate deeply, not IT-only | Business application systems |
| Contract must specify source escrow and IP | Projects depending on external vendors |
| Reserve 15–20% budget & schedule buffer | All projects |
| Pilot 10% of scenarios first, then scale | Innovation projects |
| Large projects: watch leadership-change & policy windows | Large projects |
| Data-privacy compliance first, not after-the-fact | Projects involving personal data |

---

## 6. Risk Monitoring Dashboard

### 6.1 Weekly Risk Dashboard
```
============================================================================
              Project Risk Dashboard (Week __)
============================================================================

Overall: ☐ Green (safe)  ☐ Yellow (watch)  ☐ Red (alert)

High: ___ (vs last wk: +___ / −___)
Medium: ___ (vs last wk: +___ / −___)
Low: ___ (vs last wk: +___ / −___)

----------------------------------------------------------------------------
[TOP 5 High Risks]
| Rank | Risk ID | Brief | Score | State | This week |
|------|---------|-------|-------|-------|-----------|
| 1 | | | | ☐ Worse ☐ Stable ☐ Better | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

----------------------------------------------------------------------------
[Triggered Alerts]
  Triggered this week: ________________________________________
  Likely soon: ________________________________________

----------------------------------------------------------------------------
[Needs PM / Sponsor decision]
  1. ________________________________________
  2. ________________________________________
============================================================================
```

---

## 7. Usage Instructions
1. **First risk-identification workshop**: At kickoff, run a 2–3 hr workshop using this register as a checklist.
2. **Score P and I**: For each identified risk, assign P and I; compute score and level.
3. **Response plan**: For High and Medium risks, define mitigation and contingency.
4. **Assign owner**: One unique owner per risk.
5. **Regular review**: High weekly, Medium monthly, Low quarterly.
6. **Dynamic update**: Continuously identify new risks; adjust P/I.
7. **Trace lessons**: See Section 5 to avoid repeating failures.
8. **Close-out summary**: At project end, aggregate all realized risks and impacts into an organizational risk knowledge base.
