## Description:

iTunes Search API (performance-partners.apple.com). Use this skill for ANY iTunes Search API request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search the iTunes Store and Apple Books Store or look up store records by identifier through OOMOL's oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl-to-bash and PowerShell remote installer one-liners.

Mitigation: Before installing the oo CLI, prefer an official package manager or download-and-verify process rather than executing a remote installer directly.

Risk: The skill relies on OOMOL's oo CLI and account flow to broker connector access.

Mitigation: Use the skill only when that dependency and account flow are acceptable for the deployment environment.

## Reference(s):

- [iTunes Search API homepage](https://performance-partners.apple.com/search-api)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-itunes-search)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only store search and lookup results are returned through the oo CLI connector.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
