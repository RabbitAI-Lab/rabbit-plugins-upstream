# Transportation Data Quality Assessment Toolkit

## Transportation Data Quality Assessment Toolkit

---

## 1. Toolkit Overview

This toolkit provides a systematic framework for assessing transportation data quality, covering six quality dimensions, detailed rating criteria, a problem-classification and remediation guide. It is designed for data-quality governance across transport data lakes, big-data platforms, integrated transport operations centers, and AI training-data pipelines.

### Six Assessment Dimensions

| Dimension | English | Definition | Default Weight |
|-----------|---------|------------|----------------|
| DQ1 | Completeness | Whether data is missing / null, and whether collection coverage is comprehensive | 20% |
| DQ2 | Accuracy | Whether data truly reflects real-world conditions | 25% |
| DQ3 | Timeliness | Whether the delay from generation to availability is acceptable | 20% |
| DQ4 | Consistency | Whether the same data from different systems / sources agrees | 15% |
| DQ5 | Uniqueness | Whether data contains duplicate records | 10% |
| DQ6 | Traceability | Whether data source and processing are traceable | 10% |

---

## 2. Detailed Rating Criteria (1–5 per dimension)

### DQ1: Completeness

| Score | Criteria |
|-------|----------|
| 1 | Critical-field missing rate >20%, large gaps in core collection points |
| 2 | Critical-field missing rate 10–20%, some collection points uncovered |
| 3 | Critical-field missing rate 2–10%, main collection points covered |
| 4 | Critical-field missing rate <2%, near-full coverage |
| 5 | Critical-field missing rate <0.5%, full-element coverage with a missing-data compensation mechanism |

**Completeness Checks by Transport Data Category:**

| Data Category | Key Fields | Minimum Completeness |
|---------------|-----------|----------------------|
| Traffic flow | Time, intersection ID, lane, flow, occupancy, speed | ≥95% (per-minute) |
| Vehicle GPS | Plate/ID, time, longitude, latitude, speed, heading | ≥98% |
| Transit smart-card | Card ID, route, board time, alight time (if any) | ≥90% |
| Video surveillance | Device ID, time, stream URL, device status | ≥99% |
| Signal timing | Intersection ID, phase, cycle, green split, plan time | ≥99% |
| Traffic crash | Time, location, type, casualties, fault determination | ≥95% |
| Parking data | Lot ID, time, entry/exit, plate | ≥90% |
| Carbon emissions | Time, zone, source, emission volume | ≥85% |

### DQ2: Accuracy

| Score | Criteria |
|-------|----------|
| 1 | Major data clearly erroneous (deviation >30%), no validation mechanism |
| 2 | Some data erroneous (deviation 15–30%), basic validation |
| 3 | Data basically accurate (deviation 5–15%), rules exist but incomplete |
| 4 | High accuracy (deviation 1–5%), sound validation & correction mechanism |
| 5 | Very high precision (deviation <1%), multi-source cross-validation + AI auto-correction |

**Reference Accuracy by Transport Data Category:**

| Data Category | Baseline Accuracy | Notes |
|---------------|-------------------|-------|
| Detector flow | ≥95% | Radar / loop detection; periodic calibration needed |
| Plate recognition | ≥98% (day) / ≥95% (night) | Affected by weather / lighting |
| GPS positioning | Civilian 5–10 m, differential <1 m | Urban-canyon effect |
| Mobile signaling | ≥85% (location), ≥90% (OD) | Base-station handover drift |
| Transit smart-card | ≥98% | Tap accuracy; alight inferred with error |
| Video event detection | Detection ≥95%, false-alarm <5% | AI model precision |
| Weather data | ≥95% | Station-level weather stations |
| Carbon estimation | ≥80% (estimate) | Inherently model-based |

### DQ3: Timeliness

| Score | Criteria |
|-------|----------|
| 1 | Data delay >1 hour, fails business needs |
| 2 | Data delay 15–60 min, acceptable but efficiency impacted |
| 3 | Data delay 5–15 min, main business runs normally |
| 4 | Data delay 1–5 min (near-real-time), good core experience |
| 5 | Data delay <1 s (real-time), end-to-end latency controlled |

**Timeliness Requirements by Scenario:**

| Scenario | Requirement | Source |
|----------|-------------|--------|
| V2X safety warning | <100 ms | RSU / OBU |
| Real-time signal control | <1 s | Intersection detectors |
| Dynamic routing | 1–5 min | Floating car / detectors |
| Traffic-state monitoring | 1–5 min | Multi-source fusion |
| Transit arrival prediction | <30 s (refresh) | GPS / smart-card |
| Trip route planning | <5 min | Traffic-condition service |
| Traffic statistics | Daily / weekly / monthly | Offline aggregation |
| Carbon report | Monthly / quarterly | Monthly aggregation |

