## Description:

Helps users check Kia vehicle status, location, and charging and request confirmed remote vehicle commands through their Kia account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and their assistants use this skill to check vehicle condition and location, review EV charging, and request confirmed climate, charging, or door commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account access can expose vehicle location and enable remote commands.

Mitigation: Use read-only mode when commands are not needed, and confirm each vehicle command with the user.

Risk: An exported refresh token can retain access without another MFA challenge.

Mitigation: Avoid exporting the token unless deployment requires it; forget the local session when access is no longer needed.

Risk: Cached reads or accepted commands can be mistaken for current vehicle state.

Mitigation: Refresh and re-read status when freshness matters, and verify a command's effect before reporting it as complete.

## Reference(s):

- [kiaaccess on ClawHub](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package (linked in skill)](https://www.npmjs.com/package/kiaaccess-mcp)
- [kiaaccess-mcp project (linked in skill)](https://github.com/chrischall/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses with vehicle status and command confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Status and location may be cached; command acceptance does not establish a changed vehicle state.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
