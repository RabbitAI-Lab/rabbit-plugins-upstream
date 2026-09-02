## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up Untappd beer, brewery, venue, and account activity data and to perform confirm-gated actions on their own Untappd account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Untappd login credentials and mobile app client credentials.

Mitigation: Install only when comfortable providing those credentials; keep them in protected environment variables and prefer a dedicated or low-risk account.

Risk: Confirmed write actions can post public check-ins, toasts, and comments to the user's Untappd account.

Mitigation: Review each dry-run preview carefully and set confirm to true only for intended public account actions.

Risk: The skill may maintain a local SQLite cache of account history.

Mitigation: Store the cache in a protected location, limit local access, and remove it when the account-history data is no longer needed.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Configuration, Guidance]

**Output Format:** [Markdown or plain text responses with MCP tool calls and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions use dry-run previews and require explicit confirmation before posting.]

## Skill Version(s):

1.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
