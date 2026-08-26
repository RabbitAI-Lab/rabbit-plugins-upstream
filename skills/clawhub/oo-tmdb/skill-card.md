## Description:

TMDB (themoviedb.org). Use this skill for ANY TMDB request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to search TMDB and retrieve read-only movie, TV, person, configuration, and trending data through an OOMOL-connected TMDB account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes TMDB access through OOMOL as an intermediary.

Mitigation: Install and use it only when that intermediary model is acceptable for the user or organization.

Risk: First-time setup may require installing the oo CLI from an external installer.

Mitigation: Review the oo CLI installer before running it and install only when the oo command is missing.

Risk: Authentication or TMDB connection flows can change account state or expose users to unnecessary setup steps.

Mitigation: Run login or connection steps only after a command fails with an authentication or connection error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tmdb)
- [TMDB homepage](https://www.themoviedb.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only TMDB connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
