## Description:

RAWG lets agents search and read RAWG video game database records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search, inspect, and retrieve RAWG video game catalog data, including games, platforms, stores, genres, tags, developers, publishers, screenshots, movies, Reddit posts, and related series.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends piping a remote installer directly into a shell.

Mitigation: Use a trusted installation path such as manually downloading and verifying the installer or installing the oo CLI from a signed package-manager source before enabling the skill.

Risk: The skill depends on an authenticated OOMOL-connected RAWG account and can fail when credentials, scopes, app readiness, or billing are not in good standing.

Mitigation: Run setup only after an auth or connection failure, then resolve the specific account, connection, scope, expiration, app, or billing condition before retrying.

## Reference(s):

- [RAWG homepage](https://rawg.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [RAWG skill on ClawHub](https://clawhub.ai/oomol/skills/oo-rawg)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses read-only RAWG connector actions and returns connector responses containing data plus execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
