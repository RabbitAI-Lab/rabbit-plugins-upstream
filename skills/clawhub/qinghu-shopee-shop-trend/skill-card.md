## Description:

Queries up to 720 days of Shopee shop trends by month, quarter, or year, with optional category and product filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shop operators and market analysts use this skill to assess longer-term Shopee shop growth and sales trends across supported sites and reporting periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance may install or upgrade Node and npm packages and change the local PATH without a separate approval step.

Mitigation: Require explicit approval before setup commands and prefer a pinned qhkit version.

Risk: Configuring the Qinghu API token in a visible shell command can expose a secret.

Mitigation: Supply the token through a safer secret mechanism rather than a visible command.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-shop-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Text, Files]

**Output Format:** [Concise trend summary with supporting figures; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports site, period, sample size, and credits spent on paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
