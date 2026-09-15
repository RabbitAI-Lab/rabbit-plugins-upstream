## Description:

Manage OpenTable reservations through an MCP server by searching restaurants, checking slot availability, booking or modifying tables, listing and canceling reservations, and managing favorites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage restaurant reservations on OpenTable from a signed-in browser session, including search, availability checks, booking, modification, cancellation, profile lookup, and favorites management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a signed-in browser session and can expose reservation, profile, and payment-hold details.

Mitigation: Use only a browser profile the user is comfortable connecting to this MCP server, and avoid full response mode unless needed.

Risk: The skill can book, modify, or cancel restaurant reservations.

Mitigation: Confirm every booking, modification, cancellation, and credit-card-required preview in plain language before committing the action.

Risk: The skill relies on external components that may be installed through unpinned package or extension sources.

Mitigation: Prefer pinned package versions or reviewed source commits for the MCP server and fetchproxy extension.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable website](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [Guidance, MCP tool calls, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return compact or full OpenTable payload views depending on the requested tool view.]

## Skill Version(s):

0.19.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
