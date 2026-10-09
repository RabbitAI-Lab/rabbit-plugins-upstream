## Description:

Queries historical Ozon-wide market trend snapshots by day or calendar month through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace analysts and sellers use this skill to review daily or monthly Ozon-wide market trends and summarize changes across requested periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing Node or unpinned qhkit tooling can change the local environment.

Mitigation: Review the installation steps and preinstall trusted tooling through an approved administrator path.

Risk: Configuring a paid-service API token locally may persist credentials.

Mitigation: Prefer short-lived environment credentials where possible and avoid storing tokens in shared environments.

Risk: Market-data calls may incur variable charges.

Mitigation: Check the current estimate and obtain user approval before paid calls, especially for large queries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-market-trend)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise trend summary with optional tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results identify the platform, period, and sample size; paid calls report credits consumed.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
