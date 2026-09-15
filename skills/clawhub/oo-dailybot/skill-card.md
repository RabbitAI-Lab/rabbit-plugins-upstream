## Description:

Dailybot (dailybot.com). Use this skill for ANY Dailybot request: reading, creating, and updating data through the OOMOL-connected Dailybot connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Dailybot action schemas and run authenticated Dailybot read and write actions through the OOMOL-connected oo CLI, including user, organization, team, conversation, email, and message workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands for the oo CLI, and the server security verdict flags this as suspicious pending review.

Mitigation: Review the installer source before use and prefer an official, versioned, signed, or checksum-verified installation path; do not allow an agent to execute remote installer commands automatically.

Risk: The skill can send Dailybot messages and email notifications, which changes state in an external service.

Mitigation: Confirm the exact payload, recipient, and expected effect with the user before running any write-tagged Dailybot action.

## Reference(s):

- [ClawHub Dailybot skill page](https://clawhub.ai/oomol/skills/oo-dailybot)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Dailybot homepage](https://www.dailybot.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON payload examples, and connector response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Dailybot actions require confirmation of the exact payload and effect before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
