## Description:

API-SPORTS (api-sports.io). Use this skill for API-SPORTS search and read requests through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve API-SPORTS football data, including fixtures, standings, statistics, predictions, injuries, leagues, players, teams, squads, and top scorers through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documentation includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Do not allow an agent to run those installer commands automatically; install the oo CLI only from a trusted source with explicit user approval and a verifiable, versioned method.

## Reference(s):

- [ClawHub API-SPORTS skill](https://clawhub.ai/oomol/skills/oo-api-sports)
- [API-SPORTS homepage](https://api-sports.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before API-SPORTS requests and returns connector responses that include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
