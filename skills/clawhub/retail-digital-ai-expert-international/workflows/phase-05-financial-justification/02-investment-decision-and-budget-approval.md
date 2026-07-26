# 02 — Investment Decision & Budget Approval

> **Trigger**: ROI justification completed; formal management approval needed
> **Deliverables**: Investment memo + management presentation + signed approval

---

## 1. Investment Memo Structure (10 pages max)

Template: see `templates/roi-and-business-case-template.md`

### Lean Version (for busy CEO / CFO, 3 pages)

```
Page 1: One-sentence summary + core metrics (investment / return / ROI / payback / cost of inaction)
Page 2: Where the money goes + where the money comes from
Page 3: Risk floor + what we need you to approve
```

---

## 2. Phased Budget Request

> Never request the full budget at once — phased requests reduce approval resistance

| Phase | Amount | Purpose | Approval Gate | Exit Condition |
|------|:---:|------|------|------|
| **Phase 1** | $[X]K | PoC / Pilot (1-3 stores) | Immediate approval | Pilot doesn't meet targets → stop or adjust |
| **Phase 2** | $[X]K | Batch rollout (30-50% of stores) | After pilot success | Results <80% of baseline → scale back |
| **Phase 3** | $[X]K | Full rollout (100% of stores) | After rollout success | — |

---

## 3. Management Communication Strategy

### 3.1 Key Concerns and Talking Points by Role

| Role | Most Concerned About | Communication Points | Avoid |
|------|------|------|------|
| **CEO** | Strategy, competition, ROI | "Competitors are already at [X]; we can catch up in [X] months" | Technical details |
| **CFO** | TCO, payback period, risk | "3-year spend of $[X]K, [X]-month payback; positive returns even in the pessimistic scenario" | Vague "efficiency gains" |
| **COO** | Operational impact, transition period | "We'll provide on-site support during cutover; store operations will not be disrupted" | Downplaying cutover risks |
| **CTO** | Technical feasibility, integration | "Integration with existing [X] system via API; integration risk is manageable" | Avoiding discussion of technical debt |

### 3.2 Common Objections & Responses

| Objection | Response |
|------|------|
| "It's too expensive" | "The cost of doing nothing is even higher — $[X]K in annual losses. Doing this delivers [X]% 3-year ROI" |
| "Can we get it cheaper?" | "We compared 3 vendors; this is the best value. Cutting [X] feature saves $[X]K but sacrifices [X]" |
| "Can we build it ourselves?" | "For under 200 stores, in-house build costs 5-10x more than buying. Better to invest where it counts" |
| "Let's wait and see" | "Every year of waiting costs $[X]K in efficiency losses + widening competitive gap. Wait until when?" |
| "We tried a system before and it failed" | "That failure was due to [X] (our research finding). This time we've specifically designed around that" |

---

## 4. Approval Process

```
Business Lead Approval → IT Lead Approval → CFO Approval → CEO / Board Approval
(Confirm need is real)  (Confirm tech feasible)  (Confirm financial soundness)  (Strategic decision)
```

### Approval Package Checklist

- [ ] Investment memo
- [ ] TCO detailed breakdown
- [ ] ROI calculation (three scenarios)
- [ ] Vendor selection report
- [ ] Risk assessment & mitigation
- [ ] Implementation plan summary
- [ ] Approval signature page

---

## 5. Common Pitfalls

1. **Requesting the full budget at once and getting rejected** → Use phased requests; Phase 1 only needs pilot funding
2. **ROI calculated too optimistically** → Use conservative estimates + three scenarios; only credible if pessimistic scenario is still positive
3. **Ignoring the CFO's risk concerns** → Proactively list TOP 5 risks with mitigation measures
4. **CEO says "yes" but CFO says "no budget"** → Pre-brief the CFO; don't let them be "surprised" in the meeting
