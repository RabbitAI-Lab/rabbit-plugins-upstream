## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up Untappd beer, brewery, venue, profile, check-in, wishlist, badge, friend, and activity information. With confirmation, it can also help post check-ins, toasts, and comments to the user's public Untappd account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for the user's Untappd password and mobile client credentials.

Mitigation: Install only in trusted environments, keep secrets out of shell history and logs, and rotate credentials if exposure is suspected.

Risk: Confirmation-gated actions can post or modify public Untappd account content.

Mitigation: Review each preview before approving and avoid automatic confirmation mode unless the deployment is fully trusted.

Risk: Local cache files may contain drinking-history and social-activity data.

Mitigation: Store cache files in a protected location and remove them when the skill is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool-call and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact or full response guidance and confirmation previews for write actions.]

## Skill Version(s):

2.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
