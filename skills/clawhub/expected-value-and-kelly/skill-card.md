## Description: <br>
Guides agents through expected-value checks, Kelly sizing, fractional-Kelly adjustments, and stop triggers for repeated capital-allocation decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and agents use this skill to decide whether a repeated bet or allocation has positive expected value and how much bankroll, budget, or capital to stake using Kelly or fractional Kelly sizing. It is suited to repeated decisions such as ad spend, A/B test ramps, portfolio sizing, venture allocation, and other measurable edge cases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can influence betting, investment, or business allocation decisions and may be mistaken for personalized financial advice. <br>
Mitigation: Treat outputs as educational decision-support, verify inputs independently, and have qualified humans review material allocation decisions. <br>
Risk: Incorrect probability, payoff, bankroll, or correlation assumptions can produce misleading Kelly fractions and oversized bets. <br>
Mitigation: Use fractional Kelly for estimated edges, include uncertainty ranges, check correlation, and set stop-and-reestimate triggers before acting. <br>
Risk: Applying Kelly to one-shot or non-repeatable life decisions can misframe the decision. <br>
Mitigation: Confirm the decision is repeated and measurable before using Kelly; redirect one-shot life decisions to a regret-minimization approach. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/expected-value-and-kelly) <br>
- [deciqAI skill metadata](https://www.deciqai.com/s/expected-value-and-kelly.json) <br>
- [deciqAI knowledge-skills repository](https://github.com/deciqAI/knowledge-skills) <br>
- [Primary sources](references/sources.md) <br>
- [Ed Thorp blackjack and Princeton-Newport example](examples/ed-thorp-blackjack-and-princeton-newport-1961-1988.md) <br>
- [Bill Benter Hong Kong horse racing example](examples/bill-benter-hong-kong-horse-racing-1985-2001.md) <br>
- [Hyperscaler GPU capex Kelly example](examples/hyperscaler-gpu-capex-kelly-2023-2026.md) <br>
- [Kelly 1956 paper](https://www.princeton.edu/~wbialek/rome/refs/kelly_56.pdf) <br>
- [Thorp Kelly criterion paper](https://www.eecs.harvard.edu/cs286r/courses/fall12/papers/Thorpe_KellyCriterion2007.pdf) <br>
- [SEC EDGAR company filings](https://www.sec.gov/cgi-bin/browse-edgar) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown EV-Kelly sizing analysis with explicit inputs, formulas, fractional sizing, and stop triggers.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided or estimated probabilities, payoffs, bankroll or budget, uncertainty, repeatability, and correlation assumptions.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
