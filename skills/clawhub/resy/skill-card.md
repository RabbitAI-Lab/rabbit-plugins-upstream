## Description:

Manage Resy restaurant reservations via MCP by searching venues, booking tables, listing and canceling reservations, managing favorites, and subscribing to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Resy restaurant reservations through a registered MCP server, including availability search, booking, cancellation, favorites, payment-method lookup, and Priority Notify subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run a third-party MCP package that may be installed without a pinned version.

Mitigation: Install only a trusted, pinned version of resy-mcp and review the package before registering it with an agent.

Risk: The skill uses reusable Resy account credentials.

Mitigation: Store credentials only in a private environment or local MCP configuration, keep them out of shared project files and version control, and rotate them if exposed.

Risk: The skill can perform account-changing actions such as booking and canceling reservations.

Mitigation: Require explicit user confirmation before any booking, cancellation, favorite change, or Priority Notify subscription change.

Risk: The MCP server uses Resy's private web-app API rather than an official public API.

Mitigation: Treat API behavior as subject to change, review failures before retrying account-changing actions, and keep the MCP server updated to a vetted release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp source repository](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API Calls, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples; MCP tool calls return structured reservation, venue, profile, payment, favorite, and notification data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Resy email and password credentials and a registered resy-mcp server; write actions can book or cancel reservations.]

## Skill Version(s):

0.14.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
