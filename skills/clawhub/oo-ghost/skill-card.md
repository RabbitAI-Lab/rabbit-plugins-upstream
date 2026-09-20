## Description:

Provides read-only access to Ghost site content and public settings through the OOMOL Ghost connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve published Ghost posts, pages, authors, tags, and public site settings from an OOMOL-connected Ghost site.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote oo CLI installer scripts directly.

Mitigation: Review the installer before running it, prefer a verified installer or documented package source, and run setup only when an auth or connection error requires it.

Risk: The connector can read public Ghost content and settings from the connected site.

Mitigation: Connect Ghost to OOMOL only for sites where this read access is acceptable.

## Reference(s):

- [ClawHub Ghost skill](https://clawhub.ai/oomol/skills/oo-ghost)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Ghost](https://ghost.org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
