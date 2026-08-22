## Description:

Compare debt payoff strategies with real amortization math: avalanche (highest APR first), snowball (smallest balance first), and minimum-only baseline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to compare personal debt payoff strategies, estimate debt-free dates, and generate month-by-month payoff plans for consumer debts such as credit cards, student loans, personal loans, and auto loans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The calculator may be mistaken for professional financial advice.

Mitigation: Present outputs as planning estimates and have users review assumptions or consult a qualified advisor before acting on material debt decisions.

Risk: Sensitive debt balances, APRs, and minimum payments are entered by the user.

Mitigation: Run the planner locally and avoid sharing debt inputs with external services or logs.

Risk: The model excludes mortgages, tax effects, loan forgiveness programs, investment comparisons, and changing minimum-payment formulas.

Mitigation: Use it for consumer-debt payoff comparison only, and flag excluded cases for separate professional or domain-specific analysis.

## Reference(s):

- [Debt Payoff Math Reference](references/payoff-math.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/debt-blitz-planner)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; the bundled script can also emit JSON or CSV payoff schedules.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local calculation only; user-provided debt figures are processed by the script without network or financial account access according to security evidence.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
