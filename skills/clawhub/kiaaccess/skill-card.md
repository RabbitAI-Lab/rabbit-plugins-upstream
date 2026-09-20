## Description:

Helps an agent set up and use the kiaaccess MCP server to read Kia vehicle status, location, EV charge information, and confirm-gated vehicle commands through a user's Kia Access account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and vehicle owners use this skill to configure an agent for Kia Access MCP workflows, including account bootstrap, status reads, vehicle location, EV charging information, and explicitly confirmed comfort or door commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable sensitive vehicle actions such as climate, charging, lock, or unlock commands.

Mitigation: Use KIA_WRITE_MODE=none or comfort unless door commands are required, and require explicit confirmation before every vehicle command.

Risk: Kia account passwords and refresh tokens can grant access to the user's vehicle account.

Mitigation: Protect KIA_PASSWORD and KIA_RMTOKEN like account credentials, never echo them in conversation, and only export refresh tokens for deployment migration.

Risk: The MCP server is installed from an external npm package.

Mitigation: Verify that the referenced npm package and source repository are trusted before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, API Calls]

**Output Format:** [Markdown with JSON configuration examples and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confirm-gated vehicle command guidance and secret-handling cautions.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
