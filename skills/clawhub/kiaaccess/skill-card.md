## Description:

This skill connects an agent to a user's Kia Access / Kia Owners account to check vehicle status, location, EV charge state, and run explicitly confirmed door, climate, and charging commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent interact with their own Kia account for vehicle reads and explicitly confirmed comfort, charging, and lock/unlock workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a user's Kia account and stored refresh token.

Mitigation: Install only from trusted sources, protect KIA_RMTOKEN like a password, and export it only to deployments the user controls.

Risk: Vehicle commands can affect a real vehicle, including unlocking doors or changing climate and charging state.

Mitigation: Prefer KIA_WRITE_MODE=none or comfort unless door lock and unlock are required, require explicit user confirmation before commands, and verify state after accepted commands.

Risk: Cached status or last reported location can be stale.

Mitigation: Use kia_refresh_status and then re-read status when freshness matters, and describe location as last reported rather than live.

Risk: Repeated failed logins can lead to account challenges that block server-side login.

Mitigation: Stop after a rejected login and have the user verify credentials in the Kia Access app before trying again.

## Reference(s):

- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)
- [kiaaccess-mcp source repository](https://github.com/chrischall/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown with JSON configuration and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Kia account credentials, MFA bootstrap when no session exists, and explicit confirmation for vehicle commands.]

## Skill Version(s):

0.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
