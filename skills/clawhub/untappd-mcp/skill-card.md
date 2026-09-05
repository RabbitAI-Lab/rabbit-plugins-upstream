## Description:

Search Untappd beers, breweries, venues, user profiles, check-ins, wishlists, badges, friends, and activity feeds, and help post confirmed check-ins, toasts, and comments to the user's own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up Untappd beer, brewery, venue, and social activity data from their own account. It can also help prepare account actions such as check-ins, toasts, and comments when the user explicitly confirms them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires raw Untappd credentials and intercepted mobile app client credentials.

Mitigation: Install only in trusted MCP environments, store credentials in environment variables or a secrets manager, and prefer an official OAuth-based implementation when available.

Risk: Confirmed write tools can affect the user's public Untappd account.

Mitigation: Review every dry-run preview before setting confirm: true, especially for check-ins, toasts, comments, friend actions, and wishlist changes.

Risk: The local check-in cache can contain personal account and activity history.

Mitigation: Store the cache in a protected location, limit filesystem access to the MCP process, and delete or rotate the cache when it is no longer needed.

Risk: Reverse-engineered Untappd mobile API behavior may drift and produce incomplete or unexpectedly large responses.

Mitigation: Run the health check after setup, watch for truncation or another_run_needed fields, and request view: "full" only when the extra response detail is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration, API Calls]

**Output Format:** [Markdown with tool names, configuration details, and structured tool result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools return compact summaries by default; full Untappd responses are available for supported tools with view: "full".]

## Skill Version(s):

1.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
