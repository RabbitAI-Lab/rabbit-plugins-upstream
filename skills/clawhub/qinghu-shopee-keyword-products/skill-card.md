## Description:

Queries popular Shopee products associated with a hot-search term ID through Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to identify popular products associated with a specified hot-search term, site, and reporting date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node.js and the Qinghu qhkit CLI on the host.

Mitigation: Review installation steps and preinstall a pinned qhkit version instead of allowing automatic tool installation.

Risk: Configuring a Qinghu API token may store a long-lived credential.

Mitigation: Provide the token through a temporary environment variable rather than saving it in persistent configuration.

Risk: Qinghu data lookups can incur paid API charges.

Mitigation: Check the current credit estimate and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-keyword-products)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written findings with product previews and a table file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results reflect recorded rather than real-time Shopee data; include site, reporting period, sample size, and credits spent when applicable.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
