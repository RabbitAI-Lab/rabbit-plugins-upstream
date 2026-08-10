## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Untappd beer, brewery, venue, profile, check-in, wishlist, badge, friend, and activity-feed data, and to manage their own Untappd interactions. It can also help answer has-had and top-not-had questions from synced check-in cache data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires raw Untappd account credentials and mobile app client credentials.

Mitigation: Use only an account you are willing to expose to this tool, keep credentials out of code and logs, and avoid intercepted or third-party client secrets unless you are certain that use is allowed.

Risk: The skill may cache account-linked check-in history.

Mitigation: Review cache location and retention before use, and protect or delete cached data according to the sensitivity of the account history.

Risk: Write actions can post to a public Untappd account.

Mitigation: Use the documented dry-run behavior and require explicit confirmation before posting check-ins, comments, or toasts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text guidance with tool-call recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews for confirm-gated write actions and freshness caveats for cached check-in results.]

## Skill Version(s):

1.8.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
