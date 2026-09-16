## Description:

Access football-data.org through OOMOL's football_data connector to retrieve competitions, teams, standings, and match data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer football-data.org data requests by listing competitions, teams, standings, matches, or retrieving a match after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI through a verified, pinned, signed, or package-manager route, and avoid running remote installer commands from an elevated shell.

Risk: Connector input and output contracts may change over time.

Mitigation: Inspect the live connector schema before each action and build payloads only from the returned schema.

## Reference(s):

- [football-data.org homepage](https://www.football-data.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-football-data)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building JSON payloads; football-data.org actions listed in the artifact are read-only.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
