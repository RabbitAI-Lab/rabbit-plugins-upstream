## Description:

Use kiaaccess to help an agent read Kia vehicle status, location, and EV charge data, and to perform confirm-gated climate, charging, and door commands through a user's Kia Access account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect and manage their own Kia vehicle through Kia Access, including vehicle status, location, charging, climate, and lock state workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plaintext Kia credentials or an exported refresh token could expose the user's Kia account and vehicle controls.

Mitigation: Prefer KIA_WRITE_MODE=none unless commands are needed, keep credentials and tokens out of committed project configs, restrict config file permissions, and treat KIA_RMTOKEN like a password.

Risk: Door, climate, and charging commands can affect a real vehicle, including leaving it unlocked.

Mitigation: Require explicit user confirmation for every command, keep dry runs separate from real actions, and verify the vehicle state after command acceptance.

Risk: Cached status or accepted commands may not reflect the current vehicle state.

Mitigation: Refresh and re-read vehicle status when freshness matters, and report command outcomes based on confirmed state rather than acceptance alone.

Risk: Repeated rejected login attempts can trigger Kia account protections that break server-side login.

Mitigation: Stop after a rejected login and ask the user to verify credentials in the Kia Access app before trying again.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve confirm-gated vehicle commands and sensitive Kia account credentials.]

## Skill Version(s):

0.8.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
