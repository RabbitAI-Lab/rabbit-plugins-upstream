## Description:

Provides agent access to read Agility CMS content, pages, sitemaps, and content models through an OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to retrieve Agility CMS content items, content lists, pages, flat and nested sitemaps, and content models from an OOMOL-connected Agility CMS account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests piping remote installer scripts directly into a shell.

Mitigation: Review the install process first, prefer a verified package or documented manual install path, and run remote scripts only after trusting the publisher and accepting the local execution risk.

Risk: The skill depends on an authenticated OOMOL Agility CMS connection.

Mitigation: Use first-time authentication or connection setup only after an oo CLI command fails with an auth or connection error, and avoid exposing raw credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-agility)
- [Agility CMS Homepage](https://agilitycms.com/)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Agility Connection](https://console.oomol.com/app-connections?provider=agility)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads; normal action output is JSON returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
