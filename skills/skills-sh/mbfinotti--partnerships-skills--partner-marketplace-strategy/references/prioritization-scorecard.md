# Marketplace Prioritization: Hard Gates, Weighted Scorecard, Four-Way Outcome

Three passes, in order: screen hard gates, score survivors, filter by impact × effort. End each candidate at one of four outcomes - never a bare yes/no.

## Pass 1 - hard-gate screen (before any scoring)

Check binary blockers first. Scoring a disqualified candidate wastes the effort.

- Platform terms the business cannot accept (exclusivity, data, pricing-parity, IP clauses).
- A take rate or fee floor the gross margin cannot absorb.
- A prerequisite the company lacks with no budget to build (metering engineering, fulfilment capacity, required certifications).
- Buyer evidence absent: no target accounts procure there and no committed-spend or traffic signal.

Rule: never convert an unresolved question into a rejection or an acceptance. An unverified fee, an unclear compliance obligation, or an unknown committed-spend footprint sends the candidate to **hold for verification** with a named owner and source that would resolve it.

## Pass 2 - weighted scorecard

Propose weights, agree them with the user before scoring, and show the formula. Leave a dimension unscored when no evidence supports it: an unscored cell is honest. An invented score is not.

Starting dimension set (tune per engagement - weights below are a B2B illustration, not a standard):

| Dimension                       | Illustrative weight | What it measures                                                        |
| ------------------------------- | ------------------- | ----------------------------------------------------------------------- |
| Buyer procurement presence      | 25%                 | Committed spend or buying traffic of target accounts on this platform   |
| Strategic / ICP fit             | 15%                 | Does the platform own the buyer's workflow or category                  |
| Net economics                   | 15%                 | Take rate + cost-to-serve vs margin, at future rates                    |
| Operational cost to participate | 15%                 | Engineering, deal desk, tax/legal (B2B); fulfilment, returns, ads (B2C) |
| Competitive saturation          | 10%                 | Category crowding; whether differentiation is possible on-platform      |
| Co-sell / promotion access      | 10%                 | Field-seller incentives, featuring, retail-media leverage available     |
| Platform risk                   | 10%                 | Rate-change history, policy/algorithm volatility, dispute governance    |

Composite = Σ(score × weight) on a 1-5 scale. Weight buyer-procurement evidence heaviest by default: it is the single most predictive variable in both worlds, and the one teams most often replace with wishful demand assumptions.

### Worked example (B2B SaaS, ~$40k ACV, sales-led)

| Candidate               | Procurement 25%                                         | Fit 15% | Economics 15%                                        | Ops cost 15%                        | Saturation 10%         | Co-sell 10% | Risk 10% | Composite |
| ----------------------- | ------------------------------------------------------- | ------- | ---------------------------------------------------- | ----------------------------------- | ---------------------- | ----------- | -------- | --------- |
| Cloud marketplace A     | 4.5 (60% of target accounts hold committed spend there) | 4.0     | 4.5 (3% - SaaS listing, confirmed; falls on renewal) | 2.5 (metering + deal desk to build) | 3.5                    | 4.0         | 4.0      | **3.9**   |
| Workflow app store B    | 2.5 (buyers use it, don't buy software there)           | 4.5     | 2.5 (20% share, announced increase)                  | 3.5                                 | 2.0 (category crowded) | 3.0         | 2.5      | **3.0**   |
| Integration directory C | 1.5                                                     | 3.5     | 5.0 (free)                                           | 5.0                                 | 3.0                    | 1.5         | 4.0      | **3.2**   |

Reading: A wins on procurement evidence despite the heaviest build cost - the ops gap is the thing to fund, not a reason to pick C. C's high composite is cheapness, not opportunity: it earns a low-effort listing, never priority investment.

B goes to "prepare" or "hold" until the announced fee increase is modeled. The negative pattern this table exists to prevent: ranking by ease (C first) or by brand gravity (B first) instead of by where buyers already procure.

### Negative example - the list-and-pray scorecard

Same company, the way this goes wrong. This is the failure the skill's own body calls "the most-cited failure in both B2B and B2C", shown rather than named.

| Candidate               | Brand reach (25%) | Category size (25%) | Setup ease (25%) | Exec interest (25%) | Composite |
| ----------------------- | ----------------- | ------------------- | ---------------- | ------------------- | --------- |
| Workflow app store B    | 5                 | 5                   | 4                | 5                   | **4.75**  |
| Cloud marketplace A     | 3                 | 4                   | 2                | 3                   | **3.00**  |
| Integration directory C | 2                 | 2                   | 5                | 2                   | **2.75**  |

What is wrong, line by line:

- **No procurement dimension at all.** The single most predictive variable - whether target buyers already hold budget and a purchasing path on that platform - is absent, so the table cannot answer the question it was built for.
- **"Brand reach" and "category size" are demand assumptions wearing scorecard clothing.** A marketplace is a procurement rail. Neither column is evidence that anyone will find the listing, and together they are half the score.
- **Equal weights, no justification.** Nobody decided anything. The format decided.
- **No take-rate column, so no margin gate.** B is a 20% server-image listing with an announced increase. Here it wins.
- **"Setup ease" rewards the cheapest option** rather than costing the ops build honestly - the composite hides that A's 2.5 on ops is the thing to fund, not a reason to reject it.
- **"Exec interest" is the sponsored candidate scoring itself.**
- **No four-way outcome, no unscored cells, no delist trigger.** Everything is "go", ranked by charm.

The output looks rigorous and crowns the platform with the biggest logo and the worst economics. When a user brings a scorecard shaped like this, rebuild from the readiness gate and the demand-vs-procurement diagnosis rather than reweighting its columns.

## Pass 3 - second-pass filter

Plot scored candidates on impact × effort before committing sequence: expected revenue impact against total effort (engineering weeks, deal-desk rework, contractual commitment, coordination, reversibility). Never use the take rate as the effort axis: it is an input to impact, not a measure of work.

On the first pass the ROI model does not exist yet: plot a provisional impact estimate, label it as such, and leave a candidate unplotted rather than invent a number. Re-run the filter once the ROI model is built, and record any candidate that changed quadrant.

Order the quadrants by value per unit of effort, and say the order out loud rather than leaving it implied:

- efficiency: `high impact + low effort > high impact + high effort > low impact + low effort > low impact + high effort`

Each quadrant gets a different response:

- The first starts now.
- The second is staged behind gates.
- The third runs lean or waits.
- The fourth is declined regardless of composite score: delete it from the memo and name it, rather than ranking it last where it returns as scope.

The filter catches what a composite hides: a strong score driven by cheap dimensions.

That order starves the second quadrant, and the biggest procurement unlocks live there. Promote a high-impact/high-effort candidate above a cheaper one when the effort is a one-time build the company owns afterwards - metering, a deal desk, a tax registration - rather than a recurring cost, and when the user's stated effort ceiling covers it.

## Four-way outcome per candidate

- **Pilot** - evidence supports a limited, gated start now. Envelope and delist trigger attached.
- **Prepare** - promising, but named work (capability, policy, verification of one number) must finish before commitment.
- **Hold for verification** - an unknown (fee, compliance, procurement footprint) could change feasibility. Name the owner and the source that resolves it.
- **Do not prioritize** - weaker fit than alternatives. Record what would change the decision, so the ranking can be revisited without re-running the whole exercise.

Re-score on the memo's review cadence and on trigger events: an operator fee change, a platform policy shift, or new evidence of buyer procurement moving.
