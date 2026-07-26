# Transportation LLM Scenario-Fit Assessment Tool

## Transportation LLM Scenario Readiness Assessment

---

## 1. Toolkit Overview

This tool provides an end-to-end evaluation framework for introducing and applying large language models (LLMs / LMMs) in the transportation sector. It covers data / compute / talent readiness, suitability scoring for nine transportation LLM scenarios, a model-selection decision tree, compute-resource estimation, fine-tuning strategy selection, an evaluation framework, cost-benefit analysis, and deployment-architecture guidance.

### Applicable Scenarios
- Transportation agencies assessing LLM feasibility
- Budgeting and business cases for transport LLM programs
- Model selection (general LLM vs. fine-tuned vs. in-house)
- Deployment-architecture decisions (cloud vs. on-prem vs. edge)

### Background

From 2023–2025, LLMs moved from proof-of-concept to production in transportation. Core sector demands include: domain knowledge Q&A, proposal/document generation, data analysis & visualization, intelligent customer service, and decision support. Unlike generic use, transport LLMs require high accuracy, domain knowledge, data security, and real-time assurance.

---

## 2. Transportation LLM Readiness (Data / Compute / Talent / Scenario)

### 2.1 Composite Readiness

| Dimension | Weight | Description | Score (1–5) | Weighted |
|-----------|--------|-------------|-------------|----------|
| Data readiness | 30% | Sufficient transport-domain data | | |
| Compute readiness | 20% | GPU / compute resources available | | |
| Talent readiness | 20% | AI / LLM talent available | | |
| Scenario readiness | 30% | Clear high-value use cases | | |
| **Total** | **100%** | | | **____** |

**Levels:**
- 4.0–5.0: High readiness — launch an LLM program directly
- 3.0–3.9: Medium readiness — close gaps before launch
- 2.0–2.9: Low readiness — build foundations & run a light pilot
- <2.0: Not ready — start with data governance & talent; observe

### 2.2 Data Readiness Detail

| Item | Score (1–5) | Notes |
|------|-------------|-------|
| Transport text (regs / standards / reports / proposals) | | GB-scale? TB-scale? |
| Transport structured data (flow / crash / ops) | | Standardized storage? |
| Transport image / video | | Labeled? |
| Data quality (completeness / accuracy / consistency) | | See Data Quality Assessment Tool |
| Format standardization | | LLM-friendly? |
| Privacy / compliance status | | Usage authorization? |
| Update frequency | | Continuously updated? |

### 2.3 Compute Readiness Detail

| Item | Score (1–5) | Notes |
|------|-------------|-------|
| GPU servers / accelerator count | | 0 / 1–8 / 16+ |
| GPU model | | T4 / A100 / H100 class |
| Total VRAM | | <80GB / 80–320GB / >320GB |
| Interconnect bandwidth | | NVLink / InfiniBand |
| Cloud AI-compute support | | Elastic GPU access? |
| Storage (NVMe / object) | | |

### 2.4 Talent Readiness Detail

| Item | Score (1–5) | Notes |
|------|-------------|-------|
| NLP / LLM algorithm engineers | | Quantity & quality |
| Data engineers (processing / labeling) | | |
| ML-platform engineers (MLOps / LLMOps) | | |
| Transport domain experts | | |
| Outsourcing / partner availability | | |

### 2.5 Scenario Readiness Detail

| Item | Score (1–5) | Notes |
|------|-------------|-------|
| High-value LLM scenarios identified | | |
| Business-unit acceptance & expectations | | |
| Clear business KPIs to measure | | |
| Management / executive support | | |
| Reference cases in the industry | | |

---

## 3. Nine Transportation LLM Scenario Suitability Scores

### 3.1 Scoring Dimensions

| Dimension | Description |
|-----------|-------------|
| Business value (1–5) | Value to core business |
| Technical feasibility (1–5) | Can current LLM tech deliver? |
| Data availability (1–5) | Ease of obtaining required data |
| Accuracy requirement (1–5) | Required model accuracy (lower = easier) |
| Risk controllability (1–5) | Risk & consequence of wrong output controllable? |

### 3.2 Nine-Scenario Scores

