## Description:

Find Toast restaurants, inspect their menus and availability, and, when signed in, read order history, receipts, loyalty details, and Toast Cash.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Diners use this skill to find Toast restaurants, review online or register menus, check item availability, and retrieve their own Toast account details when signed in. It requires the Toast MCP service and the ContextMint Bridge browser extension with a relevant Toast page open.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When the user is signed in, the skill can read personal order history, receipts, loyalty details, and Toast Cash.

Mitigation: Review server and extension permissions before installing. Keep personal account tools disabled for menu lookup and enable them only when you want the agent to read account information.

Risk: Menu results can be truncated, and item availability changes over time.

Mitigation: Treat out-of-stock status as current-day information, report when results are truncated, and confirm details with the restaurant before relying on them.

## Reference(s):

- [toasttab-mcp on ClawHub](https://clawhub.ai/chrischall/skills/toasttab-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language summaries and lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Menu and account details depend on the information available through the user's Toast pages; account details require a signed-in session.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
