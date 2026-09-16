## Description:

Slack enables agents to read, create, update, and delete Slack data through the OOMOL-connected oo CLI and Slack connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and automation agents use this skill to operate Slack conversations, messages, files, reactions, searches, and user metadata through an authenticated OOMOL Slack connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Use official, version-pinned, verifiable installation instructions and avoid allowing an agent to automatically run remote installer commands.

Risk: Slack write and destructive actions can change, delete, or overwrite workspace data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive Slack actions.

## Reference(s):

- [Slack homepage](https://slack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Slack skill](https://clawhub.ai/oomol/skills/oo-slack)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Slack connector command payloads and action-specific confirmation guidance.]

## Skill Version(s):

1.0.9 (source: evidence release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
