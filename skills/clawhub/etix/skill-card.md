## Description:

Search Etix events, venues, and performers and pull event and venue details through an MCP server that uses an active etix.com browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to discover Etix events, venues, performers, showtimes, pricing, and venue details from natural-language requests. It is intended for event discovery workflows that can tolerate dependence on an unofficial Etix integration and a local browser bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review says the skill asks users to run unpinned third-party code and load a browser extension that uses their live Etix browser session.

Mitigation: Use a pinned and reviewed etix-mcp version, pin the fetchproxy commit, inspect extension permissions, and run it in a dedicated browser profile.

Risk: The Etix integration depends on an unofficial browser-session bridge and website endpoints that may change or be blocked.

Mitigation: Keep Etix logged out unless authenticated access is required, use the healthcheck before relying on results, and disable or remove the MCP configuration and extension when not in use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp source](https://github.com/chrischall/etix-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)
- [Etix website](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires etix-mcp, a local fetchproxy browser extension, and an open etix.com tab for live lookups.]

## Skill Version(s):

0.6.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
