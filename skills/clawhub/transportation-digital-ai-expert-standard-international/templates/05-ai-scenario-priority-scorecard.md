# AI Scenario Priority Scorecard

> **Project Name:** [Organization] AI Application Scenario Prioritization
> **Authoring Team:** [Org name / AI working group]
> **Assessment Period:** [YYYY-MM — YYYY-MM]
> **Version:** V[X.X]

---

## Table of Contents

1. [AI Opportunity Landscape Scan](#1-ai-opportunity-landscape-scan)
2. [RICE++ Scoring Framework](#2-rice-scoring-framework)
3. [Individual Scenario Scorecards](#3-individual-scenario-scorecards)
4. [Composite Score Matrix](#4-composite-score-matrix)
5. [Prioritization & Decision](#5-prioritization--decision)
6. [Dependency Map](#6-dependency-map)
7. [Phased Implementation Path](#7-phased-implementation-path)
8. [Resource Estimate](#8-resource-estimate)
9. [Risk Assessment](#9-risk-assessment)
10. [Final Recommendation](#10-final-recommendation)
11. [Appendices](#11-appendices)

---

## 1. AI Opportunity Landscape Scan

### 1.1 Industry AI Trend

[Overview of the main trends and hot directions of AI application in transport today. 1–2 paragraphs.]

> **Example:** "In 2025, transport-sector AI shows three major trends: ① Large models (LLM / VLM) are accelerating penetration, extending from intelligent assistants to traffic-state analysis, regulation interpretation, and report generation; ② Multimodal perception fusion (vision + radar + audio) is rapidly maturing for incident detection and safety warning; ③ Digital twin + AI simulation is upgrading from 'perception' to 'decision.' Gartner predicts that by 2027, 60% of traffic management will incorporate AI-assisted decision-making."

### 1.2 AI Scenario Landscape

[Map all possible AI scenarios by business domain to form a panorama.]

| Business Domain | Perception AI | Prediction AI | Decision / Optimization AI | Generative AI | Interaction AI |
|-----------------|---------------|---------------|----------------------------|---------------|---------------|
| **Safety** | [Incident detection] [Fatigue detection] [Debris detection] | [Crash-risk prediction] [Blackspot ID] | [Emergency resource dispatch] | [Auto incident report] | [Safety alert push] |
| **Traffic Mgmt** | [Plate / vehicle-type ID] [Traffic param. capture] [Violation ID] | [Flow prediction] [Congestion warning] [OD prediction] | [Signal optimization] [Dynamic lane mgmt] [Area coordination] | [Daily ops report] | [Smart navigation] |
| **Maintenance** | [Pavement-defect ID] [Asset-damage detection] [Greenery monitoring] | [Pavement decay prediction] [Asset life prediction] | [Maintenance planning] [Resource scheduling] | [Maintenance report] [Defect description] | [Mobile inspection assistant] |
| **Toll Ops** | [Vehicle-type / plate AI audit] [Green-lane smart inspection] | [Toll-revenue prediction] [Evasion-risk prediction] | [ETC gantry optimization] | [Reconciliation report] | [Smart assistant] |
| **Mobility Service** | [Passenger-flow detection] [Crowding level] | [Demand prediction] [Peak prediction] | [Dynamic bus dispatch] [Ride-pooling match] | [Personalized rec.] [Trip summary] | [Voice assistant] [Sign-language translate] |
| **Hub / Station** | [Abnormal-behavior detection] [Left-item detection] [People / vehicle count] | [Crowd prediction] [Queue prediction] | [Security staffing] [Parking allocation] | [In-station voice guidance] | [Robotic kiosk] |
| **Enterprise Mgmt** | — | [Financial indicator prediction] | [Workforce optimization] | [Contract AI review] [Meeting minutes] [Smart BI Q&A] [Regulation Q&A] | [RPA automation] |
| **UAM / New** | [UAV inspection] [Low-altitude object detection] | [Conflict prediction] | [Route optimization] [Vertiport dispatch] | [Flight report] | — |

### 1.3 Scenario Collection Method

| Method | Description | # Scenarios |
|--------|-------------|-------------|
| Business interviews | [XX depts / XX persons] | [XX] |
| Brainstorm workshop | [XX sessions, XX participants] | [XX] |
| Benchmark research | [XX benchmark cases] | [XX] |
| Feasibility research | [XX AI vendors / institutes] | [XX] |
| **Total (deduplicated)** | — | **[XX]** |

---

## 2. RICE++ Scoring Framework

### 2.1 Framework Description

This scoring uses the **"RICE++"** extended framework, adding **"S — Strategy"** (strategic alignment) and **"D — Data Readiness"** (data readiness) — two dimensions critical to the transport sector — on top of classic RICE (Reach-Impact-Confidence-Effort).

**Formula:**

```
Priority score = (R × I × C × S × D) / E
```

| Code | Dimension | Weight Meaning | Note |
|------|-----------|----------------|------|
| **R** | Reach | Scope of impact | How many people / vehicles / km / stations affected |
| **I** | Impact | Value magnitude | Improvement in efficiency / safety / cost / experience |
| **C** | Confidence | Certainty | Confidence in technical feasibility + business support |
| **S** | Strategy | Strategic fit | Alignment with digital strategy and regulatory requirements |
| **D** | Data Readiness | Data foundation | Availability, quality, timeliness, compliance of required data |
| **E** | Effort | Investment cost | Composite of tech complexity + data engineering + org change |

### 2.2 Scoring Rubric per Dimension

#### R — Reach | 1–5

| Score | Standard | Transport Example |
|-------|----------|-------------------|
| 5 | Full / universal | Affects whole corridor / whole org / all public users |
| 4 | High coverage | Multiple major business lines / most corridors / most public |
| 3 | Medium coverage | Major part of one line / specific zone |
| 2 | Low coverage | 1–2 departments / specific scenario |
| 1 | Minimal | Only a few individuals / single pilot point |

#### I — Impact | 1–5

| Score | Standard | Transport Example |
|-------|----------|-------------------|
| 5 | Disruptive | Efficiency / safety / cost improvement > 30%, or annual benefit > [€XX M] |
| 4 | Significant | Improvement 15–30%, or annual benefit [€X–XX M] |
| 3 | Moderate | Improvement 5–15%, or annual benefit [€X–X M] |
| 2 | Marginal | Improvement < 5%, or annual benefit < [€X M] |
| 1 | Negligible | Only UX tweak |

#### C — Confidence | 1–5

| Score | Standard | Note |
|-------|----------|------|
| 5 | Very high | Mature tech with internal success / peer reference; strong business support |
| 4 | High | Mature tech, multiple industry successes; business support |
| 3 | Medium | Feasible but needs customization; business neutral |
| 2 | Low | Early tech, no mature industry case; business concerns |
| 1 | Very low | Still in lab; business resistance |

#### S — Strategy | 1–5

| Score | Standard | Note |
|-------|----------|------|
| 5 | Core strategy | Directly supports core strategic objective / hard regulatory requirement |
| 4 | Strong alignment | Supports important objective, not a hard requirement |
| 3 | Moderate alignment | Consistent with direction, not critical |
| 2 | Weak alignment | Low strategic relevance |
| 1 | Irrelevant | Unrelated / contrary |

#### D — Data Readiness | 1–5

| Score | Standard | Note |
|-------|----------|------|
| 5 | Ready | Data already collected, quality met (completeness >90%, accuracy >95%) |
| 4 | Mostly ready | Most data exists, little supplement / cleaning needed (quality >80%) |
| 3 | Partly ready | Some data exists, substantial collection / governance needed (quality >60%) |
| 2 | Low readiness | Mostly missing, new collection system needed |
| 1 | No data | No foundation, build from zero |

#### E — Effort | 1–5

| Score | Standard | Note |
|-------|----------|------|
| 1 | Very low | < [€XX M], < [X] mo, small adjustment by existing team |
| 2 | Low | [€XX–XXX M], [X] mo, little external support |
| 3 | Medium | [€XXX–XXX M], [X] mo, dedicated project team |
| 4 | High | [€XXX–XXXX M], [X] mo, large program management |
| 5 | Very high | > [€XXXX M], > [X] mo, organization-level change |

---

## 3. Individual Scenario Scorecards

> **Note:** Templates for 25 predefined transport AI scenarios below. Add / remove scenarios per your organization. Each scenario needs score + rationale.

---

### Scenario 01: [Automatic Traffic Incident Detection]

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **R — Reach** | [X] | [Basis: covers XX km / XX cameras / XXk veh/day] |
| **I — Impact** | [X] | [Basis: detection time from XX min to XX sec] |
| **C — Confidence** | [X] | [Basis: mature (CV + Transformer), >100 industry cases] |
| **S — Strategy** | [X] | [Basis: safety KPI mandate, #1 safety program] |
| **D — Data Readiness** | [X] | [Basis: XX video streams, XXk labeled images] |
| **E — Effort** | [X] | [Basis: X GPUs, X pm algorithm team] |
| **RICE++ score** | **[X.X]** | (R×I×C×S×D)/E |
| **Priority** | [P0/P1/P2] | [Reason] |
| **Est. investment** | [€XXX M] | [HW XX + dev XX + labeling XX] |
| **Est. duration** | [X] mo | — |
| **Data needs** | [Video stream + labels] | [See data-needs assessment] |
| **Dependencies** | [Video stream connected to AI platform] | — |

---

### Scenario 02: [Traffic-Flow Prediction & Congestion Warning]

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **R** | [X] | [Basis] |
| **I** | [X] | [Basis] |
| **C** | [X] | [Basis] |
| **S** | [X] | [Basis] |
| **D** | [X] | [Basis] |
| **E** | [X] | [Basis] |
| **RICE++ score** | **[X.X]** | |
| **Priority** | [P0/P1/P2] | |

---

### Scenario 03: [AI Pavement-Defect Recognition]

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **R** | [X] | [Basis] |
| **I** | [X] | [Basis] |
| **C** | [X] | [Basis] |
| **S** | [X] | [Basis] |
| **D** | [X] | [Basis] |
| **E** | [X] | [Basis] |
| **RICE++ score** | **[X.X]** | |
| **Priority** | [P0/P1/P2] | |

---

### Scenario 04: [AI Signal-Control Optimization]

[Same format as above]

### Scenario 05: [AI-Assisted Toll Compliance Audit]

[Same format as above]

### Scenario 06: [Intelligent Assistant (LLM)]

[Same format as above]

### Scenario 07: [Driver Fatigue / Distraction Detection]

[Same format as above]

### Scenario 08: [Bridge / Tunnel Structural-Health Anomaly Detection]

[Same format as above]

### Scenario 09: [Severe-Weather AI Early Warning]

[Same format as above]

### Scenario 10: [Intelligent Maintenance Scheduling Optimization]

[Same format as above]

### Scenario 11: [Intelligent Emergency-Resource Dispatch]

[Same format as above]

### Scenario 12: [Digital-Twin Traffic Simulation]

[Same format as above]

### Scenario 13: [Travel-Demand Prediction & Dynamic Dispatch]

[Same format as above]

### Scenario 14: [Abnormal Driving Behavior Detection (speeding / wrong-way / emergency-lane misuse)]

[Same format as above]

### Scenario 15: [Passenger / Freight Safety-Risk Prediction]

[Same format as above]

### Scenario 16: [Intelligent BI & Management-Analytics Q&A]

[Same format as above]

### Scenario 17: [AI Contract / Procurement-Document Review]

[Same format as above]

### Scenario 18: [Tunnel Fire / Smoke AI Early Detection]

[Same format as above]

### Scenario 19: [Road Debris / Falling-Object Detection]

[Same format as above]

### Scenario 20: [Parking-Space AI Guidance & Prediction]

[Same format as above]

### Scenario 21: [UAV Bridge / Slope AI Inspection]

[Same format as above]

### Scenario 22: [Exempt-Commodity (Green-Lane) Vehicle Intelligent Inspection]

[Same format as above]

### Scenario 23: [Transport Regulation / Policy Intelligent Q&A (KB + LLM)]

[Same format as above]

### Scenario 24: [Construction-Site Safety AI Monitoring (helmet / fencing / lifting)]

[Same format as above]

### Scenario 25: [ETC Gantry Data AI Imputation & Anomaly Detection]

[Same format as above]

---

## 4. Composite Score Matrix

### 4.1 All-Scenario Score Summary

| ID | Scenario | R(1-5) | I(1-5) | C(1-5) | S(1-5) | D(1-5) | E(1-5) | **Score** | **Rank** | **Priority** |
|----|---------|--------|--------|--------|--------|--------|--------|-----------|----------|--------------|
| 01 | Automatic Traffic Incident Detection | [X] | [X] | [X] | [X] | [X] | [X] | [X.X] | [X] | [P0/P1/P2] |
| 02 | Traffic-Flow Prediction & Congestion Warning | [X] | [X] | [X] | [X] | [X] | [X] | [X.X] | [X] | [P0/P1/P2] |
| 03 | AI Pavement-Defect Recognition | [X] | [X] | [X] | [X] | [X] | [X] | [X.X] | [X] | [P0/P1/P2] |
| 04 | AI Signal-Control Optimization | [X] | [X] | [X] | [X] | [X] | [X] | [X.X] | [X] | [P0/P1/P2] |
| 05 | AI-Assisted Toll Compliance Audit | [X] | [X] | [X] | [X] | [X] | [X] | [X.X] | [X] | [P0/P1/P2] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 25 | ETC Gantry Data AI Imputation | [X] | [X] | [X] | [X] | [X] | [X] | [X.X] | [X] | [P0/P1/P2] |

### 4.2 Visualization Priority Matrix

```
Impact (I)
  High │  ★ P1 (long-term strategic)    ★★ P0 (launch now)
       │  High impact, hard / low data      High impact, data ready, high confidence
       │
       │  ○ P3 (watch & wait)           ● P2 (opportunistic)
  Low  │  Low impact, hard / low data       Low impact, easy to do
       └────────────────────────────────────
          Low        Effort (E)        High
```

[Map the 25 scenarios into the four quadrants above, annotate IDs.]

**P0 quadrant (launch now):** [Scenarios 01, 05, …]
**P1 quadrant (long-term strategic):** [Scenarios 02, 04, …]
**P2 quadrant (opportunistic):** [Scenarios 06, …]
**P3 quadrant (watch & wait):** [Scenarios 15, …]

---

## 5. Prioritization & Decision

### 5.1 Recommended Priority

#### P0 — Launch Immediately (Batch 1, Y1Q1–Q2)

| Rank | ID | Scenario | Score | Rationale |
|------|----|---------|-------|-----------|
| 1 | [01] | [Name] | [X.X] | [Reason] |
| 2 | [05] | [Name] | [X.X] | [Reason] |
| 3 | [19] | [Name] | [X.X] | [Reason] |
| 4 | [...] | [...] | [...] | [...] |
| 5 | [...] | [...] | [...] | [...] |

#### P1 — Key Push (Batch 2, Y1Q3–Y2Q2)

| Rank | ID | Scenario | Score | Prerequisite |
|------|----|---------|-------|--------------|
| 6 | [02] | [Name] | [X.X] | [Need data-platform XX module] |
| 7 | [04] | [Name] | [X.X] | [Need signal system upgrade] |
| ... | ... | ... | ... | ... |

#### P2 — Opportunistic (Batch 3, Y2Q3–Y3Q2)

| Rank | ID | Scenario | Score | Condition |
|------|----|---------|-------|-----------|
| [...] | [...] | [...] | [...] | [...] |

#### P3 — Watch & Track (not started; monitor industry)

| Rank | ID | Scenario | Score | Watch Indicators |
|------|----|---------|-------|------------------|
| [...] | [...] | [...] | [...] | [Tech maturity / cases / ROI] |

### 5.2 Priority Decision Log

| Decision Item | Conclusion | Basis | Decider | Date |
|---------------|-----------|-------|---------|------|
| P0 list confirmed | [List] | [Basis] | [XXX] | [Date] |
| XX scenario downgraded | [P1 → P2] | [Reason] | [XXX] | [Date] |
| XX scenario vetoed | [Not done] | [Reason] | [XXX] | [Date] |

---

## 6. Dependency Map

### 6.1 Scenario Dependency Matrix

| Scenario | Data Platform Dep. | AI Capability Dep. | HW / Infra Dep. | Predecessor |
|---------|--------------------|--------------------|-----------------|-------------|
| 01-Incident | Video ingest platform | Detection / tracking model | GPU + video gateway | — |
| 02-Flow | Traffic-flow DB | Time-series model | — | Data platform |
| 03-Defect | Inspection image store | CV classification / segmentation | Inspection capture terminal | — |
| 04-Signal | Real-time traffic data | RL / optimization | Signal-system API | 02-Flow |
| 05-Toll audit | ETC gantry + toll data | Anomaly model | — | Data platform |
| ... | ... | ... | ... | ... |

### 6.2 Dependency Diagram (text)

```
[AI platform infra (GPU cluster + MLOps + labeling platform)]
    │
    ├──► [Data Platform V1.0]
    │       │
    │       ├──► 01-Incident (P0) ──── independent go-live
    │       ├──► 02-Flow (P1) ──────── independent go-live
    │       │       │
    │       │       └──► 04-Signal (P1) ── depends on 02
    │       ├──► 03-Defect (P0) ─────── independent go-live
    │       ├──► 05-Toll audit (P0) ── independent go-live
    │       │
    │       └──► 06-Assistant (P2) ── independent go-live
    │
    └──► [LLM Platform]
            │
            ├──► 23-Regulation Q&A (P1)
            └──► 16-BI Q&A (P2)
```

### 6.3 Capability Reuse Plan

| Shared AI Capability | Serves Scenarios | Build Note |
|----------------------|------------------|------------|
| **CV detection / tracking engine** | 01, 03, 07, 14, 18, 19, 24 | **Build once, reuse many** |
| **Time-series prediction engine** | 02, 06, 09, 15 | **Unified time-series platform** |
| **NLP / LLM engine** | 06, 16, 17, 23 | **Unified LLM platform** |
| **Optimization engine** | 04, 10, 11, 13 | **Accumulate optimization algorithm library** |
| **Anomaly-detection engine** | 05, 08, 20 | **Unified anomaly framework** |
| **Data labeling platform** | All CV scenarios | **Build once, operate long-term** |

---

## 7. Phased Implementation Path

### 7.1 Three-Phase Overview

| Phase | Period | Objective | # Scenarios | Investment |
|-------|--------|-----------|-------------|------------|
| **Phase 1: Pilot breakthrough** | [Y1Q1–Y1Q4] | Pick 3–5 high-value, easy scenarios for quick delivery; build confidence | [X] | [€XXX M] |
| **Phase 2: Scale-out** | [Y2Q1–Y2Q4] | Expand to [X] scenarios; build shared AI capability platform | [X] | [€XXX M] |
| **Phase 3: Deep integration** | [Y3Q1–Y3Q4] | Embed AI in core processes; form data-algorithm-business loop | [X] | [€XXX M] |

### 7.2 Phase 1 Detail

| Scenario | Period | Milestone | KPI |
|---------|--------|-----------|-----|
| [01-Incident] | [Y1Q1–Y1Q2] | [PoC → pilot → full rollout] | [Recall >95% / precision >90%] |
| [03-Defect] | [Y1Q1–Y1Q3] | [Train → inspection-vehicle pilot → app integration] | [Defect precision >85%] |
| [05-Toll audit] | [Y1Q2–Y1Q3] | [Aggregate → model → live audit] | [Evasion detection +XX%] |
| [19-Debris] | [Y1Q2–Y1Q4] | [Shared CV engine with 01, incremental] | [Debris detection >90%] |

### 7.3 Phase 2 Detail

| Scenario | Predep | Period | KPI |
|---------|-------|--------|-----|
| [...] | [...] | [...] | [...] |

### 7.4 Phase 3 Detail

| Scenario | Predep | Period | KPI |
|---------|-------|--------|-----|
| [...] | [...] | [...] | [...] |

---

## 8. Resource Estimate

### 8.1 Overall Resource Needs

| Category | Phase 1 | Phase 2 | Phase 3 | Total |
|----------|---------|---------|---------|-------|
| **HW / infra (€M)** | [XXX] | [XXX] | [XXX] | [XXX] |
| — GPU / NPU server | [X] / [€XXX M] | [X] / [€XXX M] | [X] / [€XXX M] | [€XXX M] |
| — Storage / network | [€XX M] | [€XX M] | [€XX M] | [€XX M] |
| **SW / platform (€M)** | [XXX] | [XXX] | [XXX] | [XXX] |
| — MLOps / AI platform | [€XXX M] | — | — | [€XXX M] |
| — LLM platform | — | [€XXX M] | — | [€XXX M] |
| — Labeling platform | [€XX M] | [€XX M] | — | [€XX M] |
| **People (pm)** | [XX] | [XX] | [XX] | [XX] |
| — AI algorithm eng. | [X] | [X] | [X] | — |
| — AI product mgr | [X] | [X] | [X] | — |
| — Data eng. | [X] | [X] | [X] | — |
| — Labeling / ops | [X] | [X] | [X] | — |
| **External (€M)** | [XXX] | [XXX] | [XXX] | [XXX] |
| — Algorithm R&D partner | [€XX M] | [€XX M] | [€XX M] | [€XX M] |
| — Labeling outsourcing | [€XX M] | [€XX M] | [€XX M] | [€XX M] |
| — Consulting | [€XX M] | [€XX M] | [€XX M] | [€XX M] |
| **Total** | **[€XXXX M]** | **[€XXXX M]** | **[€XXXX M]** | **[€XXXX M]** |

### 8.2 Team-Build Roadmap

| Role | Y1Q1 | Y1Q3 | Y2Q1 | Y2Q3 | Y3 |
|------|------|------|------|------|-----|
| AI lead | 1 | 1 | 1 | 1 | 1 |
| Algorithm eng. (CV) | 2 | 3 | 4 | 4 | 5 |
| Algorithm eng. (NLP/LLM) | — | 1 | 2 | 3 | 4 |
| Algorithm eng. (TS/OR) | 1 | 1 | 2 | 2 | 3 |
| ML / data eng. | 1 | 2 | 3 | 3 | 4 |
| AI product mgr | 1 | 1 | 2 | 2 | 2 |
| Labeling / ops | 2 (outsourced) | 3 | 4 | 4 | 4 |
| **Total** | **8** | **12** | **18** | **19** | **23** |

---

## 9. Risk Assessment

### 9.1 AI-Specific Risk Register

| ID | Category | Description | Affected | Likelihood | Impact | Mitigation | Owner |
|----|----------|-------------|----------|------------|--------|------------|-------|
| RA1 | Data | Poor labeling quality → inaccurate model | 01,03,14 | High | Med | Labeling QA process, multi-round review | [AI lead] |
| RA2 | Data | Training/serving distribution drift | 01,02,05 | Med | High | Online monitoring + periodic retrain | [ML eng] |
| RA3 | Algorithm | Model accuracy below target | All | Med | High | Tech gate (mAP >XX%), PoC first | [Algorithm lead] |
| RA4 | Engineering | Inference latency fails real-time | 01,07 | Med | Med | Quantization / pruning, GPU, edge-cloud | [Eng lead] |
| RA5 | Compliance | AI ethics / privacy (face / plate data) | 01,07,14 | Low | High | Privacy computing / masking / review / registration | [Legal / AI] |
| RA6 | Talent | Hard to hire / retain AI talent | All | High | High | Market pay + university tie-up + internal build | [HR / AI] |
| RA7 | Business | AI output not adopted by business | 04,06,10 | Med | Med | Business co-ownership, quick-win demo, KPI tie | [AI PM] |
| RA8 | Ethics | AI bias / discrimination (e.g., unfair signal) | 04 | Low | Med | Fairness assessment, explainability report | [AI lead] |

### 9.2 AI Ethics & Compliance Checklist

| Item | Status | Note |
|------|--------|------|
| Face / plate data processing compliant (GDPR / NIS2 / AI Act) | [✅/❌/⚠️] | [Note] |
| AI on high-impact decisions requires registration (EU AI Act) | [✅/❌/⚠️] | [Note] |
| Algorithm fairness review process in place | [✅/❌/⚠️] | [Note] |
| AI decisions explainable / traceable | [✅/❌/⚠️] | [Note] |
| AI security testing (adversarial / backdoor) done | [✅/❌/⚠️] | [Note] |
| Human-in-the-loop / fallback mechanism in place | [✅/❌/⚠️] | [Note] |

---

## 10. Final Recommendation

### 10.1 Recommended Action Plan

1. **Launch P0 scenarios (X) now:** [scenario names], total ~[€XXX M], results by [Y1Q2].
2. **Build shared AI capabilities in parallel:** [CV engine / time-series platform / MLOps] to reuse for later scenarios.
3. **Hire AI core team ASAP:** at least AI lead + 2 algorithm engineers + 1 ML engineer first.
4. **Start data prep:** labeling for P0 scenarios now; involve domain experts in rule definition.
5. **Establish AI governance:** form AI ethics committee; publish AI usage policy.

### 10.2 What If We Do Nothing?

[Consequences short-term (1 yr) and long-term (3 yr) if AI scenarios are not invested in.]

### 10.3 Next Steps

| No. | Action | Owner | Due |
|-----|--------|-------|-----|
| 1 | [P0 scenario kickoff approval] | [XXX] | [Date] |
| 2 | [AI platform tech selection] | [XXX] | [Date] |
| 3 | [Algorithm team hiring start] | [HR] | [Date] |
| 4 | [Labeling needs scoping] | [Business + AI] | [Date] |
| 5 | [AI ethics policy draft] | [Legal] | [Date] |

---

## 11. Appendices

### Appendix A: Scenario Scoring Workshop Log

| Session | Date | Attendees | Depts | Output |
|---------|------|-----------|-------|--------|
| [1] | [Date] | [XX] | [XX dept] | [Long list XX scenarios] |
| [2] | [Date] | [XX] | [XX dept] | [Scoring + priority discussion] |
| [3] | [Date] | [XX] | [XX dept] | [Final priority confirmation] |

### Appendix B: Industry AI Benchmark Reference

| AI Scenario | Leading Practice | Typical Effect | Source |
|------------|------------------|----------------|--------|
| Incident detection | [XX motorway / XX solution] | [Effect data] | [Source] |
| ... | ... | ... | ... |

### Appendix C: Glossary

| Term | Note |
|------|------|
| RICE | Reach-Impact-Confidence-Effort prioritization framework |
| MLOps | Machine Learning Operations |
| mAP | mean Average Precision (object-detection metric) |
| Data Drift | Shift in data distribution |
| Human-in-the-loop | Human-machine collaborative decision |
| LLM / VLM | Large Language Model / Vision-Language Model |
| PoC | Proof of Concept |

### Appendix D: RICE++ Score Formula Detail

```
Priority score = (R × I × C × S × D) / E

Where:
- Score range: theoretically 0.2 — 3125
- Typical range: 1 — 500
- P0 (launch now) threshold: > 100
- P1 (key push) threshold: 30 — 100
- P2 (opportunistic) threshold: 10 — 30
- P3 (watch & wait) threshold: < 10
```

---

> **Prepared by:** [AI working group / Digital Transformation Office]
> **Reviewed by:** [CDO / CTO]
> **Approved by:** [Digital Transformation Steering Committee]
>
> **Version history:**
> | Version | Date | Change | Author |
> |---------|------|--------|--------|
> | V1.0 | [YYYY-MM-DD] | First draft, 25 scenarios scored | [Name] |
