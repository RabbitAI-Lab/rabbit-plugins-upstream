## Description:

This skill helps agents search and read TMDB data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect TMDB connector schemas and retrieve movie, TV, person, image configuration, search, and trending data through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback recommends running an unverified remote installer directly in a shell.

Mitigation: Review the installer source and use official, version-pinned installation steps with checksum or signature verification before using the skill.

Risk: An agent could attempt first-time setup or authentication actions automatically.

Mitigation: Do not let an agent run the remote installer or authentication flow automatically; install and authenticate the oo CLI yourself if you trust OOMOL and need TMDB access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tmdb)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [TMDB homepage](https://www.themoviedb.org)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
