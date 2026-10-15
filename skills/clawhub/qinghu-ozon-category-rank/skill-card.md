## Description:

Helps agents query and summarize Ozon category sales rankings by period, sort order, and page using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use this skill to identify top-selling categories and compare category sales data across selected periods and rankings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing qhkit may modify the local developer environment.

Mitigation: Review installation steps and prefer a preinstalled, pinned qhkit version.

Risk: Storing an API token locally may expose credentials.

Mitigation: Prefer a platform-managed secret or temporary QHKIT_TOKEN over persisting the token.

Risk: Queries may consume paid Qinghu credits, with charges varying by result volume.

Mitigation: Check the estimate and obtain user approval before paid calls, especially large requests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ozon-category-rank)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise narrative with ranking data; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should identify the platform, period, and sample size; paid calls should report credits consumed.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
