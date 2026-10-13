## Description:

Analyzes a Shopee shop's listed brands by product count, sales volume, and sales value using a shop ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shop operators and analysts use this skill to compare the brands sold by a Shopee shop and assess their product counts, recent sales volume, and sales value.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may install or upgrade Node.js and qhkit on the user's machine.

Mitigation: Review installation steps first; prefer a preinstalled, pinned qhkit version.

Risk: The skill requires a Qinghu API token and suggests storing it in persistent configuration.

Mitigation: Provide credentials through a temporary QHKIT_TOKEN environment variable instead of persistent configuration.

Risk: Data queries may consume Qinghu credits, including when a server-side call fails.

Mitigation: Check the current estimate and get user approval before paid calls; report actual credits after each call.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-shop-brands)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key management](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written analysis; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports brand metrics with Shopee site, reporting date, and sample size; availability depends on the queried shop and site.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
