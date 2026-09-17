## Description:

Census Bureau (census.gov). Use this skill for ANY Census Bureau request: searching and reading data through the OOMOL Census Bureau connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to discover Census Bureau datasets, inspect variables and groups, and query public Census Data API datasets through the OOMOL `oo` CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions direct users or agents to run mutable remote installer scripts.

Mitigation: Review setup instructions before installing, prefer a version-pinned or verified `oo` CLI installation method where available, and run setup only when an auth, connection, or missing-CLI error requires it.

Risk: The skill depends on trusting OOMOL's `oo` CLI and installer delivery path.

Mitigation: Use the skill only when that dependency is acceptable for the environment; once installed and connected, use the documented read-oriented Census actions.

## Reference(s):

- [ClawHub Census Bureau Skill](https://clawhub.ai/oomol/skills/oo-census-bureau)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Census Bureau Homepage](https://www.census.gov)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before constructing connector request payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
