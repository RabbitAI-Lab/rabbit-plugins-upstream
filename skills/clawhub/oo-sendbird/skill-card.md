## Description:

Sendbird (sendbird.com). Use this skill for ANY Sendbird request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Sendbird users, group channels, messages, moderation actions, unread counts, and session tokens through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes remote installer commands for the oo CLI that could be unsafe if run blindly.

Mitigation: Use a verified or administrator-approved OOMOL CLI installation path before running Sendbird actions.

Risk: The unban_user action changes access control but is not marked as a write action in the artifact.

Mitigation: Require explicit approval before running unban_user and other access-control changes.

Risk: The skill can read and change Sendbird users, channels, messages, bans, mutes, and session tokens.

Mitigation: Install and use it only with a Sendbird account where OOMOL is approved for those permissions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sendbird)
- [Sendbird Homepage](https://sendbird.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger Sendbird read, write, or destructive operations through the oo CLI after schema inspection and required confirmations.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
