## Description:

Operates Google Search Console through OOMOL's google_search_console connector for reading, creating, updating, and deleting Search Console data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and SEO operators use this skill to list and manage Google Search Console properties and sitemaps, inspect indexed URLs, and query search analytics through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes mutable remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Prefer a pinned, signed, or package-manager installation path, and review installer contents before execution.

Risk: Write and destructive actions can change or remove Google Search Console properties and sitemaps.

Mitigation: Confirm the exact payload, target, and expected effect before running any write or destructive action.

Risk: Google Search Console actions depend on OOMOL as an intermediary for account-connected operations.

Mitigation: Install only when the user accepts OOMOL's role in brokering Google Search Console actions and credential handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-google-search-console)
- [Google Search Console](https://search.google.com/search-console)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-connected credentials server-side and returns connector responses as JSON when actions run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