### DQ4: Consistency

| Score | Criteria |
|-------|----------|
| 1 | Same data across systems differs >30%, no consistency check |
| 2 | Difference 15–30%, occasional checks |
| 3 | Difference 5–15%, rule-based checks but incomplete |
| 4 | Difference 1–5%, systematic consistency checks |
| 5 | Difference <1%, real-time consistency monitoring + auto-repair |

**Common Transport Data Consistency Issues:**

| Scenario | Typical Inconsistency | Root Cause |
|----------|----------------------|-----------|
| Different detectors, same intersection | Difference >10% | Detector type / placement |
| Plate recognition vs. toll system | Plate mismatch | OCR error / cloned plate |
| GPS trajectory vs. road network | Vehicle off-road | GPS drift / inaccurate network |
| Smart-card vs. manual passenger count | Difference >15% | Alight-inference algorithm |
| Crash data vs. insurance claim | Severity mismatch | Different statistical caliber |
| Different map networks | Road-attribute mismatch | Update frequency / source |

### DQ5: Uniqueness

| Score | Criteria |
|-------|----------|
| 1 | Duplicate rate >10%, no de-duplication |
| 2 | Duplicate rate 5–10%, manual de-dup |
| 3 | Duplicate rate 1–5%, basic de-dup rules |
| 4 | Duplicate rate <1%, automated de-dup |
| 5 | Duplicate rate <0.1%, real-time de-dup + idempotent design |

### DQ6: Traceability

| Score | Criteria |
|-------|----------|
| 1 | No source record at all |
| 2 | Source described but no structured record |
| 3 | Structured record of source & processing for key data |
| 4 | Full-chain data lineage (collect → process → apply) |
| 5 | Complete lineage + change history + versioning + audit log |

---

## 3. Assessment Method

### 3.1 Sampling & Detection Method

| Data Type | Sampling Strategy | Detection Method | Min. Sample |
|-----------|-------------------|------------------|-------------|
| Traffic flow | Random 2 weeks (incl. weekday & holiday) | Statistical + visualization | 100k+ records |
| Vehicle GPS | Random 100 vehicles × 7 days | Trajectory + anomaly detection | 1M+ records |
| Transit smart-card | Random 1 month | Statistics + OD validation | 500k+ records |
| Video / image | Random 1000+ frames | Human-labeled validation | 1000+ frames |
| Crash records | Full 3 months | Logic + manual review | All |
| Parking data | Random 10 lots × 1 week | Entry/exit time validation | 10k+ records |

### 3.2 Scoring Formula

```
Dimension Score = (sum of indicator scores in dimension / number of indicators)
Total DQ Score = DQ1×20% + DQ2×25% + DQ3×20% + DQ4×15% + DQ5×10% + DQ6×10%

Grade:
  4.5–5.0 : Grade A — Excellent; directly usable for AI training & key decisions
  3.5–4.4 : Grade B — Good; usable for most analysis & applications
  2.5–3.4 : Grade C — Acceptable; basic use OK, governance needed for advanced use
  1.5–2.4 : Grade D — Poor; remediate before use
  <1.5   : Grade E — Very poor; rebuild the data system recommended
```

---

## 4. Data-Quality Problem Classification & Remediation Guide

### 4.1 Problem Classification System

| Category | ID | Typical Problem | Severity | Fix Difficulty | Remediation |
|----------|----|-----------------|----------|----------------|-------------|
| Missing | M01 | Collection-device fault causes missing data | High | Medium | Repair device + backfill / interpolation |
| Missing | M02 | New system lacks historical data | Medium | High | Back-estimate + mark data start date |
| Missing | M03 | Optional fields mostly empty | Low | Low | Mandatory constraint + default |
| Anomaly | A01 | Sensor drift / fault produces absurd values | High | Medium | Anomaly detection + device calibration |
| Anomaly | A02 | Transmission error (garble / truncation) | High | Low | Validate + re-collect |
| Anomaly | A03 | Inconsistent units / coordinate systems | High | Medium | Format standardization |
| Duplicate | D01 | Multiple systems re-collect same event | Medium | Medium | De-dup + master-data management |
| Duplicate | D02 | Retransmission / backfill causes duplicates | Medium | Low | De-dup + idempotent design |
| Timeliness | T01 | Network latency / insufficient bandwidth | High | High | Network optimization + edge pre-processing |
| Timeliness | T02 | Batch interval too long | Medium | Low | Adjust ETL frequency |
| Consistency | C01 | Different caliber / granularity across systems | Medium | High | Unify standard + data mapping |
| Consistency | C02 | Heterogeneous DB time / encoding mismatch | Medium | Medium | Unified encoding + timezone spec |
| Traceability | R01 | Unknown source / black-box processing | Low | Medium | Build lineage + processing log |

