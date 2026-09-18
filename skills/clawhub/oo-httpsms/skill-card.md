## Description:

httpSMS helps an agent read, create, update, and delete httpSMS data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage httpSMS account, phone, billing, thread, message, send, and delete workflows from an agent while relying on OOMOL for connector access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remote installer directly.

Mitigation: Review the oo CLI installation path first and prefer a verified package or download-and-inspect workflow instead of piping the installer into Bash or PowerShell.

Risk: OOMOL brokers access to the connected httpSMS account.

Mitigation: Install only when that account-broker role is acceptable for the deployment and connection policy.

Risk: Send and delete actions can change or remove httpSMS messages.

Mitigation: Confirm the exact payload and effect before sending messages, and require explicit approval for destructive deletes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-httpsms)
- [httpSMS homepage](https://httpsms.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
