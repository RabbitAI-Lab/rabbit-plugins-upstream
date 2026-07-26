# AI Scenario Identification & Prioritization Playbook

## Playbook Overview

| Item | Description |
|------|-------------|
| **Applicable scenarios** | Transport authorities / enterprises needing systematic AI-scenario identification, evaluation, and prioritization to form an AI implementation roadmap |
| **Core tool** | RICE++ transport-AI six-dimension priority scorecard (Reach / Impact / Confidence / Effort + Safety Impact + Policy Urgency) |
| **Scenario pool** | Covers 25+ transport AI scenarios (transport LLM / autonomous driving / V2X / AI signal control / smart maintenance / smart ports / smart airports / urban air mobility, etc.) |
| **Total duration** | 6–8 weeks |
| **Deliverables** | AI scenario long list / short list, RICE++ scores, Top-scenario business cases, AI implementation roadmap |
| **Assessment team** | 1 AI architect + 2 business analysts + 1 data engineer + 1 PM |

---

## Phase 1: AI Opportunity Scan (Weeks 1–2)

### 1.1 Opportunity-Scan Workshop Design

**Workshop preparation checklist:**

- [ ] Send invitations 2 weeks ahead (participants: business-unit heads, IT team, innovation / planning function)
- [ ] Prepare the 130-scenario checklist (attached in 1.3)
- [ ] Prepare a whiteboard / online whiteboard tool (Miro / Mural / FigJam)
- [ ] Prepare sticky notes (3 colors per person: green = AI opportunity, yellow = data need, red = risk concern)
- [ ] Book a full-day large meeting room (cannot be replaced by a 1-hour slot)

**Workshop agenda (full day, 6 hours):**

| Time | Segment | Duration | Content | Method |
|------|---------|----------|---------|--------|
| 09:00–09:30 | Opening & warm-up | 30 min | AI trend briefing (10-min transport-AI lightning talk) + rules | Deck + interaction |
| 09:30–10:30 | Divergent brainstorm | 60 min | "If you had an all-powerful AI, what business problem would you most want it to solve?" | Silent sticky method (5 min solo write → share → post on board) |
| 10:30–10:45 | Break | 15 min | | |
| 10:45–11:45 | Scenario checklist sweep | 60 min | Walk the 130-scenario list, fill gaps, quickly tag "possible / not-fit / already-have" | Full-group browse, vote per category |
| 11:45–12:00 | Scenario clustering | 15 min | Cluster sticky notes & list scenarios by business domain | Move stickies on board + name clusters |
| 12:00–13:30 | Lunch | 90 min | | |
| 13:30–14:30 | Initial vote | 60 min | Each person picks Top 3 scenarios per cluster (red-dot vote) | Dot voting (15 dots per person) |
| 14:30–15:00 | Merge & de-dup | 30 min | Merge similar scenarios, normalize naming | Group discussion + naming consensus |
| 15:00–15:15 | Break | 15 min | | |
| 15:15–16:15 | Initial priority | 60 min | Quick "impact vs feasibility" 2×2 matrix for the Top 20 | Collaborative matrix placement |
| 16:15–16:30 | Wrap-up & next steps | 15 min | Output long list (30–50 scenarios), assign data-research tasks | PM summary |

### 1.2 Brainstorming Techniques

**Technique 1: Silent brainstorming**
- Each person independently writes every AI application they can think of (5 min, at least 5)
- Each person reads their notes in turn and posts them on the board
- No commenting or challenging while others speak — post, don't question
- After posting, group and categorize collectively

**Technique 2: Pain-point reverse derivation**
- Each business unit lists its sharpest current pain ("spend 3 hours manually reviewing video daily")
- Convert each pain into an AI scenario using the frame "Can AI…?"
- Example: "3 hours daily manually reviewing video" → "Can AI auto-detect traffic incidents and alert?"

