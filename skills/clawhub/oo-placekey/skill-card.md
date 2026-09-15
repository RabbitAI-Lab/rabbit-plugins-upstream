## Description:

Placekey helps agents search and read Placekey data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to resolve addresses into geocodes or Placekey identifiers, including single-location and bulk lookups, through an OOMOL-connected Placekey account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute remote installer scripts on the user's machine.

Mitigation: Prefer OOMOL's official install guide or a package manager path with version and integrity checks; avoid piping remote installer scripts directly into bash or PowerShell in sensitive environments.

Risk: Placekey access depends on OOMOL as the intermediary for authentication and connector execution.

Mitigation: Install and use the skill only when the user accepts OOMOL's role as the intermediary for Placekey.

## Reference(s):

- [ClawHub Placekey skill page](https://clawhub.ai/oomol/skills/oo-placekey)
- [Placekey homepage](https://www.placekey.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run with --json.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
