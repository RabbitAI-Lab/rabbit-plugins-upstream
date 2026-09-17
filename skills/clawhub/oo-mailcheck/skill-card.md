## Description:

Mailcheck (usercheck.com) enables an agent to inspect account status, validate domains, and verify email addresses through an OOMOL-connected Mailcheck account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected Mailcheck account use this skill to check account details, monitor API usage, validate domains, and verify individual email deliverability or risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path asks users to run a downloaded installer script directly in the shell.

Mitigation: Review the installer path first and prefer official, signed, version-pinned, or package-managed oo CLI installation instructions.

Risk: Mailcheck lookups may send queried emails, domains, and account information through OOMOL/Mailcheck.

Mitigation: Use the skill only with data appropriate for the connected OOMOL/Mailcheck account and applicable privacy requirements.

## Reference(s):

- [Mailcheck ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailcheck)
- [Mailcheck Homepage](https://www.usercheck.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; queried emails, domains, and account information may be sent through OOMOL/Mailcheck.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
