---
slug: invassistant
displayName: InvAssistant
description: >
  Multi-asset investment portfolio management framework with A/B/C asset-class differentiated rules,
  7 red-line portfolio risk controls, and 4-factor QMS quality scoring.
  Covers US, A-share (China), and HK stocks with disciplined entry/exit logic.
  中文摘要：多资产投资组合管理框架——A/B/C 类资产差异化规则、7 条红线组合风险控制、四因
  子质量管理，覆盖美股/A股/港股的纪律化进出场逻辑。触发词：投资组合管理、持仓复盘、
  风险红线检查、仓位规则.
description_zh: "多资产投资组合管理框架：A/B/C 类资产差异化规则、7 条红线组合风险控制、四因子质量管理；覆盖美股、A 股、港股，纪律化进出场逻辑。"
version: "2.3.14"
read_when:
  - "User requests portfolio review, A/B/C asset classification, or 7-red-line risk check for their holdings"
  - "User asks about entry/exit logic for US stocks, A-shares (China), or HK stocks under the framework"
  - "User requests QMS (quality scoring) evaluation of a stock candidate"
  - "User asks about portfolio risk controls, warning lines, or position sizing rules"
  - "User wants to log a trade or review trade history against the framework"
not_for:
  - "Real-time trading signals or market timing predictions"
  - "Specific stock buy/sell recommendations without portfolio context"
  - "Tax, legal, or regulatory advice — this is a portfolio management framework, not financial advice"
  - "Analysis of assets outside US / A-share / HK stocks (crypto, commodities, fixed income) without adaptation"


allowed-tools:
  - read_file
  - write_to_file
  - replace_in_file
  - execute_command
disable: false
metadata:
  openclaw:
    requires:
      bins:
        - python3
      env: []
    tags:
      - investment
      - trading
      - portfolio
      - stock
      - finance
      - us-stock
      - a-share
      - hk-stock
      - risk-control
---
name: invassistant
description: >
  Multi-asset investment portfolio management framework with A/B/C asset-class differentiated rules,
  7 red-line portfolio risk controls, and 4-factor QMS quality scoring.
  Covers US, A-share (China), and HK stocks with disciplined entry/exit logic.
allowed-tools:
  - read_file
  - write_to_file
  - replace_in_file
  - execute_command
disable: false
metadata:
  openclaw:
    requires:
      bins:
        - python3
      env: []
    tags:
      - investment
      - trading
      - portfolio
      - stock
      - finance
      - us-stock
      - a-share
      - hk-stock
      - risk-control
---

# InvAssistant

> Multi-asset investment portfolio management framework — current version v2.3.14 (2026-09-11).
> Core philosophy: portfolio before stock-picking, discipline before inspiration. Rules are guardrails, not cages.

> ⚠️ **Risk Warning**: This is a decision-support framework, not financial advice. AI guidance is probabilistic; all action triggers — including rule-based alerts and entry thresholds — require human review before any execution. Author assumes no liability for trading losses.

---

## 1. Asset Classification (Three Tiers)

This is the foundation of v2.1+. Different assets use different exit logic.

| Tier | Definition | Rules | When To Sell |
|------|-----------|-------|-------------|
| **A-Class (Platform Core)** | Long-moat, cash-flow-stable platform companies | HOLD, no trailing stop; DCA entries | Only 3 reasons: ① fundamental deterioration (2+ quarters) ② narrative change ③ portfolio limit breach |
| **B-Class (High-Beta Cyclical)** | High-beta, narrative-driven growth | Trailing stop + position management | QMS < 40 triggers review |
| **C-Class (Low-Volatility Income)** | Broad-market/dividend ETFs, utilities | DCA + rebalancing | No active timing |

Key insight: A-class price drawdowns ≠ sell signals. Using trailing stops on A-class washes out long-term compounders.

---

## 2. Portfolio Risk Controls: 7 Red Lines (Non-Overridable)