| Scenario | Biz Value | Feasibility | Data Avail. | Accuracy Req. | Risk Control | Weighted | Recommend |
|----------|-----------|-------------|-------------|---------------|--------------|---------|----------|
| 1. Transport regulation Q&A | 4 | 4 | 5 | 3 | 5 | 4.2 | ★★★ |
| 2. Proposal / report generation | 4 | 4 | 4 | 3 | 4 | 3.9 | ★★★ |
| 3. Data analysis & viz (Text2SQL) | 4 | 3 | 4 | 4 | 4 | 3.8 | ★★☆ |
| 4. Intelligent customer service | 4 | 5 | 4 | 2 | 4 | 3.9 | ★★★ |
| 5. Hotline / complaint handling | 3 | 4 | 4 | 3 | 4 | 3.6 | ★★☆ |
| 6. Incident summarization & analysis | 4 | 4 | 4 | 3 | 4 | 3.9 | ★★★ |
| 7. Contract / proposal review | 3 | 3 | 3 | 5 | 3 | 3.4 | ★★☆ |
| 8. Planning & design assistance | 5 | 2 | 2 | 5 | 2 | 3.1 | ★☆☆ |
| 9. Emergency decision support | 4 | 2 | 2 | 5 | 1 | 2.7 | ★☆☆ |

### 3.3 Scenario Detail

**Scenario 1: Transport Regulation Q&A**
- Users: transport managers, planners, enforcement staff
- Input: natural-language questions
- Output: clause citation + interpretation + applicability
- Core tech: RAG + regulation knowledge base
- Key data: transport regulations, standards, policy docs (10k-scale)
- Challenge: timely updates, terminology understanding
- Recommended: general LLM + RAG + regulation KB
- Quick start: build KB from top high-frequency questions

**Scenario 2: Proposal / Report Generation**
- Users: transport engineers, planners, PMs
- Input: requirements, data, templates
- Output: feasibility studies, technical proposals, summaries
- Core tech: LLM + template engine + RAG
- Key data: historical reports, case library, templates
- Challenge: high professionalism, formatting discipline
- Recommended: general LLM + fine-tuning + RAG

**Scenario 3: Data Analysis & Visualization (Text2SQL)**
- Users: analysts, managers
- Input: NL query ("today's top-10 congested intersections at AM peak")
- Output: table + chart + narrative
- Core tech: NL2SQL / Text2SQL + analytics agent
- Key data: operations DB schema, query history
- Challenge: complex-query accuracy, multi-table joins
- Recommended: NL2SQL specialist model + schema adaptation

**Scenario 4: Intelligent Customer Service**
- Users: citizens, drivers
- Input: trip inquiries, service requests, complaints
- Output: accurate, friendly, safe replies
- Core tech: LLM + KB + business-API
- Key data: chat history, process docs, FAQ
- Challenge: safety boundaries (no hallucination), multi-turn
- Recommended: general LLM + RAG + guardrails

**Scenario 5: Hotline / Complaint Handling**
- Users: hotline agents, managers
- Input: transcribed call text
- Output: classification, key extraction, disposition, auto-dispatch
- Core tech: LLM + NER + classification + workflow
- Key data: historical tickets, taxonomy, process
- Challenge: ASR quality, sentiment detection
- Recommended: general LLM + fine-tuning + ticket-system integration

**Scenario 6: Incident Summarization & Analysis**
- Users: command-center, managers
- Input: multi-source incident / congestion info
- Output: summary, impact analysis, disposition advice
- Core tech: LLM + fusion + knowledge graph
- Key data: incident, network, history
- Challenge: multi-source fusion, real-time
- Recommended: LLM + rules engine + real-time API

**Scenario 7: Contract / Proposal Review**
- Users: legal, procurement, PM
- Input: contracts / proposals / docs
- Output: compliance issues, risks, edit suggestions
- Core tech: LLM + legal KB + rules
- Key data: contract library, regulation library, rules
- Challenge: very high accuracy (95%+), legal consequence
- Recommended: LLM + fine-tuning + human review (not a replacement)

**Scenario 8: Planning & Design Assistance**
- Users: transport planners, designers
- Input: terrain / demand / conditions
- Output: design suggestions, option comparison, evaluation
- Core tech: LLM + CAD + simulation + multimodal
- Key data: design codes, history, cases
- Challenge: multimodal understanding, design logic
- Recommended: not pure-LLM short-term; human + AI collaboration

**Scenario 9: Emergency Decision Support**
- Users: emergency command
- Input: incident info
- Output: impact, resource dispatch, response plan
- Core tech: LLM + emergency KB + real-time data
- Key data: response plans, history, live situation
- Challenge: high accuracy + low latency + high reliability
- Recommended: rules + LLM hybrid, LLM as assistant (short-term)

---

## 4. Model-Selection Decision Tree

### 4.1 Selection Flow