**Technique 3: AI-capability reverse derivation**
- List 10 mature AI capabilities (vision recognition / NLP / forecasting / optimization / generation / recommendation / anomaly detection / knowledge graph / reinforcement learning / multimodal)
- For each capability, ask: "Where can this be used in our business?"
- At least 3 scenario ideas per capability

**Technique 4: Benchmark stimulation**
- Show industry-benchmark AI applications (Singapore LTA / London TfL / Rotterdam Port AI / Waymo AV)
- After each case, ask: "Can we do this? What could we do better?"
- Spark the "we can too" mindset

### 1.3 Transport AI 130-Scenario Checklist (abridged)

> **For the full 130-scenario list, see SKILL.md Part 4. The themes below are for workshop filtering.**

| # | AI scenario theme | Modes covered | Typical value | Quick tag |
|---|-------------------|---------------|---------------|-----------|
| A01 | AI adaptive signal control | Urban roads | Cut congestion 15–25% | Possible / Not-fit / Have |
| A02 | AI automatic crash detection | Highway / urban | Cut response time 50%+ | |
| A03 | AI traffic-flow forecasting | All modes | Support guidance & dispatch | |
| A04 | AI video event analytics | All modes | 7×24 automated patrol | |
| A05 | AI plate / vehicle-type recognition | All modes | Foundational sensing | |
| A06 | Transport large language model (QA / reports) | All modes | Lower domain-expertise barrier | |
| A07 | AI automatic pavement-defect recognition | Highway / municipal | Cut maintenance cost 30% | |
| A08 | AI bridge / tunnel structural-health monitoring | Highway / rail | Preventive maintenance | |
| A09 | AI dynamic bus scheduling | Public transit | Lower empty-running rate | |
| A10 | AI metro passenger-flow forecasting | Urban rail | Optimize capacity allocation | |
| A11 | AI port container-dispatch optimization | Ports | Raise throughput efficiency | |
| A12 | AI airport A-CDM optimization | Aviation | Improve on-time performance | |
| A13 | Autonomous shuttle bus | Urban / campus | Last-mile connectivity | |
| A14 | V2X AI decision-making | Urban / highway | Safety & efficiency uplift | |
| A15 | AI driver-behavior analytics | Bus / logistics | Safety risk control | |
| A16 | AI carbon-emission monitoring & forecasting | All modes | Carbon-neutrality goals | |
| A17 | Low-altitude UAV AI traffic management | Urban air mobility | Core UTM capability | |
| A18 | AI multimodal route optimization | Logistics | Cost down, efficiency up | |
| A19 | AI parking-occupancy forecasting | Smart parking | Raise turnover | |
| A20 | AI sentiment / complaint intelligent classification | All modes | Improve public satisfaction | |
| ... | (scenarios continue numbering to S130) | | | |

**Quick-tag rules in the workshop:**
- **"Possible" (green):** Fits the organization and is technically feasible — into the long list
- **"Not-fit" (red):** Irrelevant to the business or technically infeasible — exclude
- **"Have" (blue):** Already deployed or under construction — into the long list but tagged "optimize" not "build"

### 1.4 Scenario Description Card Template

> **For each scenario entering the long list, fill one scenario description card:**

| Field | Content |
|-------|---------|
| Scenario ID | A03 |
| Scenario name | AI short-term traffic-flow forecasting |
| Business domain | Traffic control |
| Applicable modes | Urban roads / highways |
| Business pain | Current signal timing relies on historical data; cannot respond to real-time flow changes |
| AI capability | Time-series forecasting (LSTM / Transformer) |
| Input data | Detector / radar / video flow data (15-min granularity), weather, event calendar |
| Expected output | 15 / 30 / 60-min ahead flow forecast per direction (with confidence interval) |
| Expected value | Signal-timing accuracy +20%, travel delay −10% |
| Linked scenarios | A01 (AI adaptive signal control) — flow forecasting is its prerequisite |
| Preliminary implementation difficulty | Medium (data exists, model mature, but needs engineering rollout) |
| Current status | None |

