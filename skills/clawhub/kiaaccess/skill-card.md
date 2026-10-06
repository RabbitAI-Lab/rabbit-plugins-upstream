## Description:

Helps Kia owners check vehicle status, location, and charging and request confirmation-gated vehicle commands through their Kia account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and their assistants use this skill to review vehicle status, location, and EV charging details and, with explicit approval, control doors, climate, or charging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kia account credentials and exported session tokens can grant access to sensitive vehicle information and controls.

Mitigation: Store credentials in private configuration, never commit or echo them, and export session tokens only with explicit approval.

Risk: Commands can unlock a vehicle or change climate and charging settings.

Mitigation: Start with read-only mode when possible; explicitly confirm every command and enable door controls only when needed.

Risk: Cached readings and accepted commands can be mistaken for confirmed vehicle state.

Mitigation: Refresh and re-read status when freshness matters; verify state after commands without blindly repeating them.

## Reference(s):

- [kiaaccess ClawHub listing](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text with vehicle readings and command status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vehicle reads may be stale; accepted commands do not guarantee the vehicle changed state.]

## Skill Version(s):

1.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
