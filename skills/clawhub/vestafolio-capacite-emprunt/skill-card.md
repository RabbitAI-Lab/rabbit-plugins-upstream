## Description:

Estimate the maximum mortgage a French household can borrow from income, existing charges and the HCSF 35 % debt ratio using Vestafolio's simulator API, after asking the simulator's questions (net household income, fixed charges, rate, duration, insurance rate).

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to estimate mortgage borrowing capacity for a French household before a property search. It asks for income, fixed charges, loan rate, duration and insurance rate, then grounds the answer in Vestafolio's simulator API output.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: Borrowing-capacity inputs such as household income and fixed charges are sent to Vestafolio's API for calculation.

Mitigation: Install and use the skill only when API processing by Vestafolio is acceptable; avoid real personal financial details when a local rough estimate is sufficient.

Risk: The result is an estimate and not a bank pre-approval or financial advice.

Mitigation: State the simulator assumptions and caveats in the response, including that final borrowing capacity depends on lender review.

Risk: If network access is unavailable or the API fails, a personalized calculation cannot be completed.

Mitigation: Do not invent a result; explain that the calculation could not be completed and provide the interactive simulator link.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-capacite-emprunt)
- [Vestafolio capacite-emprunt API](https://www.vestafolio.com/api/tools/v1/capacite-emprunt)
- [Vestafolio interactive simulator](https://www.vestafolio.com/simulateurs/capacite-emprunt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown response grounded in API results, with optional inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responds in French when the user writes in French; explains assumptions, caveats and the simulator link.]

## Skill Version(s):

1.2.0 (source: frontmatter; release evidence version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
