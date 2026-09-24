## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Untappd beer, brewery, venue, profile, activity, wishlist, and badge data, and to log or interact with check-ins on their own Untappd account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Untappd account credentials and mobile client credentials.

Mitigation: Use a protected secret store for credentials and avoid committing them to source control or exposing them in logs.

Risk: The security guidance reports inconsistent documentation around account-changing tools.

Mitigation: Verify the actual MCP tool list and confirm-gated behavior before using write actions.

Risk: Sync and cache tools can store Untappd history locally in SQLite.

Mitigation: Review the local cache location and retention expectations before syncing personal or friend-visible activity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, environment variables, and structured MCP result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes compact/full view guidance, confirm-gated write guidance, and cache sync caveats.]

## Skill Version(s):

2.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
