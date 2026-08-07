## Description:

Manage Resy restaurant reservations through an MCP server, including venue search, booking, listing and cancellation, favorites, and Priority Notify subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a Resy MCP server for restaurant reservation workflows, including searching venues, booking tables, listing or cancelling reservations, managing favorites, and subscribing to Priority Notify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can book or cancel real Resy reservations without documented confirmation safeguards.

Mitigation: Require the agent to confirm the exact venue, date, time, party size, and reservation before booking or cancelling.

Risk: The skill requires Resy credentials in MCP configuration and uses an unofficial Resy API client.

Mitigation: Install only after reviewing this behavior, restrict access to credential configuration, and use local secrets or protected environment files where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-mcp)
- [npm package](https://www.npmjs.com/package/resy-mcp)
- [Project link listed in artifact](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP tool names and setup snippets for local Resy credential configuration.]

## Skill Version(s):

0.6.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
