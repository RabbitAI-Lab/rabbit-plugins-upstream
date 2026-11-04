## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd users can look up beer, brewery, venue, and account activity, check what they or friends have tried, and prepare or post check-ins and comments to their own account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials grant access to Untappd, and the separately supplied MCP server implementation is outside this skill review.

Mitigation: Prefer an existing access token, keep credentials private, and verify the MCP server before providing it with credentials.

Risk: Check-ins, toasts, and comments change activity visible on the user's Untappd account.

Mitigation: Review the exact confirmation preview and obtain the user's approval before submitting a write.

Risk: Synchronized history can retain dates, comments, and venue details, including friends' activity, until removed.

Mitigation: Sync only histories the user wants retained and remove local cached records when they are no longer needed.

## Reference(s):

- [Untappd MCP on ClawHub](https://clawhub.ai/chrischall/skills/untappd-mcp)
- [Publisher profile: chrischall](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [API Calls, Structured Data, Guidance]

**Output Format:** [Structured Untappd results and concise natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include account activity; cached check-in data can be incomplete until synchronization finishes.]

## Skill Version(s):

2.5.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
