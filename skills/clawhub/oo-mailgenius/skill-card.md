## Description:

MailGenius helps agents operate MailGenius through an OOMOL-connected account to create email audits, retrieve audit results, list audits, and check daily limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run MailGenius deliverability audit workflows from an agent, including generating test email addresses, retrieving results, listing audits, and checking API usage limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute downloaded scripts.

Mitigation: Review the oo CLI installation source before use, prefer a versioned installer or package-manager flow with signature or checksum verification, and do not allow an agent to run pipe-to-shell setup commands automatically.

Risk: The create_email_audit action changes MailGenius state and may consume daily test capacity.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and check daily limits when capacity matters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailgenius)
- [MailGenius Homepage](https://www.mailgenius.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and authenticated oo CLI connected to MailGenius; write actions should be confirmed before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
