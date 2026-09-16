## Description:

Search Etix events, venues, and performers and retrieve event or venue details through an MCP server that requires etix-mcp and fetchproxy with an active etix.com browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find Etix events, venues, performers, showtimes, and detailed event or venue information from an agent workflow. It is suited for public event discovery when the user has installed the required MCP server and browser proxy extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP workflow routes requests through the user's browser session via a local extension, giving third-party code sensitive local and browser authority.

Mitigation: Use a dedicated browser profile with no unrelated sessions, inspect extension permissions, and remove the MCP configuration and extension when no longer needed.

Risk: The documented setup installs etix-mcp and fetchproxy without pinning reviewed versions or commits.

Mitigation: Pin etix-mcp and fetchproxy to reviewed package versions or commits before installation.

Risk: The skill depends on Etix website endpoints and pages rather than a public consumer API, so behavior may change and use may require terms review.

Mitigation: Confirm use is consistent with Etix terms, run etix_healthcheck when calls fail, and review returned event details before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp source repository listed by artifact](https://github.com/chrischall/etix-mcp)
- [fetchproxy source repository listed by artifact](https://github.com/chrischall/fetchproxy)
- [Etix ticket site](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with setup snippets and event or venue detail summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires etix-mcp, fetchproxy, and an active etix.com browser tab for live event lookup.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
