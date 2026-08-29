## Description:

Humaans (humaans.io). Use this skill for ANY Humaans request - searching and reading data. Whenever a task involves Humaans, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and agents with an OOMOL-connected Humaans account use this skill to search and read Humaans people records, token details, and paginated people lists through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Humaans people records available to the connected account, including sensitive HR profile data when private read scopes are granted.

Mitigation: Install only for accounts and scopes appropriate to the task, review granted Humaans scopes before use, and avoid exposing results beyond authorized recipients.

Risk: Connection, scope, credential, or billing errors can block connector execution.

Mitigation: Use the documented first-time setup and troubleshooting steps only after a command fails with the matching error.

## Reference(s):

- [Humaans homepage](https://humaans.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-humaans)
- [OOMOL Humaans connection](https://console.oomol.com/app-connections?provider=humaans)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON, Text guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector actions return data with meta.executionId when run with --json.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
