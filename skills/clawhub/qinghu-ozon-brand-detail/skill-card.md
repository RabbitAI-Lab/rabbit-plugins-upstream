## Description:

Queries Ozon brand sales details for up to 10 brand names and helps compare the results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use this skill to look up sales details for specific brands and compare brand performance before making marketplace decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating external Node/qhkit tooling may change the agent's environment.

Mitigation: Review the installation and prefer a preinstalled, pinned qhkit version.

Risk: Qinghu API token exposure and variable charges from paid brand-data queries.

Mitigation: Prefer an ephemeral environment-variable token, check the estimated credit cost, and obtain user consent before querying.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-brand-detail)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise findings and supporting brand data; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 10 brands per query; reports the platform, site, period, sample size, and credits charged when available.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
