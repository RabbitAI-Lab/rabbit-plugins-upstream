## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd account users use this skill to look up beers, venues, profiles, check-ins, and friend activity, maintain a local activity cache, and post account changes after reviewing and confirming them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials can be used to access personal Untappd data and perform account actions.

Mitigation: Prefer an existing access token over supplying a password, and keep credentials private.

Risk: Check-ins, toasts, comments, and other supported changes affect the user's account.

Mitigation: Review the exact preview and approve only the intended action; confirm the connected server's safeguards are enabled.

Risk: Synced activity can include friends' check-ins, comments, and venues and remains cached until removed.

Mitigation: Sync only the data needed and remove cached data when it is no longer needed.

Risk: The server implementation is not bundled, and some capability descriptions may conflict.

Mitigation: Use a trusted MCP server and check its actual tools and safeguards before relying on them.

## Reference(s):

- [Untappd MCP on ClawHub](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON results and concise text feed lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results, cache sync status and freshness, plus previews and receipts for supported account changes.]

## Skill Version(s):

2.6.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
