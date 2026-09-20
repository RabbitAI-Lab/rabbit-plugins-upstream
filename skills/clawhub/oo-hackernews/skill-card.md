## Description:

Provides agent access to Hacker News for searching and reading stories, comments, updates, and user profiles through the OOMOL oo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Hacker News posts, stories, comments, updates, and public user profiles without constructing connector calls directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running unverified remote installer scripts directly in a shell.

Mitigation: Prefer installing the oo CLI through a trusted, verifiable method with version pinning or checksum/signature verification, and do not let an agent run the remote installer automatically just because oo is missing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hackernews)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Hacker News](https://news.ycombinator.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Hacker News actions by default; inspect the live connector schema before constructing a payload.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
