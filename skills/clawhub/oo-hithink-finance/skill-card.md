## Description:

Provides agent guidance for searching and reading Tonghuashun Financial Data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Tonghuashun A-share and public-fund data through an authenticated OOMOL connector, including market snapshots, historical prices, financial statements, fund holdings, and bulk exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code on the user's machine.

Mitigation: Verify and trust the oo CLI installer source before running installer commands; use setup steps only after a command fails because the CLI is missing or authentication is unavailable.

Risk: Large export actions may upload datasets to transit storage.

Mitigation: Confirm the intended export action, dataset scope, and storage expectations with the user before running bulk export actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hithink-finance)
- [Tonghuashun Financial Data Homepage](https://fuyao.aicubes.cn/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include data and meta.executionId; export actions may create Parquet datasets in transit storage.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