### 4.2 Remediation Priority Matrix

```
                  High Impact
                      ↑
       Fix Now        │      Fix First
   (Critical Bug)     │   (Major Issue)
                      │
    ┌─────────────────┼─────────────────┐
    │                 │                 │
    │  Large-area data │  Severe cross-  │
    │  loss from device│  system caliber │
    │  failure         │  inconsistency │
    │                 │                 │
    ├─────────────────┼─────────────────┤
    │                 │                 │
    │  Limited historic│  Aging-device   │
    │  traceability    │  precision drift│
    │                 │                 │
    └─────────────────┴─────────────────┘
       Fix Later       │      Plan Fix
    (Minor Issue)      │   (Planned)
                      │
                  Low ←── Frequency / Scope ──→ High
```

---

## 5. Data-Quality Monitoring Dashboard Design

### 5.1 Dashboard Metrics

```
============================================================================
              Transportation Data-Quality Monitoring Dashboard
============================================================================

[Overall DQ Score]: ____ (Grade A/B/C/D/E)
  Change vs. last month: +___ / -___
  Healthy-source ratio: ____% (target >95%)

----------------------------------------------------------------------------
[By Data Source]

| Source | Completeness | Accuracy | Latency | Consistency | Uniqueness | Score | Trend |
|--------|-------------|----------|---------|-------------|------------|-------|-------|
| Microwave detector | 96% | 94% | <1s | - | 99% | 4.2 | → |
| Magnetic detector | 92% | 90% | <1s | - | 98% | 3.8 | ↓ |
| Video AI analytics | 98% | 95% | 2s | - | 100% | 4.3 | → |
| Floating-car GPS | 88% | 85% | 30s | 82% | 95% | 3.2 | ↑ |
| Transit smart-card | 94% | 98% | 5min | 90% | 99% | 4.0 | → |
| Mobile signaling | 85% | 80% | 15min | - | 92% | 3.0 | → |
| Parking data | 90% | 95% | 10s | 95% | 98% | 4.0 | ↑ |
| Weather data | 99% | 98% | 5min | - | 100% | 4.8 | → |

----------------------------------------------------------------------------
[By Quality Dimension]

Completeness heatmap:  █████████░░░ 94%
Accuracy heatmap:      ████████░░░░ 92%
Timeliness heatmap:    ██████████░░ 96%
Consistency heatmap:   ███████░░░░░ 88%
Uniqueness heatmap:    █████████░░░ 97%
Traceability:          ██████░░░░░░ 75%

----------------------------------------------------------------------------
[Alerts]

High risk (act immediately):
  □ Source [___] completeness <85% for 2 hours
  □ Source [___] latency > [__] min for 30 min

Medium risk (within 24h):
  □ Source [___] accuracy <90%
  □ Inter-system consistency [___] vs [___] <85%

Low risk (within week):
  □ Source [___] trending down continuously
  □ Traceability coverage <80%

----------------------------------------------------------------------------
[DQ Issue Trend (last 30 days)]
  New issues: ___ (vs last month: +/-___)
  Resolved: ___
  Backlog: ___
  Avg. fix time: ___ hours

============================================================================
```

### 5.2 Alert Threshold Recommendations

| Source Type | Completeness | Accuracy | Latency | Sustained Anomaly |
|-------------|--------------|----------|---------|-------------------|
| Real-time control (signal / detector) | <95% | <93% | >5 s | >5 min |
| Near-real-time (GPS / video) | <90% | <90% | >1 min | >30 min |
| Batch (smart-card / signaling) | <85% | <85% | >30 min | >2 h |
| Statistical (monthly / annual) | <90% | <90% | >24 h | >1 day |

---

## 6. Data-Quality SLA Template

