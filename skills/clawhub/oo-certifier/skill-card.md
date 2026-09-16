## Description:

Certifier (certifier.io) helps agents read, create, update, issue, and send Certifier data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Certifier connector schemas, list or search Certifier records, and create, issue, or send credentials through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to run remote installer scripts directly in a shell.

Mitigation: Review setup commands before installation and prefer a pinned official release or package manager with signature or checksum verification.

Risk: The create_issue_send_credential action creates, issues, and sends Certifier credentials.

Mitigation: Confirm the exact recipient, group, credential details, and send effect with the user before running the write action.

## Reference(s):

- [ClawHub Certifier skill page](https://clawhub.ai/oomol/skills/oo-certifier)
- [Certifier homepage](https://certifier.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before payload construction; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
