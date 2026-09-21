## Description:

Access your Vibo (vibodj.com) event music planning via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and event hosts use this skill to manage Vibo event music planning through an MCP server, including timelines, song requests, playlists, guest participation, and exports to connected music services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can access Vibo account, event, and connected music-service data.

Mitigation: Install only when that account-level access is acceptable, and review requested operations before enabling confirm-gated writes.

Risk: VIBO_PASSWORD, VIBO_ACCESS_TOKEN, VIBO_REFRESH_TOKEN, and ~/.vibo-mcp/session.json may expose sensitive credentials or sessions if leaked.

Mitigation: Treat these values like passwords, restrict local file access, and rotate or revoke credentials if configuration or session files are exposed.

## Reference(s):

- [Vibo](https://vibodj.com)
- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [vibo-mcp source repository](https://github.com/chrischall/vibo-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, API Calls, Markdown]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool call results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some read tools support compact or full views; mutating tools require explicit confirm gating before network changes.]

## Skill Version(s):

2.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
