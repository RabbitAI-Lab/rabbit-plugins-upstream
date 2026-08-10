## Description:

Read and manage your Skylight Calendar family hub, including calendar events, chores and reward stars, and shared grocery or to-do lists, using your own signed-in Skylight account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can configure an agent to read and manage a Skylight family hub, including family calendar events, chores, rewards, and shared lists. The skill is intended for use with the user's own Skylight account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives a third-party MCP server password-based access to a Skylight account.

Mitigation: Install only if the npm package is trusted, prefer project-scoped MCP configuration, and protect the MCP configuration file as a secret.

Risk: The documented capability surface includes write actions such as event deletion, chore completion, media upload, messaging, or settings changes.

Mitigation: Review the package capabilities before enabling write actions and limit use to the intended Skylight account.

Risk: The documented capability surface is broader than the manifest clearly discloses.

Mitigation: Review the release documentation and security summary before deployment.

## Reference(s):

- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with JSON configuration examples and MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide account-scoped reads and writes through a third-party MCP server.]

## Skill Version(s):

0.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
