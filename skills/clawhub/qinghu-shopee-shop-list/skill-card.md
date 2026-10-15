## Description:

Filters T+1 Shopee shop records by category, shop type, local or cross-border status, and opening date using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market researchers use this skill to find comparable shops or newly opened stores across supported sites, filtering by category and shop attributes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update Node and qhkit globally or change the local PATH.

Mitigation: Use platform-managed or reviewed installation; pin package versions where possible and require explicit approval before global installs or PATH changes.

Risk: Qinghu API credentials may be stored in local configuration.

Mitigation: Require user approval before storing a token and use a secure, user-controlled credential mechanism.

Risk: Data queries consume paid Qinghu credits, including potentially failed service calls.

Mitigation: Show the estimated cost and obtain explicit approval before paid calls; limit retries and report actual credits charged.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-shop-list)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written summary and tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the Shopee site, reporting period, sample size, and credits charged for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
