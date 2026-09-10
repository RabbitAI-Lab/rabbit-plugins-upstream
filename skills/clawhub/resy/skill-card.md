## Description:

Manage Resy restaurant reservations via MCP by searching venues, booking tables, listing or canceling reservations, managing favorites, and subscribing to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and operate a Resy MCP server for reservation search, booking, cancellation, favorites, and Priority Notify workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses an unpinned npm MCP server, so the installed package can change between runs.

Mitigation: Use a pinned, reviewed `resy-mcp` version wherever possible and re-review before upgrading.

Risk: The skill requires Resy account credentials.

Mitigation: Store credentials outside project files and source control, preferably in a user-scoped secret manager or protected MCP configuration.

Risk: The tools can make live account changes, including bookings, cancellations, favorites, and Priority Notify updates.

Mitigation: Require explicit user confirmation before any account-changing action.

Risk: The underlying server uses Resy's private web-app API, which may change without notice.

Mitigation: Verify behavior with a reviewed version before relying on booking, cancellation, or notification workflows.

## Reference(s):

- [ClawHub resy skill page](https://clawhub.ai/chrischall/skills/resy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides MCP setup and Resy reservation workflows; live account actions should require explicit user confirmation.]

## Skill Version(s):

0.13.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
