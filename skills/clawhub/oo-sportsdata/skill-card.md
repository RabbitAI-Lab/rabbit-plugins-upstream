## Description:

SportsDataIO helps agents operate the SportsDataIO connector through an OOMOL-connected account for sports data lookup and supported update workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to query SportsDataIO sports, competitions, seasons, teams, venues, schedules, live results, and final results through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance can execute an installer script when the oo CLI is missing.

Mitigation: Prefer a verified, version-pinned oo CLI package or download and inspect the installer before execution.

Risk: Inline JSON passed through shell commands can expose local command-construction risk when user-controlled data is embedded directly.

Mitigation: Use @file JSON input or argument-safe process execution for connector payloads.

Risk: Schedule-list actions are tagged as write actions in the artifact and evidence flags those tags as questionable.

Mitigation: Confirm the action schema, payload, and intended effect before running schedule-list actions until the publisher corrects the metadata.

## Reference(s):

- [ClawHub SportsDataIO skill page](https://clawhub.ai/oomol/skills/oo-sportsdata)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [SportsDataIO homepage](https://sportsdata.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before connector execution.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
