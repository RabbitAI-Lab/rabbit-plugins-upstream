## Description:

SportsDataIO helps an agent use the OOMOL sportsdata connector through the oo CLI for SportsDataIO requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SportsDataIO data through an OOMOL-connected account, including sports, competitions, seasons, teams, venues, schedules, and event results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can run code on the user's machine.

Mitigation: Use official signed packages when available, or download the installer and verify its checksum or signature before running it.

Risk: The skill uses the user's connected OOMOL/SportsDataIO account through the oo CLI.

Mitigation: Confirm write-tagged action payloads and expected account effects with the user before execution.

## Reference(s):

- [SportsDataIO homepage](https://sportsdata.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub SportsDataIO skill page](https://clawhub.ai/oomol/skills/oo-sportsdata)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands rely on the oo CLI and a connected OOMOL/SportsDataIO account.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
