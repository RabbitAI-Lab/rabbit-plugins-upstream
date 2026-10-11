## Description:

Queries popular products from an Ozon shop by name or ID, with optional category, period, sorting, and pagination filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and analysts use this skill to review an Ozon shop's popular products and compare sales, revenue, or prices across categories and reporting periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install or update Node and qhkit, potentially changing local tooling or shell configuration.

Mitigation: Preinstall and pin a trusted qhkit version; review and approve any environment changes before execution.

Risk: Configuring a Qinghu API token could expose credentials if entered into commands or shell profiles.

Mitigation: Supply the token through an environment variable and avoid storing it in shell profiles or sharing command output.

Risk: Product queries are paid and larger responses may consume additional Qinghu credits.

Mitigation: Estimate charges, obtain user approval before paid calls, and limit batch size.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ozon-shop-products)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Concise Markdown findings with optional tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should identify the Ozon shop, reporting period, and sample size; paid queries consume Qinghu credits.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
