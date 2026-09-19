## Description:

Gmail (workspace.google.com) skill for reading, creating, updating, and deleting Gmail data through the OOMOL connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Gmail connector schemas and operate an OOMOL-connected Gmail mailbox for reads, drafts, sending, labels, filters, settings, and thread workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Gmail mailbox content and settings through OOMOL.

Mitigation: Install only when granting OOMOL access to Gmail data and actions is acceptable for the deployment.

Risk: Setup includes unverified remote installer commands.

Mitigation: Use a verified package or inspect and verify the installer before running it.

Risk: Write and destructive Gmail actions can send mail, change settings, trash messages, or permanently remove data.

Mitigation: Confirm exact payloads and targets with the user before writes, deletes, trash moves, or settings changes.

## Reference(s):

- [Gmail ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gmail)
- [Gmail homepage](https://workspace.google.com/gmail/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and connector JSON responses.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
