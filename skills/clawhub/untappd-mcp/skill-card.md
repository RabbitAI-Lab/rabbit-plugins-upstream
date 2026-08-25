## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Untappd beer, brewery, venue, profile, check-in, wishlist, badge, friend, and activity data, and to prepare account write actions such as check-ins, toasts, and comments. It is suited to beer discovery, account history lookup, and public Untappd account interactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an Untappd username and password and unofficial mobile API credentials.

Mitigation: Install only if you are comfortable providing those credentials and review the release before use.

Risk: Write tools can affect a public Untappd account.

Mitigation: Treat check-ins, toasts, and comments as public account actions and rely on the skill's explicit confirmation gate before network submission.

Risk: The skill may cache check-in or beer-history data locally.

Mitigation: Use the cache only for data you have a legitimate reason to query and that is appropriately visible to you.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, API calls, Configuration guidance]

**Output Format:** [Natural-language responses with structured tool result data and confirmation-gated account actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require explicit confirmation; check-in history queries may rely on a local cache whose freshness should be reported to the user.]

## Skill Version(s):

1.8.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
