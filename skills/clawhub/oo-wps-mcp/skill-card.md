## Description:

WPS MCP helps agents read, create, and update WPS cloud documents through an OOMOL-connected WPS MCP account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate WPS MCP through an OOMOL-connected account, inspecting live connector schemas and running read or confirmed write actions for WPS cloud files, folders, and document content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent actions can use the connected OOMOL/WPS MCP account to access WPS cloud document data.

Mitigation: Install and use the skill only when connected-account access is intended, and review requested actions against the user's expected WPS data access.

Risk: Write-capable actions can create WPS files or folders or otherwise change WPS state.

Mitigation: Confirm the exact payload and expected effect with the user before approving write actions.

Risk: Setup commands can install or authenticate third-party OOMOL tooling.

Mitigation: Run installer or login flows only after a command fails because setup is missing and the user trusts the OOMOL tooling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wps-mcp)
- [WPS MCP homepage](https://www.wps.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before actions; write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
