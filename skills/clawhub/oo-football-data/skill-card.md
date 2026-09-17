## Description:

Enables agents to query football-data.org data through the OOMOL football_data connector using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to list football competitions, teams, standings, and matches, or retrieve a match by identifier through a connected football-data.org account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback suggests executing a remote installer script directly in the shell.

Mitigation: Review before installing; install the oo CLI only from a trusted, verified source, preferably with a pinned or signed package and user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-football-data)
- [football-data.org homepage](https://www.football-data.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses server-side OOMOL credential handling for the connected football-data.org account.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