```
============================================================================
            Transportation Data-Quality SLA (Service Level Agreement)
============================================================================

Effective:______________  Review:______________

[Scope]
  Data domain:____________________
  Data source:____________________
  Consumer:____________________

----------------------------------------------------------------------------
SLA Metrics — Definition & Targets
----------------------------------------------------------------------------

| Metric | Definition | Calculation | Target | Monthly Min | Frequency |
|--------|------------|-------------|--------|-------------|-----------|
| Completeness | Non-null fields / total | (1-null rate)×100% | ≥98% | ≥95% | Daily |
| Accuracy | Within tolerance of truth | (1-anomaly rate)×100% | ≥97% | ≥93% | Weekly |
| Timeliness | Generation-to-available delay | P99 latency | <1min | <5min | Hourly |
| Availability | Online service time ratio | uptime / total | ≥99.9% | ≥99.5% | Monthly |
| Consistency | Cross-system difference within tolerance | consistent / total | ≥95% | ≥90% | Weekly |
| Traceability | Traceable to source ratio | traceable / total | ≥100% | ≥95% | Monthly |

----------------------------------------------------------------------------
Monitoring Frequency
----------------------------------------------------------------------------
□ Real-time (1-min):____________________
□ Near-real-time (15-min):____________________
□ Daily inspection: all sources
□ Weekly report: full assessment + trend
□ Monthly report: SLA attainment + rating

----------------------------------------------------------------------------
Incident Response SLA
----------------------------------------------------------------------------
| Level | Response | Recovery | Notify |
|-------|----------|----------|--------|
| P0 (core business) | ≤15 min | ≤2 h | All stakeholders + management |
| P1 (partial business) | ≤30 min | ≤8 h | Project + business lead |
| P2 (monitoring / stats) | ≤4 h | ≤24 h | Data team |
| P3 (minor) | ≤8 h | ≤72 h | Data team |

----------------------------------------------------------------------------
SLA Breach Handling
----------------------------------------------------------------------------
Monthly attainment <95%:________________________________________
2 consecutive months below:________________________________________
Major (P0) data-quality incident:________________________________________
Annual attainment <90%:________________________________________

============================================================================
Sign-off:
Data Provider:________________  Date:________________
Data Governor:________________  Date:________________
============================================================================
```

---

## 7. Data-Quality Improvement Roadmap Template

```
============================================================================
        Data-Quality Improvement Roadmap (____/__ – ____/__)
============================================================================

[Current-State Assessment]
  DQ total score: ____ (Grade __)
  Core problems:________________________________________________

----------------------------------------------------------------------------
Phase 1: Firefighting (Months 1–3) — Resolve Critical Issues
----------------------------------------------------------------------------
Goal: raise DQ total from ____ to ____

Actions:
□ 1. Repair offline / faulty collection devices (expect +5–10% completeness)
□ 2. Establish basic DQ monitoring & alerts
□ 3. Fix Top-10 high-frequency anomalies
□ 4. Stand up daily source-online-rate report
□ 5. Backfill key historical missing fields

Resources: ___ FTE team, budget $____M
Milestone: end of M3, completeness ≥95%, P0 issues cleared

----------------------------------------------------------------------------
Phase 2: Governance (Months 4–9) — Build the System
----------------------------------------------------------------------------
Goal: raise DQ total from ____ to ____

Actions:
□ 1. Unify data standards & encoding
□ 2. Build DQ platform (rule engine + monitoring + reporting)
□ 3. Cross-system consistency governance
□ 4. Establish DQ SLA & assessment mechanism
□ 5. Build data-lineage tracking
□ 6. Form DQ team (2–3 dedicated)

Resources: ___ FTE team, budget $____M
Milestone: end of M9, total ≥4.0 (Grade B), SLA attainment ≥95%

----------------------------------------------------------------------------
Phase 3: Optimization (Months 10–18) — Continuous Improvement
----------------------------------------------------------------------------
Goal: raise DQ total from ____ to ____

Actions:
□ 1. AI-assisted anomaly detection & auto-repair
□ 2. Data catalog & DQ certification
□ 3. Promote DQ culture (business units participate)
□ 4. Full real-time DQ monitoring coverage
□ 5. Empower AI/ML with high-quality data

Resources: ___ FTE team, budget $____M
Milestone: end of M18, total ≥4.5 (Grade A), AI-training-grade data

============================================================================
```

---

## 8. Transportation Data-Quality Benchmarks

### 8.1 Benchmarks by Data Domain

| Data Domain | Industry Avg | Leading | Excellent | Quick Check |
|-------------|--------------|---------|-----------|-------------|
| Urban traffic-flow data | C (2.8) | B (3.8) | A (4.5+) | Detector online rate |
| Highway toll data | B (3.5) | A (4.2) | A (4.8) | Toll accuracy |
| Transit operations data | C (2.8) | B (3.8) | A (4.5) | GPS coverage |
| Taxi / ride-hail data | B (3.5) | A (4.2) | A (4.7) | Trajectory completeness |
| Traffic video / image | C (2.5) | B (3.5) | A (4.5) | Image usability |
| Parking data | C (2.8) | B (3.8) | A (4.5) | Space-detection accuracy |
| Crash data | D (2.0) | C (3.2) | B (4.0) | Location accuracy |
| Transport carbon data | D (2.0) | C (3.0) | B (3.8) | Emission-factor accuracy |
| Mobile-signaling OD | C (2.8) | B (3.5) | A (4.2) | OD validation deviation |
| Road-network GIS | B (3.5) | A (4.2) | A (4.7) | Network completeness |
| Signal-timing data | D (2.0) | C (3.2) | B (4.0) | Plan sync rate |

