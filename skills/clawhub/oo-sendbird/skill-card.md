## Description:

Sendbird lets an agent manage Sendbird users, group channels, messages, moderation, unread counts, and session tokens through the OOMOL `oo` connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Sendbird connector schemas and run Sendbird actions for user, channel, message, moderation, unread-count, and session-token workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands may execute code from OOMOL's CLI distribution path.

Mitigation: Use a trusted installation path or independently verify the installer before running it.

Risk: Sendbird write, destructive, moderation, and token actions can change or remove users, channels, messages, bans, and session tokens.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running state-changing actions.

Risk: Incorrect payloads can cause failed or unintended connector actions.

Mitigation: Inspect the live action schema before constructing each payload.

## Reference(s):

- [ClawHub Sendbird skill page](https://clawhub.ai/oomol/skills/oo-sendbird)
- [Sendbird homepage](https://sendbird.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions can return JSON responses that include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
