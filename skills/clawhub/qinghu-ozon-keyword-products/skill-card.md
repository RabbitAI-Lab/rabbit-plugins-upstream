## Description:

Looks up products associated with Ozon keyword IDs, with optional price, product-type, and reporting-period filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use the skill to find products and competitors associated with known keyword IDs and compare results within selected price ranges or reporting periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install or update Node and the qhkit package at runtime.

Mitigation: Review installation steps and package trust before execution; prefer a platform-managed or pinned qhkit installation.

Risk: Qinghu API credentials may be persisted in local configuration or exposed through command arguments.

Mitigation: Keep tokens in a secret manager or temporary environment variable when possible, and avoid exposing them in logs or shell history.

Risk: Product lookups consume paid Qinghu credits, and charges can increase with result volume.

Mitigation: Estimate cost and obtain user approval before paid calls, especially for large or repeated queries.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ozon-keyword-products)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary or exported table file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a brief result preview and total Qinghu credits consumed.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
