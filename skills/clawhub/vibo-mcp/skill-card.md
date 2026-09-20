## Description:

Access your Vibo event music planning through MCP for event timelines, song requests, playlists, guest activity, and music exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Vibo event music planning so they can inspect events, manage timeline sections, review song requests, and perform confirm-gated music planning actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vibo passwords, access tokens, refresh tokens, or captured sessions may expose event data if committed or shared.

Mitigation: Do not commit .mcp.json or session files; store credentials only in trusted local configuration and rotate or revoke them if exposed.

Risk: Confirm-gated write tools can change Vibo event data when confirm:true is supplied.

Mitigation: Review the proposed action and target event or section before approving any confirm:true call.

Risk: The skill depends on the third-party vibo-mcp npm package for MCP server behavior.

Mitigation: Install only if you trust the package and need Vibo access from your agent.

## Reference(s):

- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, text]

**Output Format:** [Markdown with configuration examples and tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides use of an MCP server whose read tools return Vibo event data and whose mutating tools require confirm:true before changing event data.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