---

## Phase 2: Data Readiness Assessment (Weeks 3–4)

### 2.1 Data Availability Checklist

> **For each shortlisted scenario, complete the following data checklist:**

| # | Check item | Options | Notes |
|---|------------|---------|-------|
| 1 | Does the required data exist in current systems? | Yes / Partial / No | "Partial" — note what's missing |
| 2 | Is the data electronic (not paper registers)? | Yes / Partial / No | Paper data must be digitized first |
| 3 | Is the data real-time / near-real-time? | Real-time / T+1 / Offline | T+1 = next day; Offline = irregular |
| 4 | Is the data format structured? | Structured / Semi / Unstructured | Unstructured (video / image / text) needs preprocessing |
| 5 | Is there a data dictionary / metadata description? | Complete / Partial / None | "None" means reverse-engineering the data |
| 6 | Is data collection continuous & stable? | Yes / Unstable / Stopped | Unstable = gaps; fix collection first |
| 7 | Is the data obtainable cross-department? | Yes / Needs coordination / Unobtainable | "Needs coordination" — note dept & difficulty |
| 8 | Does it involve privacy / security restrictions? | No / Masking manageable / Unusable | Unusable data equals no data even if it exists |
| 9 | Is historical volume sufficient for model training? | >1 yr / 6–12 mo / <6 mo | AI models usually need ≥1 full annual cycle |
| 10 | Do labels exist (supervised learning)? | Manual label / Auto label / None | No labels → labeling engineering first |

**Composite data-readiness score:**
- 2 points per item (Yes=2, Partial=1, No=0), max 20
- 15–20: Ready — start AI development directly
- 10–14: Partially ready — 1–3 months of data-engineering prep
- 5–9: Insufficient — 3–6 months of data-engineering build
- 0–4: Severely deficient — build data infrastructure first, defer the AI scenario

### 2.2 Quick Data-Quality Assessment

**Five quality dimensions (5-point scale):**

| Dimension | Meaning | Scoring |
|-----------|---------|---------|
| Completeness | Missing-data ratio | 5=<1% missing, 4=1–5%, 3=5–10%, 2=10–20%, 1=>20% |
| Accuracy | Consistency with reality | 5=validated, 4=user-confirmed accurate, 3=occasional issues, 2=known bias, 1=unreliable |
| Consistency | Contradiction across sources | 5=fully consistent, 4=occasional conflict (rule-resolved), 3=sometimes, 2=often, 1=unreconcilable |
| Timeliness | Delay to usability | 5=<1 sec, 4=<1 min, 3=<1 hr, 2=<1 day, 1=>1 day |
| Uniqueness | De-duplication | 5=auto, 4=periodic, 3=manual, 2=minor dup, 1=heavy dup |

**Quick data-quality example (A03 flow forecasting):**

| Source | Completeness | Accuracy | Consistency | Timeliness | Uniqueness | Avg | Status |
|--------|-------------|----------|-------------|------------|------------|-----|--------|
| Loop flow | 4 | 4 | 3 | 5 | 5 | 4.2 | Good |
| Radar flow | 3 | 4 | 3 | 5 | 5 | 4.0 | Good |
| Video flow | 5 | 3 | 3 | 4 | 5 | 4.0 | Good |
| Weather data | 5 | 5 | 5 | 5 | 5 | 5.0 | Excellent |
| Event calendar | 2 | 4 | 3 | 2 | 5 | 3.2 | Needs improvement |

### 2.3 Data Gap Analysis

**Gap-analysis template:**

| AI scenario | Required data | Current availability | Gap description | Remediation | Est. time | Est. cost |
|-------------|---------------|----------------------|----------------|-------------|-----------|-----------|
| A03 flow forecasting | Loop data | Available | - | - | - | - |
| | Weather data | Available | - | - | - | - |
| | Event data | Manual entry, incomplete | Build event-management system or interface from emergency services | Integrate emergency-services feed | 2 months | ~$30K |
| | Navigation data | Not obtained | Procure third-party or partner with TomTom / HERE | Commercial partnership | 1 month | ~$45K/yr |

