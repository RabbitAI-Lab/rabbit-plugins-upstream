## Description:

Slack lets an agent read, create, update, and delete Slack data through an OOMOL-connected account instead of calling Slack APIs directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and workspace users use this skill to let an agent inspect Slack workspace data, search messages, and perform approved Slack write or delete actions through the connected OOMOL Slack account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a suspicious fallback setup path because it tells the agent to run a remote CLI installer without an integrity check or clear user approval.

Mitigation: Review the OOMOL CLI installer through an official guide, prefer a package-manager or verified release path when available, and do not let the agent run the installer automatically.

Risk: Slack write and destructive actions can modify or remove workspace messages, reactions, and files.

Mitigation: Confirm the exact channel, message, file, target, and payload with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Slack skill release](https://clawhub.ai/oomol/skills/oo-slack)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Slack homepage](https://slack.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live action schemas before constructing Slack connector payloads.]

## Skill Version(s):

1.0.10 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
