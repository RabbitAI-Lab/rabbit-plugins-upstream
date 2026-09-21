## Description:

Enables agents to work with Microsoft Clarity data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect the live Microsoft Clarity connector schema and run supported Clarity actions from an OOMOL-connected account. It is intended for reading, creating, and updating Microsoft Clarity data through governed CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may run a remote installer when the oo CLI is missing.

Mitigation: Install the oo CLI through a verified method and avoid letting an agent execute the remote installer automatically.

Risk: OOMOL mediates access to the connected Microsoft Clarity account.

Mitigation: Use this skill only when that access pattern is acceptable for the workspace and account involved.

Risk: Write-tagged actions can change Microsoft Clarity state or export data.

Mitigation: Review the live schema, exact payload, target account, and expected effect before any write-tagged action runs.

## Reference(s):

- [Microsoft Clarity](https://clarity.microsoft.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown instructions with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
