## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Untappd beer, brewery, venue, user, and friend-feed information from their own account, then optionally log check-ins, toasts, or comments after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Untappd login credentials and mobile app client credentials.

Mitigation: Store required environment variables securely, avoid logging them, and install only when comfortable granting this account access.

Risk: Confirmed write tools can post check-ins, toasts, or comments to a public Untappd account.

Mitigation: Review dry-run previews carefully and pass confirmation only for intended public account actions.

Risk: The local cache can contain account activity and check-in history.

Mitigation: Protect the cache file location and limit access to systems and users that should be able to read account activity.

Risk: The skill uses intercepted mobile app credentials rather than an official delegated authorization flow.

Mitigation: Consider that authentication model before deployment and prefer accounts whose access can be monitored and revoked.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown or plain text responses with structured tool results and dry-run previews for account-writing actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include freshness and completeness caveats for cached Untappd history queries.]

## Skill Version(s):

1.9.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
