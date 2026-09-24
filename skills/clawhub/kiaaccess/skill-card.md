## Description:

This skill should be used when the user asks about their Kia vehicle through the Kia Access / Kia Owners account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to read Kia vehicle status, location, EV charge information, and to perform confirm-gated Kia Access commands such as climate, charging, lock, and unlock actions through the user's own Kia account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Kia account credentials, persistent session tokens, vehicle location data, and remote vehicle commands.

Mitigation: Install only in trusted environments, protect MCP configuration files and exported refresh tokens, and use read-only KIA_WRITE_MODE=none unless command tools are required.

Risk: Door, climate, and charging commands can affect a real vehicle, and command acceptance does not always mean the vehicle state changed.

Mitigation: Require explicit user confirmation for every command, treat dry runs as previews only, and verify command results by re-reading vehicle status instead of retrying blindly.

Risk: Rejected logins may trigger account protections that block server-side login.

Mitigation: Stop after a rejected login, ask the user to verify credentials in the Kia Access app, and avoid guessing or retrying passwords.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [npm package](https://www.npmjs.com/package/kiaaccess-mcp)
- [Source repository](https://github.com/chrischall/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, API Calls, Text]

**Output Format:** [Markdown guidance and structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vehicle status, location links, EV charge details, command previews, and command acceptance or confirmation state.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