| # | Rule | Threshold | Action |
|---|------|-----------|--------|
| 1 | Single position concentration | >25% | Reduce to ≤20% within 3 months |
| 2 | Single sector concentration | >35% | Reduce to ≤30% within 3 months |
| 3 | AI single-narrative | >50% | Reduce to ≤40% within 6 months |
| 4 | Portfolio drawdown (mild) | >-12% | Halve satellite positions |
| 5 | Portfolio drawdown (severe) | >-15% | Total position ≤60% |
| 6 | VIX systemic risk | ≥40 | Reduce total to ≤50% |
| 7 | Pre-Trade Log compliance | <100% | Log immediately |

---

## 3. US Stock Strategy

### Entry Modes

| Mode | Applies To | Logic |
|------|-----------|-------|
| **A (Panic Mispricing)** | B-Class (high-beta narrative) | Emotion release + technical support + VIX <25 |
| **B (Trend Confirmation)** | B-Class | Price > MA50 + breakout + fundamentals + valuation |
| **C (Rebalancing)** | Portfolio-level | Triggered by Red Lines 1-3 only |
| **D (A-Class Candidate Zone Entry)** | Candidate pool (non-tech diversification targets) | Callback-based, no observation delay |

### Mode D: A-Class Candidate Zone Entry (v2.1.1)

Applied to new A-class candidates before they join the core portfolio. Designed to solve the "observation delay misses entry window" problem.

**Principle**: No observation delay. A -10% pullback from 20D high on an A-class candidate is itself a complete entry signal — the underlying moat business doesn't change with share price.

| Zone | Trigger | Allocation | Execution |
|------|---------|------------|-----------|
| First tranche | -10% from 20D high | 50% of target | Execute immediately |
| Add | -15% (or >3% further drop after first) | 30% | Execute on trigger |
| Final | -20% (or 5+ days sideways without new low) | 20% | Within zone |

**Constraints**: total ≤2% portfolio; some candidates carry an additional valuation gate (e.g. an entry PE-percentile cap); no chasing after rebound.

**Anchor discipline**: the anchor is the **20-day high, frozen at position open**. Do not substitute a 12-month or 52-week range high — that belongs to the range-position rule (§13 D1). A level computed off the wrong window is arithmetically correct and semantically wrong.

### Why Different from Panic-Entry Mode A

Narrative-driven, high-beta satellites need bottom confirmation — the drop might be fundamentally justified. A-class candidates (moat compounders) only need price confirmation — a -10% discount on a quality business is self-evidently an opportunity.

---

## 4. A-Share Strategy (3-Condition Engine)

All three conditions must pass for entry:

| Condition | Standard |
|-----------|----------|
| ① Engine score ≥80 + 3 consecutive days on list | Core selection pool |
| ② Current price ≤ dynamic target (with floor) | `max(static×0.85, min(static, MA20×0.95))` |
| ③ MA20 flat or turning up | MA20 delta ≥ -0.05 |

**Flex window**: 2/3 conditions met + 3rd deviation ≤10% → half-position trial.
**Time stop**: 6 months max in selection pool without entry → forced review.

---

## 5. HK Stock Strategy

| Source | Framework |
|--------|-----------|
| Actively bought | Follow A/B/C classification rules |
| Company allocation/incentive | Warning line + reduction framework (not hard stop) |

**Warning line** (not hard stop): Triggers 48h review upon breach.
**Time limit**: 18 months post-vesting with remaining position → unconditional full exit.

---

## 6. QMS Scoring (4-Factor)

```
QMS = 0.35 × Earnings Trend
    + 0.25 × Sector Relative Strength
    + 0.25 × EPS Revision
    + 0.15 × Price Structure
```

| Score | Meaning | Action |
|-------|---------|--------|
| ≥70 | High quality + good timing | Hold / observe entry |
| 50-70 | Healthy, not at entry point | HOLD |
| <50 | Quality or timing issues | No new positions |
| <40 | Review exit queue | Evaluate reduction (B-Class only) |

**Boundary**: QMS is entry reference for A-Class, NOT an exit trigger. Only B-Class uses QMS <40 as reduction signal.

---

## 7. Monthly KPIs

