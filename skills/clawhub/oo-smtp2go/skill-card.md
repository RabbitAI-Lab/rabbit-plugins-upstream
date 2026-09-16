## Description:

Operates SMTP2GO through an OOMOL-connected account to read account data, inspect sender and template metadata, search activity, and send confirmed JSON emails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to inspect and operate SMTP2GO account workflows through OOMOL without handling raw API credentials. It supports account summaries, sender verification checks, template lookup, activity search, API permission review, and confirmed email sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts for the oo CLI.

Mitigation: Review the installer source and prefer a verified or package-manager installation path before using the CLI.

Risk: The send_email action can send email through the connected SMTP2GO account.

Mitigation: Confirm the exact recipients, message content, and JSON payload with the user before running the write action.

Risk: Connector actions depend on the permissions available to the connected SMTP2GO API key.

Mitigation: Review API key permissions and use the least-privileged connected account that supports the requested task.

## Reference(s):

- [SMTP2GO homepage](https://www.smtp2go.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub SMTP2GO skill page](https://clawhub.ai/oomol/skills/oo-smtp2go)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payloads or responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute SMTP2GO connector actions through the oo CLI after schema inspection; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
