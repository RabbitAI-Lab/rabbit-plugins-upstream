## Description:

Gmail lets an agent operate a connected Gmail account through OOMOL's gmail connector for mailbox reads, drafts, sending, labeling, filters, settings, and deletion workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read, search, draft, send, label, organize, and manage Gmail mailbox settings through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup directs users to install the OOMOL CLI through an internet installer.

Mitigation: Review the installation path before use and prefer a signed or checksum-verified installer.

Risk: OOMOL's connector processes the Gmail requests and data needed for each action.

Mitigation: Connect Gmail only when the user is comfortable with that processing path and the requested mailbox scope.

Risk: The skill includes write and destructive Gmail actions such as sending messages, changing labels or settings, trashing messages, and deleting drafts, filters, or labels.

Mitigation: Inspect the live action schema, confirm the exact payload and effect with the user, and require explicit approval for destructive targets before execution.

## Reference(s):

- [ClawHub Gmail skill page](https://clawhub.ai/oomol/skills/oo-gmail)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gmail homepage](https://workspace.google.com/gmail/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Text with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Gmail message data, mailbox settings, file transit references for attachments, and connector execution IDs.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
