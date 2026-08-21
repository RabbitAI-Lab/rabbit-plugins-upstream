# Rate Theory — The Economics of Not Going Broke Busy

## Why Freelancers Underprice: The Four Hidden Costs

### 1. The billable ratio

A freelancer's week: client work, but also proposals (unpaid), invoicing and
chasing payments (unpaid), taxes/bookkeeping (unpaid), learning new tools
(unpaid), sales calls (unpaid, and lots of them early on).

Industry benchmarks for billable ratio:

| Situation | Typical billable ratio |
|---|---|
| New freelancer (still building pipeline) | 40–50% |
| Established, mostly repeat clients | 60–70% |
| Agency with dedicated sales staff | 70–80% |
| Solo consultant who also sells | 50–65% |

Default in this tool: **60%**. If you're new, use 0.50 — the lower ratio is
the cost of building the pipeline that doesn't exist yet.

### 2. Self-employment tax

Employees pay 7.65% FICA and the employer matches it. Freelancers pay both
halves: 15.3% SECA on 92.35% of net earnings (the 7.65%-equivalent deduction
is folded in). Effective ≈ 14.1%. On top of income tax.

The tool's keep-ratio: `1 − income_tax − 0.153 × 0.9235`.
With 18% income tax: **67.9% of revenue is yours**. On a $100 invoice,
$32 disappears before your mortgage does.

### 3. Self-funded benefits

The employee's hidden paycheck: health insurance (employer average
contribution $6–8k/yr for single coverage, $13–20k family), retirement match
(3–6%), paid leave (which is your bench time), life/disability insurance.
As a freelancer all of it is retail to you. Enter it in `--benefits`.

### 4. Bench time

Contracts end. Pipelines gap. A realistic year includes 1–3 unpaid months
of overlap, holidays-between-contracts, and "the client ghosted after SOW
signature". Bench is priced into the working months — that's why
`--bench-months` shrinks billable hours.

## The Multiplication Effect

Put together, replacing a salary takes roughly **2–2.5× the naive hourly**:

```
$95,000 salary → naive $45.67/h
  × 1.47 (taxes: keep 68% of revenue)
  × 1.67 (billable ratio 60%)
  × 1.09 (bench month)
  × 1.10 (benefits self-funded)
  ≈ $115–120/h honest replacement
```

This is why "I'll just charge $50/h, that's more than I made salaried!"
ends in burnout at month 14 with savings gone.

## Fixed-Bid Pricing

Hourly billing transfers estimate risk to the client; fixed-bid transfers
it to you. Price the transfer:

```
quote = hours × (1 + risk_buffer) × rate
```

- **Risk buffer 15%** for well-defined scope, 25–35% for fuzzy scope.
  It's not padding — it's insurance you're selling them.
- **Rush premium +25%**: compressed timelines compress everything else
  out of your calendar.
- **Value ceiling**: if the client's expected value from the work is $10k,
  a $14k quote loses regardless of your costs. Cap and note it.
- **Change orders**: quote the base scope; every addition gets
  "happy to quote that as a change order at the same rate" — in writing.

### Effective-rate exposure

If you quote $8,100 for 60 buffered hours but it takes 80:
effective rate = $8,100/80 = **$101/h**. The tool prints this so the
downside is visible before you sign.

## Value-Based Pricing (When It Beats Hourly)

When your work creates outsized, measurable client value — a checkout flow
worth +$200k/yr, an automation saving 20 h/week — hourly billing caps you
at your cost. Value pricing anchors on their gain:

- Estimate client's annual gain conservatively
- Price at 10–30% of that gain
- Still compute your hourly floor with this tool — value price must never
  fall below `hours × honest rate`

Use hourly for ambiguous scope, value for measurable outcomes, retainer
for ongoing access (retainer = guaranteed billable ratio, so a 10–15%
discount off the spot rate is rational).

## Rate Increase Scripts

**Existing clients (30-day notice):**
> "Starting [date] my rate for new work will be $X/h. Current projects
> continue at the current rate through [end of current SOW]. I wanted to
> give you as much runway as possible to plan around it."

**New client asking 'why so much':**
> "The rate covers delivery, not just hours — it's built on my actual
> capacity, taxes, and the tools and insurance I carry so you don't have
> to. If the number doesn't fit, I can propose a smaller scope that does."

**Recruiter pushing 'budget is $X':**
> "I understand. At $X the scope that fits is [trimmed scope]. If you want
> the full scope, it's $Y. I don't discount the rate — I resize the work."

## Estimating Bench, Costs, and Ratio (Worksheet)

Before your next `rate` run, fill these honestly:

| Input | Where to find it |
|---|---|
| Target net | last year's take-home + inflation + savings goal |
| Overhead | sum actual subscriptions, hardware amortized, insurance, CPA fees |
| Benefits | health premiums quote + retirement you'll self-fund |
| Billable ratio | 2 weeks of honest time-tracking (include sales/admin!) |
| Bench months | your last 12 months' unpaid gap, +1 if pipeline < 3 warm leads |

## Limits of This Model

- US-centric taxes (SECA, rough income tax). Elsewhere: override
  `--se-tax`/`--income-tax` with local equivalents.
- Single-person model; agencies have payroll, margin, and sales-comp
  structures this doesn't model.
- Planning aid, not tax advice. Quarterly estimates, deductions, and
  entity structure belong to a CPA.
