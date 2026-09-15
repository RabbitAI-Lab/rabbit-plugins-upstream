## Description:

TMDB helps agents search and read TMDB movie, TV, person, trending, and image-configuration data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve TMDB movie, TV, person, search, trending, and image configuration details through an OOMOL-connected account without handling raw TMDB credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include mutable remote installer commands executed directly in a shell.

Mitigation: Use the skill only after a trusted oo CLI installation is already available; prefer an official package manager or download-and-verify flow and review installers before execution.

## Reference(s):

- [ClawHub TMDB Skill](https://clawhub.ai/oomol/skills/oo-tmdb)
- [TMDB Homepage](https://www.themoviedb.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
