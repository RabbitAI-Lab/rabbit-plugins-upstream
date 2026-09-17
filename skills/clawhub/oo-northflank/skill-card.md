## Description:

Northflank (northflank.com). Use this skill for ANY Northflank request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Northflank projects and services through an OOMOL-connected account. It supports read-oriented get and list workflows after checking the live connector schema for each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes remote installer commands for the oo CLI.

Mitigation: Avoid running remote installer commands directly unless the installer is verified through a trusted channel.

Risk: Connector action scope may be broader than the skill's read-only description.

Mitigation: Restrict use to the listed get and list actions unless the user explicitly approves a state-changing operation.

Risk: The skill uses OOMOL-mediated access to the user's Northflank account.

Mitigation: Install and use the skill only when OOMOL-mediated account access is acceptable for the deployment context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-northflank)
- [Northflank homepage](https://northflank.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Northflank app connection](https://console.oomol.com/app-connections?provider=northflank)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
