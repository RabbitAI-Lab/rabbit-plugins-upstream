## Description:

Manage Resy restaurant reservations via MCP: search venues, book tables, list and cancel reservations, manage favorites, and subscribe to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Resy restaurant availability, bookings, cancellations, favorites, and Priority Notify subscriptions through a registered resy-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Resy account credentials and can act with live authority over reservations.

Mitigation: Keep credentials out of shared projects and source control, restrict file permissions, and require explicit confirmation before bookings or cancellations.

Risk: The MCP server depends on mutable third-party code and private Resy web-app endpoints.

Mitigation: Prefer a pinned package version or reviewed commit, and review failures or endpoint changes before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [npm package: resy-mcp](https://www.npmjs.com/package/resy-mcp)
- [Source repository: resy-mcp](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to make live MCP calls that read account data or create, cancel, favorite, and subscribe to restaurant reservations.]

## Skill Version(s):

0.14.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