### 8.2 Data Quality vs. AI Model Effectiveness

| DQ Grade | AI Applications Supported | Expected Model Accuracy | Typical Effort | Notes |
|----------|---------------------------|-------------------------|---------------|-------|
| A (4.5+) | Full-scene AI, LLM training | ≥95% | Standard | Data no longer the bottleneck |
| B (3.5–4.4) | Main AI scenes, model fine-tuning | 88–95% | Medium | Targeted data augmentation needed |
| C (2.5–3.4) | Basic AI scenes, heavy cleaning | 75–88% | Higher | High AI data-prep cost |
| D (1.5–2.4) | Not recommended; govern first | <75% | Very high | Quality severely limits AI |
| E (<1.5) | Unsuitable for AI | - | - | Rebuild collection system |

---

## 9. Data-Quality Assessment Worksheet

```
============================================================================
            Transportation Data-Quality Assessment Worksheet
============================================================================

Object:____________________
Date:____________________
Assessor:____________________

==================================================================
PART A: Dimension Assessment
==================================================================

DQ1 Completeness (max 5)
  1. Flow completeness: ____% → score ____
  2. Vehicle GPS completeness: ____% → score ____
  3. Transit smart-card completeness: ____% → score ____
  4. Video online rate: ____% → score ____
  5. Other source completeness: ____% → score ____
  DQ1 avg = ____

DQ2 Accuracy (max 5)
  1. Detector flow accuracy: ____% → score ____
  2. Plate-recognition accuracy: ____% → score ____
  3. Travel-time accuracy: ____% → score ____
  4. Transit ETA accuracy: ____% → score ____
  5. Event detection (precision/recall): ____% → score ____
  DQ2 avg = ____

DQ3 Timeliness (max 5)
  1. Real-time control latency: ____ s → score ____
  2. Near-real-time latency: ____ min → score ____
  3. Batch latency: ____ h → score ____
  DQ3 avg = ____

DQ4 Consistency (max 5)
  1. Multi-source flow consistency: ____% → score ____
  2. Plate vs. toll consistency: ____% → score ____
  3. Transit OD vs. survey consistency: ____% → score ____
  DQ4 avg = ____

DQ5 Uniqueness (max 5)
  1. Event de-dup accuracy: ____% → score ____
  2. Vehicle-record duplicate rate: ____% → score ____
  DQ5 avg = ____

DQ6 Traceability (max 5)
  1. Lineage coverage: ____% → score ____
  2. Processing transparency: ____% → score ____
  DQ6 avg = ____

==================================================================
PART B: Composite Assessment
==================================================================

Weighted Total = DQ1×0.20 + DQ2×0.25 + DQ3×0.20 + DQ4×0.15 + DQ5×0.10 + DQ6×0.10
        = ____ + ____ + ____ + ____ + ____ + ____
        = ____

Grade: □ A (≥4.5) □ B (3.5–4.4) □ C (2.5–3.4) □ D (1.5–2.4) □ E (<1.5)

==================================================================
PART C: Key Findings & Recommendations
==================================================================

Top 3 quality issues:
  1. ________________________________________
  2. ________________________________________
  3. ________________________________________

Top 3 sources to improve:
  1. ________________________________________
  2. ________________________________________
  3. ________________________________________

Recommended actions (by priority):
  P0: ________________________________________
  P1: ________________________________________
  P2: ________________________________________

==================================================================
```

---

## 10. Usage Notes

1. **Define scope**: clarify data domains and sources to assess.
2. **Sample data**: follow Section 3 sampling strategy.
3. **Score dimensions**: use Section 2 criteria dimension by dimension.
4. **Classify issues**: use Section 4 classification system.
5. **Aggregate**: use Section 9 worksheet for total and grade.
6. **Set SLA**: reference Section 6 for a data-quality SLA.
7. **Build monitoring**: reference Section 5 for a monitoring dashboard.
8. **Plan roadmap**: reference Section 7 for an improvement roadmap.
9. **Re-assess periodically**: quarterly suggested; immediately after major changes.
