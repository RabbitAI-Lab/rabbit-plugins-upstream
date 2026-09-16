## Description:

Iru (Kandji) helps agents search and read Kandji blueprints and directory users through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Kandji blueprint and directory-user information from an OOMOL-connected Iru (Kandji) account. The skill is intended for read-oriented investigation and lookup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct internet installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a trusted, verified channel, inspect vendor guidance first, and do not run curl-to-shell or PowerShell download-to-execute commands blindly.

Risk: Authentication, app connection, billing, and any future write or destructive actions could affect access or account state.

Mitigation: Treat login, connection, billing, and state-changing actions as explicit user decisions; confirm the exact target, payload, and effect before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kandji)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Iru homepage](https://www.iru.com/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
