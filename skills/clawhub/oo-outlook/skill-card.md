## Description:

Outlook (microsoft.com). Use this skill for Outlook requests involving reading, creating, sending, replying to, updating messages and drafts, and managing mailbox settings through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to operate Outlook mailboxes through the OOMOL oo CLI for profile lookup, folder and message reads, email and draft creation, replies, sending, and mailbox settings updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell remote installer commands.

Mitigation: Prefer a reviewed, version-pinned installer, or inspect and verify the downloaded script before execution.

Risk: The skill can access sensitive Outlook mailbox data through a third-party connector.

Mitigation: Install only when the user trusts OOMOL with Outlook connector access, and limit use to the connected account and intended mailbox task.

Risk: Write actions can send email, update drafts, reply to messages, or change mailbox settings.

Mitigation: Confirm every send, reply, draft update, or mailbox settings change, including the exact payload and expected effect, before running the action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-outlook)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Outlook homepage](https://www.microsoft.com/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and should fetch the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
