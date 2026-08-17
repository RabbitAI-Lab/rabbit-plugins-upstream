## Description:

Gmail skill for reading, creating, updating, and deleting Gmail data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a connected Gmail mailbox, including reading messages, drafting or sending mail, organizing labels, managing filters, and updating Gmail settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and manage a connected Gmail account, including sensitive mailbox content and account settings.

Mitigation: Install and use it only when OOMOL-connected tooling is trusted for the mailbox being accessed.

Risk: State-changing Gmail operations can send mail, delete or trash items, update labels, filters, forwarding, and settings.

Mitigation: Review the exact payload and effect before approving send, delete, trash, filter, forwarding, label, or settings changes.

Risk: First-time CLI installation and authentication flows establish access paths to the connected Gmail account.

Mitigation: Run the CLI install or auth flow only after confirming that OOMOL is trusted in the deployment environment.

## Reference(s):

- [Gmail homepage](https://workspace.google.com/gmail/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI commands that return Gmail connector JSON responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
