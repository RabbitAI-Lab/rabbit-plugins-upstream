## Description:

Anymail Finder helps an agent search for verified company, decision-maker, and individual work email data and check email deliverability through an OOMOL-connected Anymail Finder account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to find verified work email addresses, inspect Anymail Finder account credits, or verify email deliverability through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback first-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Avoid running pipe-to-shell setup commands blindly; prefer an official versioned installer or package-manager path with integrity verification.

Risk: The skill operates through OOMOL as the connector for an Anymail Finder account.

Mitigation: Install only if OOMOL is an acceptable connector and connect only the Anymail Finder account the agent is intended to use.

## Reference(s):

- [Anymail Finder Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-anymail-finder)
- [Anymail Finder homepage](https://anymailfinder.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
