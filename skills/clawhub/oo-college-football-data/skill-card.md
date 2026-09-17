## Description:

CollegeFootballData helps agents inspect schemas and read college football account, conference, game, team, and venue data through the OOMOL CollegeFootballData connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query CollegeFootballData through an OOMOL-connected account without handling raw CollegeFootballData API tokens directly. It supports account lookup and read-only listing of conferences, games, teams, and venues with schema inspection before connector calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote installer scripts through a shell.

Mitigation: Prefer a verified, versioned installer or documented package source before installing the oo CLI.

Risk: Use depends on an authenticated OOMOL account and connected CollegeFootballData credentials.

Mitigation: Confirm the oo CLI is installed, authenticated, and connected only when connector commands fail with authentication, scope, or connection errors.

## Reference(s):

- [CollegeFootballData homepage](https://collegefootballdata.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector calls return JSON containing data and meta.executionId when run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
