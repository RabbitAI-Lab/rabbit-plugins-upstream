## Description:

Kickbox (kickbox.com) helps agents verify email deliverability and check whether an address or domain uses a disposable email provider through an OOMOL-connected Kickbox account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to verify individual email addresses, retrieve Kickbox risk signals, and check disposable email status from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Before installation, prefer a package-managed or checksum-verified oo CLI path when available and avoid running the remote installer from an elevated shell.

Risk: Email and domain checks are sent through OOMOL and Kickbox using the connected account.

Mitigation: Use the skill only for Kickbox checks the user intends to send through those services.

## Reference(s):

- [ClawHub Kickbox Skill Page](https://clawhub.ai/oomol/skills/oo-kickbox)
- [Kickbox Homepage](https://kickbox.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
