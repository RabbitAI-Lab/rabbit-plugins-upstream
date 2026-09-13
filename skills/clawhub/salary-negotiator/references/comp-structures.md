# Compensation Structures — How to Value Every Component

A defensible negotiation requires normalizing offers with different shapes into
comparable numbers. This reference documents each component, its risk profile,
and the valuation approach `salary_negotiator.py` uses.

## The Risk Ladder

Cash now > cash soon > cash probably > cash maybe:

| Component | Certainty | Valuation approach |
|---|---|---|
| Base salary | ~Certain | Face value |
| 401(k)/pension match | Certain (if you stay) | Face value, capped |
| Sign-on bonus | Certain (clawback risk) | Face value ÷ amortization years |
| Target bonus % | ~85% historical payout | base × bonus% × 0.85 |
| RSUs (public co) | High, vesting forfeiture ~10% | grant value × 0.90 |
| RSUs (pre-IPO) | Moderate — liquidity discount | grant value × 0.50–0.70 |
| Options (startup) | Lottery-class | paper value × 0.15 (or less) |
| Equity refresh grants | Uncertain policy | Exclude from EV; negotiate in writing |

## Base Salary

The anchor everything else hangs on. Bonus %, 401k match, and future raises
are all computed **from base** — a low base compounds for years. This is why
the tool flags "base X% below market median → negotiate BASE specifically":
$10k more base is worth ~$50k+ over five years via compounding raises and
match, far more than a one-time $10k sign-on.

## Bonuses

- **Target bonus %**: companies quote the target; actual payout history
  matters. 0% payout happens in bad years; 200% in great ones. Default
  assumption: 85% of target.
- **Guaranteed first-year bonus**: counts at face value (it's a deferred
  sign-on).
- **Discretionary bonus**: treat as 0 in EV; treat as a nice surprise.

## Sign-On Bonuses

Face value ÷ amortization period (default 3 years) — because it's one-time
money compensating for a recurring shortfall, or bait that disappears in
year 2. Watch for:
- **Clawback clauses**: repay pro-rata if you leave within 12–24 months.
- **Replacement bonus**: some companies pay sign-on instead of year-1 refresh;
  ask "is this instead of or in addition to the annual refresh?"

## RSUs (Restricted Stock Units)

- **Public company**: shares at vest, sellable. Value = grant ÷ vest years,
  annualized, × 0.90 retention factor (a ~10% chance you leave before vest).
- **Pre-IPO**: add a liquidity discount (0.50–0.70). Until there's a market,
  paper value ≠ cash value. Ask: last 409A valuation, preferred price,
  IPO horizon, any secondary sale windows.
- **Cliffs**: 1-year cliff means leaving at month 11 forfeits everything.
- **Refresh policy**: "front-loaded" 4-year grants with no refresh = a
  compensation cliff in year 5. Ask explicitly.

## Stock Options

- Paper value = (FMV − strike) × shares. **Never treat paper value as real.**
- Most startup options expire worthless, not because the company dies, but
  because of strike costs, taxes (AMT in the US), illiquidity, and
  exercise-window traps.
- Default EV factor: **0.15** of paper value. Earlier-stage → lower.
- Key questions: strike price, latest valuation, post-termination exercise
  window (90 days vs 10 years — this is a huge deal), ISO vs NSO.

## 401(k) Match / Pension

Match is cash with extra steps: employer contributes match% of salary up to
a cap. Value = min(base × match%, cap). It vests with the company's vesting
schedule (cliff-vesting match is retention compensation — factor it in when
comparing "free at 1 year" vs "free immediately").

## Benefits Deltas

When comparing offers, only the **differences** matter:

- **Insurance**: premium difference + out-of-pocket-max difference for your
  family's actual usage. A $300/mo premium difference = $3,600/yr.
- **PTO**: above-market PTO ≈ (days above market norm) × daily rate. 10 extra
  days at $200k ≈ $8k/yr of value — and it's often an easier ask than base.
- **Remote/stipends**: home-office, internet, co-working. Small but real.
- **Learning budget**: real if you'd spend it anyway.

## Worked Example: BigCo vs Startup

| | BigCo | Startup |
|---|---|---|
| Base | $150,000 | $130,000 |
| Bonus | 15% target | 0% |
| RSU | $60k/yr public | — |
| Options | — | 0.5%, strike $1.50, val $60M |
| 401k match | 4% capped $8k | none |

EV computation (tool defaults):
- BigCo: 150,000 + 150,000×0.15×0.85 (19,125) + 60,000×0.90 (54,000) +
  min(150,000×0.04, 8,000)=6,000 → **≈ $229k/yr**
- Startup: 130,000 + options: 0.5% × $60M = $300k paper ÷ 4yr = $75k/yr
  × 0.15 = 11,250 → **≈ $141k/yr + lottery ticket**

The "0.5% of a $60M company" sounds bigger than $60k/yr RSUs. After honest
risk weighting it is worth ~$11k/yr. Decide with eyes open — and if you take
the startup offer, negotiate **base and option pool**, not the paper dream.

## Multi-Year Views

Run the numbers at years 1, 2, 3 (`compare` prints all three):
- Year 1 includes sign-on; years 2-3 don't.
- Refresh grants (if promised in writing) start in year 2.
- A startup whose base is $20k lower costs you $60k over 3 years guaranteed —
  the options must plausibly beat that **plus** forgone BigCo RSUs to win.

## Negotiation Levers Beyond Base

When base is capped ("the band is the band"), in rough order of askability:

1. Sign-on bonus (easiest one-time yes)
2. Equity refresh commitment in writing / larger initial grant
3. Earlier review with written criteria ("6-month review at 160k if X")
4. Extra PTO days
5. Remote work / stipend / co-working budget
6. Title (cheap for them, valuable for your next negotiation)
7. Start-date bonus, relocation flexibility, equipment budget

Each is a scripted ask in [`scripts.md`](scripts.md).
