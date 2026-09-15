## Description:

CollegeFootballData supports requests for college football account information, conferences, games and results, teams, and venues through the OOMOL CollegeFootballData connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve CollegeFootballData information through an OOMOL-connected account without handling raw API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documentation includes unverified remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Prefer the official installation guide, a versioned package, and checksum or signature verification before installing the oo CLI.

Risk: The skill uses an OOMOL-connected CollegeFootballData account, so connector access may expose account details such as patron level and remaining calls.

Mitigation: Connect only the OOMOL and CollegeFootballData account intended for this skill and review connector access before use.

## Reference(s):

- [CollegeFootballData homepage](https://collegefootballdata.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-college-football-data)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include CollegeFootballData connector results returned by the oo CLI as JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