| KPI | Threshold | Type |
|-----|-----------|------|
| Monthly turnover rate | ≤15% | Red line |
| Pre-Trade Log compliance | =100% | Red line |
| A-Class sold on price volatility | =0 | Red line |
| Panic-period reduction (VIX≥30) | =0 | Red line |
| System execution rate | ≥80% | KPI |

---

## 8. Hard Rules Summary

1. Asset classification determines action semantics: A-Class no trailing stop, B-Class uses trailing stop
2. Held vs. watchlist semantics must not be mixed
3. A-share 3-condition is a filter: all pass → entry (flex window = 2/3 + deviation + half-size)
4. US B-Class dual-mode: Mode A (3 red lines all pass) / Mode B (4 conditions all pass)
5. Unfilled ≠ holding: portfolio data must reflect actual positions
6. Never fabricate data: all indicators must come from live data sources
7. A-Class only sells on 3 fundamental reasons (never price)
8. 7 Red Lines triggered = must follow, no override
9. Allocation/incentive positions do not use standard stops
10. Every override must be logged
11. Max 2 overrides per ticker per quarter; 3rd is void
12. Daily self-check: 5 questions, all "no" = no trade today

---

## 9. Output Format

Portfolio reviews and risk checks produce:
- **Structured review report** — A/B/C classification table, red-line pass/fail flags, position-sizing check, QMS scores for candidates
- **Action list** — framework-compliant observations (never directives): what to watch, what violates a rule, what needs human decision
- **Data-source annotations** — each number carries its source and timestamp; unsourced values are marked


---

## 10. Data Sources

| Data Type | Primary | Fallback |
|-----------|---------|----------|
| US stock quotes/technicals | westock-data | Yahoo Finance |
| A-share K-line/technicals | westock-data | AKShare |
| HK stock quotes | westock-data | Yahoo Finance |
| VIX | westock-data | Yahoo Finance |
| North-bound capital | NeoData | AKShare |
| Financial reports/consensus | westock-data | NeoData |

---

## 11. Common Mistakes

