## Description:

kiaaccess helps agents use a user's Kia Access account to read vehicle status, location, EV charging information, and run confirm-gated vehicle commands through the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent answer questions about their Kia vehicle and perform carefully confirmed remote actions such as climate, charging, and lock commands through the user's own Kia account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server needs Kia account credentials or a long-lived refresh token, which can expose vehicle account access if stored in shared or poorly protected configuration.

Mitigation: Protect MCP configuration and backups, avoid storing secrets in shared project files, prefer read-only KIA_WRITE_MODE=none unless commands are required, and use kia_forget_session when a machine should no longer be trusted.

Risk: Remote commands can affect a real vehicle, including unlocking doors or changing climate and charging behavior.

Mitigation: Require explicit user confirmation for every command, keep write mode scoped to the needed capability, and verify resulting state with vehicle status when the command result is not confirmed.

Risk: Vehicle status and location reads can be stale or sensitive.

Mitigation: Explain cached or last-reported data clearly, refresh and re-read when freshness matters, and avoid exposing location or account details unnecessarily.

Risk: Repeated rejected login attempts can trigger Kia account protections that block server-side login.

Mitigation: Stop after a rejected login and ask the user to verify credentials in the Kia Access app instead of retrying guessed passwords.

## Reference(s):

- [ClawHub kiaaccess skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [chrischall publisher profile](https://clawhub.ai/user/chrischall)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [text, configuration, shell commands, guidance]

**Output Format:** [Markdown with inline JSON configuration and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide confirm-gated MCP reads or commands against the user's configured Kia account.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
