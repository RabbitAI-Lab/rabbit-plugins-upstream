## Description:

RAWG (rawg.io). Use this skill for ANY RAWG request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to search and read RAWG video game catalog data through an OOMOL-connected RAWG connector. It supports lookup and listing workflows for games, developers, genres, platforms, publishers, stores, tags, media, stores, additions, Reddit posts, and related series.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands for the oo CLI.

Mitigation: Use the skill only after the oo CLI is already installed and connected; review and verify any installer through an official method before running it.

Risk: The connector depends on an OOMOL account connection, available credit, and a connected RAWG credential.

Mitigation: Run setup or reconnection steps only after an auth, connection, scope, credential, or billing error is observed.

## Reference(s):

- [RAWG homepage](https://rawg.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub RAWG skill page](https://clawhub.ai/oomol/skills/oo-rawg)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; RAWG action responses include data and an execution ID.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