```
          ┌── Need on-prem / private deployment?
          │
      ┌───┤
      │   └── Yes → Have GPU / compute?
      │              ├── Yes → Fine-tune open base model
      │              └── No → Acquire compute or use cloud API as bridge
      │
      └── No → Dependency on domain knowledge?
                 ├── High (needs expertise) → General LLM + RAG (KB augmentation)
                 │                            or General LLM + fine-tuning
                 ├── Medium (generic) → Call general LLM API directly
                 └── Low → Traditional NLP may be more economical
```

### 4.2 Strategy Comparison

| Strategy | General LLM API | General + Fine-tune | General + RAG | Train from Scratch |
|----------|-----------------|---------------------|---------------|--------------------|
| Accuracy | Medium | High | Med–High | Highest (theoretically) |
| Cost | Low | Med–High | Medium | Extremely high |
| Lead time | 1–2 wk | 1–3 mo | 2–8 wk | 6–18 mo |
| Compute | None | Medium | Low–Med | Extremely high |
| Data need | None | Domain (10k–100k) | KB text | Massive (TB) |
| Domain knowledge | Weak | Strong | Strong | Strongest |
| Flexibility | Medium | High | High | Highest |
| Maintenance | Low (API) | Medium | Medium | Extremely high |
| Best for | Generic CS, summarization | generation, expert QA | reg Q&A, retrieval | Not recommended |
| Rec. transport | Scenario 4 | 2/5/6 | 1/7 | Unsuitable |

### 4.3 Base-Model Reference (illustrative, as of 2025)

| Model | Params | Open / Commercial | Language | GPU Need | Fit |
|-------|--------|-------------------|----------|----------|-----|
| Open base (e.g., Llama 3 / Mistral) | 7B–70B | Open | ★★★★☆ | 1–4×A100 80G | Fine-tune + RAG |
| Commercial API (e.g., GPT-4o / Claude) | – | Commercial API | ★★★★★ | None | RAG / direct call |
| Regional cloud LLM | – | Commercial API | ★★★★☆ | None | RAG / local relevance |
| On-prem LLM suite | – | Commercial | ★★★★☆ | Vendor accelerators | Private deployment |

**Note:** The field evolves rapidly; select based on the latest benchmarks and actual PoC results.

---

## 5. Compute-Resource Estimation Calculator

> Cost figures below are indicative and use USD. Convert to local currency as needed (illustrative rate: 1 RMB ≈ $0.14).

### 5.1 Inference Estimate

| Deployment | Concurrency | Model Size | Recommended GPU | Est. Cost |
|------------|-------------|------------|-----------------|-----------|
| Pilot (<10) | 1–10 | 7B | 1×A100 40G or 1×RTX 4090 | $7k–21k |
| Medium (10–50) | 10–50 | 13B/14B | 2–4×A100 (40/80G) | $42k–112k |
| Medium (10–50) | 10–50 | 72B | 4–8×A100 80G | $112k–210k |
| Large (50–200) | 50–200 | 13B/14B | 8–16×A100 / H100 | $140k–280k |
| X-Large (200+) | 200+ | 72B | 16–32×H100 or cluster | $280k+ |
| Cloud API | Unlimited | – | Token-based | $0.07–0.70 / 1k calls |

### 5.2 Fine-Tuning Estimate

| Method | Model | Data | GPU Need | Est. Time | Est. Cost |
|--------|-------|------|----------|-----------|-----------|
| Full FT | 7B | 10k | 4×A100 80G | hours | a few $k |
| Full FT | 13B | 10k | 8×A100 80G | hours–1d | $1.4k–2.8k |
| Full FT | 72B | 10k | 16+×A100 80G | 1–3d | $7k–14k |
| LoRA/QLoRA | 7B | 10k | 1–2×A100 40G | hours | few $hundred–$k |
| LoRA/QLoRA | 13B | 10k | 1–2×A100 80G | hours | a few $k |
| LoRA/QLoRA | 72B | 10k | 4×A100 80G | hours–1d | $1.4k–2.8k |

### 5.3 Compute Cost Worksheet

```
============================================================================
           Compute-Resource Estimation Worksheet
============================================================================

[Scenario Parameters]
Target scenario:____________________
Est. daily calls: ____ / day
Avg input tokens: ____ / call
Avg output tokens: ____ / call
Peak QPS: ____
Response-time requirement: ____ s
Model size: □ 7B  □ 13B  □ 72B  □ Other ____

[Compute Estimate]

1. API mode (cloud):
   Monthly calls = ____ × 30 = ____
   Monthly tokens = ____ M tokens
   Monthly API cost = $____ (at $____ / M tokens)

2. Self-hosted inference:
   Recommended GPU config: ____
   Concurrency per server: ____
   Servers needed: ____
   Server capex: $____ × ____ = $____
   Annual power / ops: $____
   3-yr TCO: $____

[Comparison]
   API 3-yr TCO: $____
   Self-host 3-yr TCO: $____
   Recommend: □ API  □ Self-host  □ Hybrid (self-host + API fallback)

============================================================================
```