| # | Mistake | Fix |
|---|---------|-----|
| P1 | Treating A-Class as B-Class (v2.0's worst error) | Ask "Is this A or B?" before acting |
| P2 | Writing "reduce" for watchlist stocks | Ask "Is this held?" first |
| P3 | Cross-market strategy pushed to sub-pages | Cross-market → main page; specific rules → sub-page |
| P4 | LaTeX `$xxx` swallows first digit | Use `US$` / `HK$` / `¥` / `\$` |
| P5 | Wrong code block language (`'plain'`) | Must use `'plain text'` (with space) |
| P6 | Adopting a capital plan without running the consistency audit (§12) | Run A1-A5 before adopting any multi-sleeve plan |
| P7 | Writing a threshold on a metric without pinning its caliber (§12 A5) | Name the adopted caliber and list the banned ones in the rule file |
| P8 | Applying a derived price level without declaring which anchor window it came from | Resolve the window from the rule's own definition, never from whichever high is nearest in the file |
| P9 | Editing a level in every file where it appears instead of editing the registry (§13 D3) | One writable copy; everything else is a mirror — fix the registry, then propagate |
| P10 | Building an example config out of your own live holdings (§13 D8) | Sample tickers must be generic and must not coincide with anything you hold |

---

## 12. Capital Plan Consistency Audit

Run these checks before adopting any multi-sleeve capital plan (account-level targets, DCA schedules, subtype caps). All of them caught real defects on first use; all are arithmetic, not judgment — detect them by computing, not by reading.

| # | Check | Failure signature | Detection |
|---|-------|-------------------|-----------|
| A1 | **Fixed-amount vs percentage cap** | A fixed monthly split silently breaches a percentage cap partway through the horizon | `monthly_amount × horizon > cap_remaining` for any sleeve |
| A2 | **Target attainability** | The headline target is unreachable under currently active constraints (frozen / blocked sleeves) | `Σ deployable across OPEN sleeves only < required deployment` |
| A3 | **Label vs look-through exposure** | Subtype labels understate true industry concentration; ETF holdings carry hidden weights | `direct_holding + Σ(ETF_value × constituent_weight)` vs cap |
| A4 | **Drag vs protection breakeven** | "Idle cash is waste" conclusions ignore the option value given up | `p* = annual_drag_eliminated / protection_given_up` |
| A5 | **Metric caliber pinned** | A rule fires off a metric whose caliber is undefined, so conflicting published values are interchangeable | See A5 below |

**A1 fix**: allocate by remaining gap to cap, recomputed monthly — never by fixed amount. A fixed amount and a percentage cap are mathematically inconsistent whenever prices move.

**A2 fix**: state cash targets as two stages — a transitional range that is actually reachable with the sleeves open today, and the strategic range that becomes reachable on a stated trigger. Writing an unreachable target puts the rule in violation from day one.

**A3 fix**: set a look-through industry cap that takes precedence over the subtype label cap. Re-test before every new position, since adding a direct holding and growing an ETF sleeve compound.

**A4 fix**: report the breakeven probability, not the drag alone. Drag is certain and annual; protection is contingent and only pays on drawdown. A drag of 0.1% p.a. is not worth buying with concentration risk.

### A5 — Pin the caliber of every threshold metric

If a rule says "yield < X triggers Y" without defining how yield is measured, the rule is undefined, not implemented. Published values for the same instrument routinely differ by 2x. Worked example on a dividend ETF — four circulating figures, four different calibers:

| Figure | Caliber | Verdict |
|---|---|---|
| 2.44% | Year-to-date distributions ÷ price. **Not annualised**; at mid-year only half of the year's four payments are counted, so it understates at every mid-year point | Ban |
| 4.34% | Trailing four actual distributions ÷ current price | **Adopt** |
| 4.88% | Index yield, rolling, pre-tax, before fund fees | Ban |
| 4.93% | Index yield, index-provider periodic-review basis — updated once a year, denominator is a lagged average market cap | Ban |

**A5 procedure**: enumerate every published value with its caliber; adopt the one that measures what the holder actually receives; write the adopted caliber and the banned calibers into the rule file itself. Then apply A5 to the *other* side of the comparison too — a yield-vs-bond threshold also needs the bond yield pinned (curve yield vs on-the-run yield vs third-party quote differ by 5-15bp), and stale reference rates silently inflate the buffer.

Two follow-on habits that A5 surfaced:

- **Reconstruct suspicious figures before trusting or discarding them.** Back-solving `dividends ÷ yield` gave an implied price of 1.4344 against an actual NAV of 1.4522, which identified the caliber definitively. A number you cannot reconstruct is a number you have not checked.
- **Check whether the payout is contractually guaranteed.** Distributions may be conditional (e.g. fund contract requiring excess return over the benchmark before any distribution). A conditional payout makes the yield a binary variable — it can go to zero — which no continuous threshold handles. Track it as a separate monitoring item.

**Related — DCA stop/resume**: model DCA as a state machine (ACTIVE / PAUSED / STOPPED / FROZEN / BLOCKED) with explicit downgrade and upgrade conditions. **Downgrades may be automatic; upgrades must require human confirmation.** An auto-resume buys back right after a rebound, which is a systematic momentum-chasing switch. Also separate "plan completed" (position count reached — resume needs a new plan) from "risk halt" (cap breached — resume when the ratio falls back); treating both as one frozen state loses the distinction.

Give a thin threshold buffer a false-trigger guard (require two consecutive confirmations) plus a fast path for genuine deterioration (a single large move suspends immediately). Pausing inflows is cheap; breaking DCA continuity is not, since continuity is the point of DCA.

---

## 13. Derived Price Level Governance

Every price in this framework that is *computed* rather than *quoted* is a derived level: mode-D add lines, mode-B pullback triggers, range-position bands, B-class trailing stops, and derived thresholds such as a yield-versus-bond gate. They share one failure mode — none of them is self-contained. Each is `f(anchor)`, so a level is only as trustworthy as the anchor behind it, and an anchor that is never declared cannot be checked.

This section exists because a live portfolio once carried the same add-line at two different values in three different files. The trigger line sat within 1% of the price, so the disagreement was not academic. Root cause: a wide-window range high had been reused as the anchor for a narrow-window rule.

### D1 — Anchor windows are per-rule, not per-instrument

A single instrument legitimately has several "highs." They are not interchangeable:

| Rule type | Anchor window | Typical semantics |
|---|---|---|
| Short-horizon add line (e.g. candidate staged entry) | **Recent N-day high** | Short-term drawdown reference; frozen at position open |
| Pullback add on an existing holding | Recent N-day high | Rolling |
| Range-position monetisation | **52-week / 12-month high** | Upper edge of a long box; rolling, reviewed monthly |
| Trailing stop | Rolling high | Rolling, paired with a buffer |
| Derived threshold (yield, spread) | A reference rate or curve point | Refreshed on a fixed calendar |

A 52-week high answers "how far below the one-year top are we." A 20-day high answers "how far below the recent local peak are we." Substituting one for the other produces a level that is arithmetically correct and semantically wrong — which is worse than an arithmetic error, because it looks plausible.

### D2 — Never reverse-engineer an anchor from a target level

Solving `anchor = level ÷ factor` to explain an existing level manufactures an anchor out of nothing. It always "works" — any level divides by any factor — and it launders a bad number into a registered one. Two independent tells that this has happened:

- **Anchor self-inconsistency.** If a rule generates several levels from one anchor, back-solving each level must return the same anchor. Two different implied anchors means neither is real.
- **Anchor coincidence.** If the implied anchor lands within a fraction of a percent of another rule's anchor for the same instrument, the level was almost certainly computed off the wrong window.

Anchor first, from market data. Levels second. Never the reverse.

### D3 — One source of truth, everything else is a mirror

Levels get copied into whatever file needs to read them — position state, risk state, dashboards. The moment there are three writable copies, they drift. Fix the topology, not the values:

- A **registry** holds each level once, with `anchor.type`, `anchor.value`, `anchor.date`, freeze semantics, the per-level `formula`, and a `status`.
- **Every other occurrence is a mirror.** Edit the registry, then propagate. A mirror mismatch is never a judgement call — it is an error.
- Write the **anchor-window convention table** into a machine-readable file next to the registry, not into prose. A convention that exists only in a report has no enforcement power; the next scan will re-derive the level from whatever high it happens to have loaded.

### D4 — Validate mechanically, and be explicit about what the validator judges

Reading the numbers does not find these defects — they are all internally plausible. Only recomputation does. A level validator should check, in this order:

| # | Check | Detection |
|---|---|---|
| D-a | **Anchor rebuild** | Rebuild the anchor independently from daily data over the declared window and freeze date; compare |
| D-b | **Formula recompute** | Recompute each level from the registered anchor and compare |
| D-c | **Mirror consistency** | Every copy outside the registry must equal the registry value |
| D-d | **Cross-window suspicion** | Anchor within ~0.5% of another rule's anchor or range high for the same instrument |
| D-e | **Branch ordering** | When a level has two trigger branches, the higher price must trigger first |
| D-f | **Level already breached** | A live add line above the current price means it fired, or the level is wrong — either way it needs an owner |

Two design rules matter more than the checks themselves:

**The validator audits whether the truth is faithfully registered, not whether the truth is correct.** A mismatch on an entry marked `verified` is a hard failure. The same mismatch on an entry already registered as `unverified`, `suspected` or `conflicting` is a warning — the defect is on record and under repair. Without this split, a known open item turns the gate permanently red and the gate stops meaning anything; red must mean "new problem," or nobody reads it.

**An unverifiable anchor is not a passing anchor.** When the data window does not reach back far enough to rebuild the anchor, the correct output is "unverified," not "no problems found." Silence is not evidence.

### D5 — Declare, register, validate, resolve, trace

The five-step loop, applied before acting on any level:

1. **Declare** — name the rule, then take the anchor window and freeze semantics from that rule's definition.
2. **Register** — the level must be in the registry with a complete anchor record. An unregistered level is not usable for a decision.
3. **Validate** — run the validator. Its output is the only accepted evidence.
4. **Resolve** — a hard failure blocks the action. Warnings and open entries are surfaced in the output, never silently absorbed.
5. **Trace** — an anchor or formula change keeps the previous value, the reason and the date. Anchors get edited by scans, merges and hand fixes; without a trace, nobody can tell a correction from a corruption.

### D6 — Resolve every percentage cap against the owning account, not the portfolio

A percentage-of-capital limit is only meaningful once its base is named. Portfolio documents tend to say "≤N% of total assets" in dozens of places while defining "total assets" nowhere, and the same phrase quietly drifts into meaning four different numbers: portfolio net asset value, securities market value, and each account's own total.

The rule: **an add-size cap resolves against the total value of the account the instrument sits in**, because cross-account cash is not fungible. Portfolio-level limits — concentration, drawdown, allocation drift — resolve against portfolio net asset value. Account-scoped ceilings resolve against that account. State which base was used whenever a cap comes into play.

Two corollaries:

- **Ratify before you rewrite.** Check how the historical trade log actually computed the percentage before declaring a base. If the log has been using the owning-account basis all along, the formal definition ratifies existing practice rather than changing it — and it must not alter any past decision.
- **Beware same-named account fields.** An accounts block may store one book's value cash-inclusive and another's securities-only. Summing the block then silently drops cash. Resolve totals from the aggregate block, never by adding up account entries.

A cap whose base is unstated is not a cap — it is a number that will be computed two ways by two people.

### D7 — Date every balance, and reconcile it with a rollforward

Prices get validated; balances usually do not. A price series is visibly wrong when it is stale — the change column gives it away. A cash figure is invisible: it sits in a state file looking exactly like a fresh number until someone reads the broker.

The rule: **every balance-like field carries its own as-of date and source.** A balance with no as-of marker is treated as unverified, never as current. And any account-level correction ships with a **cash rollforward** — an anchor balance, every cash-moving entry in the interval, and the residual. A non-zero residual must be attributed explicitly (rounded anchor, unlogged entry, or genuinely unresolved). Never absorb it silently.

Three corollaries:

- **Match the check strength to the field's liquidity.** A field that becomes spendable cash tomorrow deserves a stronger gate than an analytical estimate. If your derived levels have a multi-check validator and your balances have none, the asymmetry is the bug.
- **Arbitrate by tier, not by recency.** A first-party broker statement wins on account-level truth — net liquidation value, cash, share counts. The exchange close wins on price. Reconcile both, state the delta and its cause, and never let one silently overwrite the other.
- **A displayed number is not a stored number.** Broker apps round. When a panel shows a rounded figure, recover the precise value from the account identity (net liquidation value minus market value) and record the rounding delta rather than quoting the display.

A stale balance is the most expensive kind of stale data, because nothing about it looks stale.

### D8 — Example configs carry no author positions

Sample data is built by copying the shape of whatever book the author happens to run. That is convenient, and it is also an export: a shipped example watchlist, a `--detail` example in a docstring, or a sample trade log quietly publishes the author's positions to everyone who installs the package. Nothing marks it as a disclosure, so nobody reviews it as one.

The rule: **sample tickers are generic and must not coincide with anything actually held.** A demo exists to show the shape of the config — strategy types, exit ladders, adapter wiring — and every one of those survives substitution. Cost bases, share counts and account balances are left at zero or plainly synthetic values for the same reason.

Two corollaries:

- **Comment residue counts.** Reviewers check the config body and skip the docstrings. A ticker sitting inside a usage example or an `Args:` block is exactly as public as one in the watchlist, and it is the one a scan for "does this file contain a symbol I hold" is least likely to cover.
- **Re-check on release, not on authoring.** A ticker that was neutral when the example was written becomes a disclosure the day it is bought. Audit before publishing, not when the sample is first drafted.

An example that mirrors your book is not a demo — it is a position disclosure shipped without review.

---

### Two rules that make this structural rather than procedural

**Opposing rules on the same instrument need a mutex.** An add line below the price and a reduce band above it are both legitimate, but if both can fire in the same period the framework contradicts itself. Resolve by first-trigger-wins on a logged timestamp, freeze the other side for the period, and re-evaluate next period. Never allow a same-period add and reduce.

**A level near the price is a live commitment, not a monitor.** The closer a line sits to the current price, the more it needs a registered anchor, a named owner and an execution plan. Distance creates the illusion of safety; the level that is 0.5% away is the one that will be hit while nobody is watching.

**A definition backfill is not a rule change — label it as such.** When a term the rules lean on was never actually defined, defining it changes no threshold and no mode; it only removes the room for two people to compute the same situation differently. Publish it under its own version, call it a backfill, and leave every number untouched. Silently "clarifying" a value is how a definition becomes a rule change nobody signed off on.

---

## Reference Files

| File | Use when |
|------|----------|
| `references/a_share_strategy.md` | A-share selection and DCA rules |
| `references/us_stock_strategy.md` | US/HK position management |
| `references/risk_control_and_overrides.md` | Red lines, macro levels, override procedure |
| `references/candidate_admission_gates.md` | **Promoting a candidate to watchlist** — G0-G5 gates, S6 dividend-yield water level, look-through industry cap. Read before any "add to watchlist" request. |

---

## Version History

| Version | Date | Summary |
|---------|------|---------|
| v2.3.14 | 2026-09-11 | Add D8 (example configs carry no author positions — sample tickers must be generic and must never coincide with real holdings, because a shipped example that mirrors your book is a disclosure, not a demo) + P10; purged real tickers from `scripts/init_config.py` sample watchlist and from two inline code comments |
| v2.3.9 | 2026-09-07 | Add §12 Capital Plan Consistency Audit (A1-A5) + P6/P7; candidate admission gates reference (G0-G5, look-through cap); restore Risk Warning & Output Format from ClawHub 2.3.8 |
| v2.3.13 | 2026-09-11 | Add D7 (every balance carries an as-of and source; account corrections ship with a cash rollforward; arbitrate broker-vs-exchange by tier; never quote a rounded display) — prompted by a 6-week-stale cash field that produced a phantom discrepancy, while derived price levels already had eight mechanical checks |
| v2.3.12 | 2026-09-11 | Add D6 (capital-base resolution — caps resolve against the owning account; ratify historical practice, never sum mixed-basis account blocks) + definition-backfill principle. Frame D1-D5 list as §13 D1-D7 |
| v2.3.11 | 2026-09-11 | Add §13 Derived Price Level Governance (D1-D5) + P8/P9 — anchor-window declaration, single source of truth for levels, mirror discipline, and mechanical level validation |
| v2.3.10 | 2026-09-08 | Add not-individualized-advice disclaimer to risk_control_and_overrides.md (scanner finding) |
| v2.3.3 | 2026-08-07 | Sync SKILL.md version declaration with ClawHub package metadata |
| v2.3.2 | 2026-06-06 | Fix display name (remove Clean suffix) |
| v2.1.2 | 2026-06-06 | Audit cleanup: bilingual README, remove legacy files |
| v2.1.1 | 2026-06-04 | Mode D: A-class candidate zone entry (no observation delay) |
| v2.1 | 2026-05-18 | A/B/C asset classification; 7 red lines; 4-factor QMS; trailing stop removed from A-class |
| v2.0 | 2026-05-18 | Full rebuild: decision pyramid, 5-factor QMS, 10 red lines (replaced) |
| v1.5 | 2026 Q1-Q2 | 3-condition engine, dual-mode entry, trailing stops |

---

> 中文简介：InvAssistant 是一个多市场投资组合管理框架。按资产三层分类（A/B/C）执行差异化规则，7 条组合红线不可覆盖，4 因子 QMS 评分辅助决策。覆盖美股、A 股、港股。核心信念：组合优先于选股，纪律优先于灵感。规则是栏杆，不是牢笼。
