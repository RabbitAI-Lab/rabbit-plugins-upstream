## Description:

Logo.dev helps agents search and read Logo.dev brand data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to fetch brand metadata, search brands, and build Logo.dev image URLs for domains, names, tickers, ISINs, and crypto symbols through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Verify the oo CLI installer from official OOMOL sources before running it, and install only when the oo command is missing.

Risk: The skill uses the user's connected OOMOL/Logo.dev account for brand searches and logo lookups.

Mitigation: Use the intended account connection, and follow authentication, connection, or billing remediation only after the matching command failure occurs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-logo-dev)
- [Logo.dev Homepage](https://logo.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect the live connector schema before running Logo.dev actions.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