---

## 6. Fine-Tuning Strategy Guide

### 6.1 Strategy Comparison

| Strategy | Best For | Data Need | Pros | Cons | Rating |
|----------|----------|-----------|------|------|--------|
| Prompt Engineering | Quick validation, simple tasks | 0 | Zero cost, fast | Limited, token waste | ★★★★★ |
| RAG | KB Q&A, doc analysis | Doc corpus | Real-time, explainable | Retrieval quality bounds result | ★★★★★ |
| LoRA/QLoRA | Domain style adaptation | few k–tens k | Low cost, fast | Can't add new knowledge | ★★★★☆ |
| Full Fine-Tune | Deep domain adaptation | 10k–100k+ | Best result | Costly, forgetting | ★★★☆☆ |
| Pre-train + Fine-tune | Brand-new domain | TB-scale | Best ultimate | Extremely costly | ★☆☆☆☆ |

### 6.2 Transport Fine-Tuning Data Prep

| Data Type | Format | Min | Recommended | Source |
|-----------|--------|------|-------------|--------|
| QA pairs | instruction-response | 1000 | 5000–20000 | Expert + AI assisted |
| Text corpus | plain text | 100k docs | 1M+ docs | reports / standards / papers / news |
| Proposal docs | structured | 100 | 500–2000 | historical projects |
| Data tables | JSON / tables | 50 | 200+ | DB / data platform |
| Regs / standards | text / PDF | full | full (thousands) | official publications |

### 6.3 Fine-Tuning Quality Checklist

```
□ Train / val / test split (suggest 70:15:15)
□ Train and test data non-overlapping
□ Clear metrics (accuracy / recall / F1 / BLEU / ROUGE)
□ Baseline model evaluated
□ Compare vs. non-fine-tuned general LLM
□ Multiple checkpoints compared on val set
□ Human evaluation (≥50–100 samples)
□ Edge / error cases human-reviewed
□ Safety evaluation (harmful / policy-violating output)
□ Catastrophic-forgetting check (general ability retained)
```

---

## 7. Evaluation Framework (by Scenario)

### 7.1 General Dimensions

| Dimension | Metric | Description | Method |
|-----------|--------|-------------|--------|
| Accuracy | Answer correctness | Correct rate on domain Qs | Auto + human |
| Relevance | On-topic | Not answering beside the point | Human / similarity |
| Completeness | Coverage | Key info not missed | Human |
| Consistency | Repeated-answer consistency | Same question, stable answer | Auto |
| Safety | Harmful-output rate | Harmful / violating / infringing | Safety tool |
| Timeliness | Freshness | Not stale | Human |
| Efficiency | Time-to-first-token | User perceived wait | Measured |
| | Throughput (tokens/s) | Service capacity | Measured |

### 7.2 Scenario-Specific Focus

| Scenario | Core Metric | Min Acceptable | Target |
|----------|-------------|----------------|--------|
| Regulation Q&A | Accuracy | ≥90% | ≥98% |
| Proposal gen | Usable rate (minor edit) | ≥60% | ≥85% |
| Text2SQL | SQL exec correctness | ≥70% | ≥95% |
| Customer service | Satisfaction | ≥3.5/5 | ≥4.5/5 |
| Ticket handling | Classification accuracy | ≥85% | ≥95% |
| Incident summary | Key-info retention | ≥80% | ≥95% |
| Contract review | Risk detection rate | ≥85% | ≥98% |

---

## 8. Cost-Benefit Analysis Template

```
============================================================================
         Transportation LLM Cost-Benefit Analysis
============================================================================

Project:____________________
LLM scenario:____________________

==================================================================
[Cost Side]

One-time:
  GPU / servers: $____M
  Software / framework license: $____M
  Data collection / labeling: $____M
  Model fine-tuning / training: $____M
  System integration: $____M
  One-time subtotal: $____M

Annual operating:
  API / cloud: $____M / yr
  Power / IDC: $____M / yr
  Ops headcount: $____M / yr
  Continuous model optimization: $____M / yr
  Annual subtotal: $____M / yr

3-yr TCO: $____M

==================================================================
[Benefit Side]

Direct:
  Labor substitution/saving (__ FTE × $____k/yr): $____M/yr
  Efficiency gain (__% × labor cost): $____M/yr
  Direct subtotal: $____M/yr

Indirect:
  Service-quality uplift: $____M/yr (est.)
  Error / risk reduction: $____M/yr (est.)
  Innovation-business revenue: $____M/yr (est.)
  Indirect subtotal: $____M/yr

Annual total benefit: $____M/yr

==================================================================
[ROI]

3-yr total benefit: $____M
3-yr total cost: $____M
3-yr ROI: (benefit − cost)/cost ×100% = ____%
Payback: ____ yr
NPV (discount 8%): $____M

Conclusion: □ High  □ Medium  □ Low  □ Loss
============================================================================
```

