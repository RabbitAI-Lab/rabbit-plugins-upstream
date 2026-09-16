## Description:

Chorus (chorus.ai). Use this skill for ANY Chorus request - searching and reading data. Whenever a task involves Chorus, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected Chorus account use this skill to inspect Chorus action schemas and retrieve conversations, teams, scorecards, engagements, and current-user details through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified internet installer commands for the oo CLI, and the security verdict flags the release as suspicious for that reason.

Mitigation: Review the installer source before execution; prefer a verified package, pinned release, checksum or signature validation, and only run setup when the CLI is missing.

Risk: The connector uses an OOMOL-connected Chorus account, so retrieved Chorus data is limited by the connected account's scopes and may include sensitive business information.

Mitigation: Connect Chorus with the least permissions needed and avoid requesting or exposing data beyond the user's task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-chorus)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Chorus homepage](https://www.chorus.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute read-only Chorus connector actions through the oo CLI and return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
