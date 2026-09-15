## Description:

Search Etix events, venues, and performers and pull event/venue details via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Etix events, venues, performers, and showtimes and retrieve event or venue details through an Etix MCP server. It is intended for agents configured with etix-mcp and fetchproxy to answer event-discovery questions using the user's Etix browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run mutable third-party code for etix-mcp and fetchproxy.

Mitigation: Pin etix-mcp to a reviewed version and fetchproxy to a reviewed commit, then build and run them in an isolated environment.

Risk: The browser extension routes requests through the user's Etix browser session.

Mitigation: Use a dedicated browser profile or limited Etix session and avoid exposing unrelated browsing state.

Risk: The unpacked extension and MCP configuration can remain active after the task is complete.

Mitigation: Remove the unpacked extension and MCP configuration when the skill is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp source](https://github.com/chrischall/etix-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with event search results, event or venue detail summaries, and inline JSON or bash setup snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires etix-mcp, the fetchproxy browser extension, and an open etix.com tab for live Etix lookup.]

## Skill Version(s):

0.6.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