---

## Phase 3: RICE++ Scoring Workshop (Week 5, Day 1)

### 3.1 The RICE++ Six-Dimension Model

> **Traditional RICE four dimensions: Reach, Impact, Confidence, Effort**
> **Transport augmentation two dimensions: Safety Impact, Policy Urgency**

| Dimension | Meaning | Scale | Anchor |
|-----------|---------|-------|--------|
| R-Reach | Volume of users / devices / coverage affected | 1–10 | 10=citywide all modes, 1=single intersection / device |
| I-Impact | Improvement to core KPIs | 1–10 | 10=>+50%, 1=<5% |
| C-Confidence | Confidence in technical feasibility | 1–10 (percent) | 10=100% certain, 5=50% sure |
| E-Effort | Required investment (person-months) | 1–10 (inverse) | 10=<10 person-months, 1=>500 person-months |
| S-Safety Impact | Positive impact on traffic safety | 1–10 | 10=directly reduces fatalities, 1=safety-irrelevant |
| P-Policy Urgency | Push from industry regulation / policy | 1–10 | 10=national hard mandate + deadline, 1=no regulatory driver |

**RICE++ composite score formula:**
```
RICE++ = (R × I × C) / E × (1 + S/10) × (1 + P/10)
```
Where:
- Safety Impact S and Policy Urgency P act as multipliers (not addends), ensuring high-safety / high-policy scenarios get a significant priority lift
- When S>7 or P>7, even if R×I/(C×E) is low, the scenario still gets a notable lift ("cannot-postpone" effect)

### 3.2 Scoring Workshop Execution

**Participants:** Core decision team (business head + IT head + AI expert + planning head)

**Pre-meeting prep:**
- [ ] Print one A4 scenario scorecard per scenario (scenario description + 6 scoring axes)
- [ ] Prepare 6-color stickies (one per dimension)
- [ ] 3 calibration scenarios (pre-scored, to align the scale)

**Agenda (6 hours):**

| Time | Segment | Content |
|------|---------|---------|
| 09:00–09:30 | Model explanation | Explain RICE++ definitions and anchors; each reads the definition card |
| 09:30–10:00 | Calibration exercise | 3 calibration scenarios scored independently → reveal reference answers → discuss divergence → reach scale consensus |
| 10:00–10:15 | Break | |
| 10:15–12:00 | Per-scenario scoring | 7 min each (2 min read card + 3 min independent score + 2 min short discussion) |
| 12:00–13:30 | Lunch | |
| 13:30–15:00 | Continue scoring | |
| 15:00–15:45 | Score computation & ranking | Enter Excel formula; auto-generate ranking |
| 15:45–16:15 | Sanity check | "Does this ranking look right? Any 'intuitively important' scenario ranked low?" |
| 16:15–17:00 | Final discussion | Adjust disputed scenarios; finalize ranking |

### 3.3 Calibration Exercise

**Standard calibration scenarios (reference answers pre-set):**

| Scenario | R | I | C | E | S | P | RICE++ | Expected rank | Difficulty |
|----------|---|---|---|---|---|---|---|--------|-----------|
| C01: AI adaptive signal control (new) | 8 | 7 | 7 | 4 | 8 | 6 | computed ref | Medium | Medium |
| C02: AI pavement-defect recognition (light) | 5 | 5 | 9 | 8 | 4 | 3 | computed ref | Medium | Low |
| C03: Transport LLM Q&A | 9 | 6 | 5 | 3 | 1 | 2 | computed ref | Medium | High |

