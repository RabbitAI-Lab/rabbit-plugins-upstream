## Description:

This skill should be used when the user asks about their Kia vehicle through the Kia Access / Kia Owners account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and their agents use this skill to check enrolled vehicle status, location, EV charging information, and to perform confirm-gated vehicle actions such as climate, charging, and door commands through a Kia Access / Kia Owners account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server requires Kia account credentials and can maintain a persistent vehicle session.

Mitigation: Store credentials outside committed project files, treat exported refresh tokens like passwords, and install only when this account access is acceptable.

Risk: Vehicle command tools can affect a real vehicle, including climate, charging, and door unlock behavior.

Mitigation: Use the most restrictive KIA_WRITE_MODE that meets the task, require explicit confirmation before commands, and enable door unlock only when needed.

Risk: The setup uses an unpinned npm MCP server through npx.

Mitigation: Review the package version and source before deployment, and pin or control the package version in managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [npm package: kiaaccess-mcp](https://www.npmjs.com/package/kiaaccess-mcp)
- [GitHub repository listed in skill artifact](https://github.com/chrischall/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, API calls]

**Output Format:** [Markdown with inline JSON and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can guide agent use of an MCP server that reads Kia vehicle data and sends confirm-gated vehicle commands.]

## Skill Version(s):

0.9.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
