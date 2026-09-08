## Description:

Simulate early retirement funded by invested capital for a French saver using Vestafolio's retirement-age simulator API after collecting the required financial assumptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to estimate whether invested capital, savings rate, expenses, mortgage payments, and optional complementary income can support early retirement. It is intended for FIRE-style capital drawdown scenarios, not statutory pension-rights calculations or investment product selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends savings, income, expenses, mortgage, age, and retirement assumptions to Vestafolio for calculation.

Mitigation: Use only values the user intends to share with Vestafolio, prefer rough estimates when adequate, and avoid unrelated personal details or credentials.

Risk: A generated retirement-age result could be mistaken for personalized financial advice.

Mitigation: State the simulator assumptions and limits, ground numerical claims in the API output, and present the result as an estimate rather than financial advice.

Risk: If API execution or network access fails, an agent could provide an unsupported numerical answer.

Mitigation: Do not invent simulation results; explain that the calculation could not be completed and provide the interactive Vestafolio simulator link.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-age-retraite)
- [Vestafolio retirement-age simulator](https://www.vestafolio.com/simulateurs/age-retraite)
- [Vestafolio retirement-age API schema endpoint](https://www.vestafolio.com/api/tools/v1/age-retraite)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown response with API-grounded retirement simulation summary and optional inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should be grounded in the Vestafolio API result; if execution or network access is unavailable, the agent should link to the interactive simulator instead of inventing a result.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and auto changelog state 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