**Calibration discussion prompts:**
1. "Why does C02 get E=8 (tiny effort) yet RICE++ trails C01?" → Reveal the multiplier effect of Safety Impact
2. "C03 has huge Reach but low Confidence — what does that mean?" → Reveal the balancing role of C (Confidence) in the formula
3. "If a scenario has S=9 but very low RICE, how to rank it?" → Safety red line — cannot postpone, but can be downgraded to "minimum viable solution first, for safety"

### 3.4 Common Scoring Biases & Corrections

| Bias | Symptom | Correction |
|------|---------|-----------|
| Optimism bias | Everyone over-rates C (Confidence), "LLMs aren't hard" | Require each person to list ≥1 "factor that could cause failure" before scoring |
| Scale inflation | R (Reach) scored "10 once live" | Clarify R = actual reachable scope at current stage, not long-term vision |
| Novelty preference | New-tech scenarios (UAM AI / digital twin) get emotional bonus | Stress RICE++ looks only at 6 dimensions, not "how cool" |
| Safety absolutism | Anything touching "safety" gets S=10 | Refine safety tiers: 10=directly reduces deaths, 7=reduces severe injury/crashes, 5=raises safety awareness, 3=safety data, 1=irrelevant |
| Budget protectionism | Dept heads over-rate their own projects | Cross-department anonymous scoring (business rates tech's scenarios, vice versa) |
| "No data, can't score" | "Our data is poor, C should be 1" | C = confidence in technical & organizational capability; data readiness already assessed in Phase 2, don't double-penalize |

### 3.5 The Ultimate Trap: "Everything is Priority 1"

**Symptom:** After ranking, the decision-maker says: "They're all important, all Priority 1"

**Three-step resolution:**

**Step 1: Acknowledge validity (1 min)**
> "Indeed, every AI scenario listed has value. Precisely because they all have value, we need prioritization — not whether to do them, but which first, which later."

**Step 2: Visualize the resource constraint (3 min)**
> On the board: "Our AI team over the next 12 months is X people, budget is $Y, we can run Z projects in parallel. Here are 30 scenarios; if we do all, each gets 1/30 of resources and none succeed. But if we concentrate on the top 5, each can be done well."

**Step 3: Return to the data (5 min)**
> "We spent 2 days evaluating all 6 dimensions of each scenario with RICE++. If you think the ranking is wrong, we can revisit a specific dimension of a few scenarios. But if we can't pin down which dimension is mis-scored, we respect the methodology's ranking."

**If the decision-maker still insists — ultimate method: phase it:**
> "We can do this: Phase 1 (0–6 mo) prioritizes the top 5; in parallel start data prep for ranks 6–10. Phase 2 (6–18 mo) promotes 6–10 to build once the top 5 show results. That way it's 'all done' yet sequenced."

---

## Phase 4: Business Case (Weeks 5–6)

### 4.1 Quick ROI Estimation

**Economic-value framework for transport-AI projects (triple-bottom-line method):**

| Benefit type | Elements | Quantified example |
|-------------|----------|--------------------|
| **Economic** | Lower O&M cost | Reduce manual inspectors X people × salary $Y = $Z/yr |
| | Efficiency / throughput gain | Travel-time efficiency +X% → time-value $Y/yr |
| | Loss reduction | Crashes −X × economic loss $Y each = $Z/yr |
| **Social** | Carbon reduction | CO2 −X t/yr → carbon-market value $Y/yr |
| | Public satisfaction | Complaints −X% / satisfaction +Y points |
| | Employment | X new high-skilled jobs |
| **Safety** | Fatalities reduction | −X fatalities/yr (priceless, but must be counted, especially for public-sector reporting) |
| | Emergency response time | Response −X min → severe-to-minor injuries −Y/yr |

**ROI quick formula:**
```
ROI = [(Economic benefit + monetized social benefit) / total investment cost] × 100%
Safety benefit listed separately (not mixed with money, but highlighted)
```

**ROI quick example — AI video event detection:**

| Item | Amount (USD/year) |
|------|-------------------|
| **Investment cost** | |
| AI video analytics platform (software + deployment) | $70K (one-time) |
| GPU servers (2) | $45K (one-time, 5-yr depreciation = $9K/yr) |
| O&M labor (0.5 FTE) | $15K |
| Annual license fee | $22K |
| **Annualized total investment** | $113K (yr1) / $46K (later yrs) |
| | |
| **Economic benefit** | |
| Reduce video patrol staff (3) | $65K |
| Shorter event detection → fewer secondary crashes | $45K |
| **Social benefit** | |
| Less congestion → time value | $75K |
| Carbon reduction | $7K |
| **Safety benefit** | |
| Estimated fatalities avoided via earlier detection | 1–2/yr (not monetized, but flagged) |
| | |
| **ROI (yr1)** | (65+45+75+7)/113 × 100% = 170% |
| **ROI (later yrs)** | (65+45+75+7)/46 × 100% = 420% |

### 4.2 Implementation Cost Estimation

**Cost-estimation framework:**

| Cost category | Detail | Method | Notes |
|--------------|--------|--------|-------|
| Hardware | GPU servers, cameras, edge-compute boxes | Vendor quote + industry benchmark | Reserve 30% GPU headroom |
| Software | AI-platform license, database, middleware | Quote + post-PoC confirmation | Watch concurrent-license vs usage-based pricing |
| Data engineering | Cleaning, labeling, pipelines | Internal/external labor × rate | Labeling is often a budget black hole — reserve ≥30% buffer |
| Model development | Algorithm R&D, training, tuning | Algorithm engineer person-month × rate | Transfer learning on pretrained models cuts 50–80% vs training from scratch |
| Integration | Interface with existing systems | Interface dev person-day × rate | Budget 5–10 person-days per system; more systems = higher cost |
| Training | User training, manuals | Trainer days × rate + materials | At least two tiers: admin and operator |
| O&M | Monitoring, upgrades, support | 15–20% of dev cost / yr | Usually included in yr1 project fee |
| Risk reserve | Contingency | 10–20% of total budget | AI projects need a higher reserve than traditional IT |

### 4.3 Value Proposition Authoring

**One-page value-proposition template per AI scenario:**

```
Scenario name: [AI adaptive signal control]
One-line value: [Use AI to optimize real-time signal timing across XX city intersections,
est. −20% travel delay, −XX t CO2/yr]

Key assumptions:
1. [Loop and enforcement-camera data quality meets requirements (verified, see 2.2)]
2. [Traffic engineers can support strategy validation]
3. [Signal system supports remote auto-push of timing plans]

Investment (3-yr TCO): $XX
3-yr cumulative benefit: $XX
3-yr ROI: XX%
Safety benefit: [Reduce traffic crashes from suboptimal signals by X/yr]

Risks & mitigation:
| Risk | Mitigation |
|------|------------|
| Data-quality fluctuation | Automated data-quality monitoring & alerting |
| Signal-system compatibility | Validate protocols of top-3 signal vendors in PoC |
| Traffic-engineering acceptance | Invite third-party transport research institute for before/after test |

Recommended decision: [Include in Phase 1 priority] / [Start after XX condition met]
```

---

## Phase 5: Roadmap & Recommendations (Weeks 7–8)

### 5.1 Phasing Logic

**Four-phase progression model:**

| Phase | Time | # scenarios | Inclusion criteria |
|-------|------|-------------|--------------------|
| Phase 1: Quick wins | 0–6 mo | 2–3 | RICE++ top 5 + E>6 (low effort) + C>7 (high confidence) |
| Phase 2: Capability build | 6–12 mo | 3–4 | RICE++ top 10 + needs some data/platform prep |
| Phase 3: Scale-out | 12–24 mo | 4–6 | On the success of Phases 1+2, extend AI to more scenarios & regions |
| Phase 4: Leading innovation | 24–36 mo | 2–3 | May rank lower on RICE++ but strategically significant (e.g., UAM AI, AV pilot zone) |

### 5.2 Quick Win Identification

**Four Quick-Win conditions:**
1. **Data ready** (data-readiness >15) — no large data-engineering build
2. **Low effort** (E>6, i.e., est. <50 person-months) — within budget headroom
3. **High visibility** (R>5, broad impact) — decision-makers can see and tell the story
4. **Short cycle** (MVP live within 3 months) — fast validation, fast confidence

**Typical Quick Wins — transport AI examples:**
- AI video event detection (add AI analytics module to existing video system)
- AI sentiment intelligent classification (interface citizen-contact-center / 511 traveler-info data)
- AI automatic pavement-defect recognition (add smart capture terminal to existing maintenance patrol vehicles)
- AI offline signal-timing optimization (not real-time control; recommend plans for engineer confirmation)

### 5.3 Investment Recommendation

**Investment-recommendation structure for decision-makers:**

| Section | Content | Suggested pages |
|---------|---------|-----------------|
| Strategic alignment | How these AI scenarios align with the org's strategic goals | 1 |
| Scenario portfolio | Phase 1–4 portfolio and logic | 2 |
| Investment summary | 3-yr total, per-year, per-scenario | 1 |
| Return expectation | 3-yr cumulative benefit, ROI, safety benefit | 1 |
| Capability build | Supporting org capabilities (AI team / platform / process) | 1 |
| Milestones | Key quarterly milestones & deliverables | 1 |
| Risks | Top risks & mitigation | 1 |
| Next steps | Recommended immediate actions (e.g., approve Phase 1 budget, start data prep) | 0.5 |

### 5.4 Common Implementation Roadmap Template

```
Month 1-2  │ Month 3-4  │ Month 5-6  │ Month 7-12 │ Month 13-18 │ Month 19-36
───────────┼────────────┼────────────┼────────────┼─────────────┼──────────────
 Data scan  │            │            │            │             │
   +        │  Quick Win │  Quick Win │            │             │
 AI platform│    #1      │    #2      │  Phase 2   │  Phase 3    │  Phase 4
 selection  │  dev+test  │  launch+iter│  scenario  │  scale-out  │  leading
 procurement│            │            │  cluster    │  cross-dept │  innovation
           │            │            │            │  rollout    │
 Team build │ Data       │ Effect     │ Platform   │ Cross-dept  │ External
 training   │ labeling   │ evaluation │ upgrade    │ promotion   │ output
            │ pipeline   │ reporting  │            │             │
```

---

## Appendix: RICE++ Scorecard Template

| Scenario ID | Scenario name | R-Reach (1–10) | I-Impact (1–10) | C-Confidence (1–10) | E-Effort (1–10) | S-Safety (1–10) | P-Policy (1–10) | RICE++ | Rank | Phase |
|-------------|---------------|------|------|------|------|------|------|--------|------|-------|
| A01 | AI signal control | 8 | 7 | 7 | 4 | 8 | 6 | computed | computed | 1 |
| A03 | Flow forecasting | 7 | 6 | 8 | 6 | 5 | 4 | computed | computed | 1 |
| A07 | Defect recognition | 5 | 5 | 9 | 8 | 4 | 3 | computed | computed | 1 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**RICE++ formula (Excel version):**
```
=(R cell × I cell × C cell / 100 / E cell) * (1 + S cell/10) * (1 + P cell/10)
```
(where C is entered as a percentage, e.g., 70% confidence → C=70)

---

> **Legal notice**: This playbook is protected under applicable copyright law. Without the author's written authorization, no commercial use is permitted (including resale, bundling, commercial training, or SaaS-ification).
> **Disclaimer**: The methodology herein is for learning reference only and does not constitute professional advice of any kind. AI-scenario investment decisions should rest on sufficient technical validation and business cases.
> **Author**: yinjianheng (Yin Jianheng) | yinjianheng@foxmail.com | WeChat: YJH-yinjianheng
