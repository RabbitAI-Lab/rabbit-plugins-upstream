## Description:

Queries up to 90 days of Ozon shop trend snapshots by shop name or ID using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use this skill to review a single shop's historical trends and assess growth over a requested period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install or upgrade qhkit and Node on the host and fetch npm packages.

Mitigation: Review changes before installation; prefer a sandbox or a preinstalled, pinned qhkit version.

Risk: Configuring qhkit can persist a Qinghu API token on the host.

Mitigation: Prefer an invocation-scoped token and avoid storing credentials on shared machines.

Risk: Shop trend requests consume paid Qinghu credits, potentially increasing with result count.

Mitigation: Estimate the charge and obtain user consent before making paid requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-shop-trend)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Brief trend summary with supporting figures; table file for 10 or more records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports platform, period, sample size and credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
