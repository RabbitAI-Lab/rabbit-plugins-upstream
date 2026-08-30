## Description:

Manage Resy restaurant reservations through an MCP server, including venue search, booking, cancellation, favorites, and Priority Notify subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a Resy MCP server for restaurant discovery, reservation booking, cancellation, saved favorites, and Priority Notify management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can book or cancel real Resy reservations using account credentials.

Mitigation: Confirm venue, date, party size, time, payment requirement, and cancellation target before any booking or cancellation.

Risk: The skill requires Resy email and password credentials for a third-party MCP server.

Mitigation: Install only after review, store credentials in the MCP environment rather than prompts or shared files, and remove access when no longer needed.

Risk: The skill uses Resy's private web endpoints, which may change or fail without notice.

Mitigation: Check responses carefully before relying on availability, booking, cancellation, favorites, or Priority Notify results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp source](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, text]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct an agent to call MCP tools that search venues, book or cancel reservations, and manage account-linked Resy settings.]

## Skill Version(s):

0.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
