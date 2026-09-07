## Description:

Project compound-interest growth of an investment with initial capital and monthly contributions using Vestafolio's simulator API, after asking the simulator's questions (initial capital, monthly contribution, duration, annual return, compounding frequency).

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to gather compound-interest assumptions, call Vestafolio's simulator API, and return year-by-year investment projections. It is intended for pure pre-tax compound-interest estimates, not tax, fee, loan, real-estate, or investment-advice workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Projection inputs are sent to Vestafolio's API.

Mitigation: Avoid entering real account identifiers or confidential financial details beyond the simulator fields; use a local calculation when the assumptions should remain private.

Risk: The projection can be mistaken for investment advice or a complete net-return estimate.

Mitigation: State that results are estimates only, assume constant returns and contributions, and exclude taxes and fees.

## Reference(s):

- [Vestafolio compound interest simulator](https://www.vestafolio.com/simulateurs/interets-composes)
- [Vestafolio compound interest API schema](https://www.vestafolio.com/api/tools/v1/interets-composes)
- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-interets-composes)
- [Vestafolio publisher profile](https://clawhub.ai/user/vestafolio)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown text with optional tables and inline API or shell command details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responds in French when the user writes in French; results should be grounded in the API response and include assumptions, limits, and the simulator link.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
