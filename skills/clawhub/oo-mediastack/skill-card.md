## Description:

Mediastack lets agents search live news articles and discover news sources through an OOMOL-connected Mediastack account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search live Mediastack news articles and discover news sources through the OOMOL oo CLI without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Before installing, use OOMOL's documented installer path with a versioned download and checksum or signature verification; avoid piping remote scripts directly into a shell.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mediastack)
- [Mediastack Homepage](https://mediastack.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Mediastack search requests; responses include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
