## Description:

Computes French mortgage monthly payments, total interest, insurance cost, and amortization schedules using Vestafolio's simulator API after collecting the required loan inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to estimate fixed-rate French mortgage monthly payments, total interest, insurance cost, and amortization schedules after providing the principal, annual rate, loan duration, and insurance rate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loan parameters are sent to Vestafolio's HTTPS API for calculation.

Mitigation: Disclose the API transfer before use and collect only the loan inputs required by the simulator.

Risk: Mortgage outputs may be mistaken for financial advice or a binding loan offer.

Mitigation: State that results are estimates and note that fees such as application, guarantee, and other TAEG components are not modeled.

Risk: API failure, network unavailability, or schema changes could prevent a grounded calculation.

Mitigation: Fetch the current schema, check successful responses, and avoid inventing results when the API cannot complete the simulation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-credit-immobilier)
- [Vestafolio credit immobilier API](https://www.vestafolio.com/api/tools/v1/credit-immobilier)
- [Vestafolio credit immobilier simulator](https://www.vestafolio.com/simulateurs/credit-immobilier)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown with calculation summaries and optional amortization tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Grounded in Vestafolio HTTPS API results; replies in French when the user writes in French.]

## Skill Version(s):

1.2.0 (source: artifact/SKILL.md frontmatter and release changelog; target release metadata version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