---

## 9. Deployment-Architecture Decision Guide

### 9.1 Three/Four Deployment Modes

| Dimension | Cloud API | Private | Hybrid | Edge |
|-----------|-----------|---------|--------|------|
| Data security | Low (data leaves) | High | Med–High | High |
| Deploy cost | Low (pay-per-use) | High (capex) | Medium | Lower |
| Perf / latency | Med–High (network) | High | Controllable | Low latency |
| Flexibility | Low (API-bound) | High | High | Low (limited compute) |
| Ops complexity | Low | High | Med–High | Medium |
| Best for | Generic CS / text | reg Q&A / proposal / review | Mixed | Real-time control |
| Rec. scenario | 4 | 1/2/7 | 2/3/5/6 | 9 (assist) |

### 9.2 Deployment Decision Tree

```
          ┌── Can data go to cloud (compliant)?
          │
      ┌───┤
      │   └── Yes → Latency requirement?
      │              ├── Real-time (<100ms) → Edge / private
      │              ├── Near-real-time (1–5s) → Hybrid (local infer, API fallback)
      │              └── Offline / batch → Cloud API first
      │
      └── No → Budget sufficient?
                    ├── Yes (>$1.4M) → Private
                    └── No → Small edge / defer
```

### 9.3 Recommended Deployment by Scenario

| Scenario | Recommended | Rationale |
|----------|-------------|-----------|
| Reg Q&A (RAG) | Private / Hybrid | Sensitive regs, live KB updates |
| Proposal gen | Hybrid | Sensitive local, generic cloud |
| Text2SQL | Private | DB security, private schema |
| Customer service (public) | Cloud API | No sensitive data, elastic |
| Ticket handling | Hybrid | Partly sensitive, fast response |
| Incident summary | Private | Real-time, sensitive events |
| Contract review | Private | Trade secrets, max security |
| Planning assist | Hybrid | Generic cloud, expert local |
| Emergency advice | Private / Edge | High availability + low latency |

---

## 10. Quick-Start Roadmap

```
============================================================================
           Transportation LLM Launch Roadmap
============================================================================

Phase 1: Proof of Concept (1–3 mo, budget $14k–70k)
□ 1. Pick 1–2 high-value, low-risk scenarios for PoC (reg Q&A / CS suggested)
□ 2. Build prototype fast with cloud API
□ 3. Collect seed data (domain text / QA pairs)
□ 4. Build eval benchmark & set
□ 5. Internal trial & evaluation
□ 6. Summarize PoC, Go/No-Go decision
→ Milestone: PoC report, Go/No-Go

Phase 2: MVP (3–6 mo, budget $70k–280k)
□ 1. Set deployment arch (API / private / hybrid)
□ 2. Prepare high-quality fine-tuning data
□ 3. Stand up RAG knowledge base
□ 4. Fine-tune / adapt model
□ 5. Build guardrails
□ 6. Integrate with existing systems
□ 7. Internal gray-release
→ Milestone: MVP live, first-user feedback

Phase 3: Scale (6–12 mo)
□ 1. Expand to 3–5 scenarios
□ 2. Continuous optimization from feedback
□ 3. MLOps / LLMOps (auto-eval + continuous training)
□ 4. Scale compute (if self-hosted)
□ 5. Team build (part-time → dedicated LLM team)
□ 6. Establish LLM governance & standards
→ Milestone: 3+ scenarios stable, MAU >1000

============================================================================
```

---

## 11. Usage Notes

1. **Readiness**: use Section 2 to assess org LLM readiness.
2. **Scenario selection**: use Section 3 nine-scenario scores; pilot 1–2 high-feasibility.
3. **Model selection**: use Section 4 decision tree & comparison.
4. **Compute planning**: use Section 5 estimator for budget.
5. **Fine-tuning**: use Section 6 to choose method & prep data.
6. **Evaluation**: use Section 7 to set scenario metrics.
7. **Cost-benefit**: use Section 8 template for ROI.
8. **Deployment**: use Section 9 decision tree for architecture.
9. **Execution**: use Section 10 roadmap to plan delivery.
