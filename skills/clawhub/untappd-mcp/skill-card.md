## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account. Use when the user asks about beer ratings, what a beer or brewery is like on Untappd, someone's Untappd check-ins or wishlist, or wants to log/toast/comment on a beer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd users can use this skill to look up beers, breweries, venues, and account activity, or to prepare and post check-ins, toasts, and comments to their own account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials are used to access Untappd.

Mitigation: Use a trusted MCP server and supply credentials through its environment settings.

Risk: Check-ins, toasts, and comments can publish activity to the user's account.

Mitigation: Keep write confirmations enabled and review the exact preview before approving an action.

Risk: Synced history, including friends' activity, remains stored until removed.

Mitigation: Remove cached history when it is no longer needed.

## Reference(s):

- [Untappd MCP on ClawHub](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [Text responses with Untappd data, write previews, and action receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results may be compact or full; cache answers report data freshness and coverage.]

## Skill Version(s):

2.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
