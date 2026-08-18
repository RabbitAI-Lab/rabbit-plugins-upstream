## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Untappd content, inspect beer and user activity, maintain a local check-in cache, and log public Untappd actions from their own account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires raw Untappd account credentials and mobile app client credentials.

Mitigation: Run only in a trusted local environment, avoid shared machines, and review how secrets are stored before use.

Risk: The skill relies on reverse-engineered mobile API access.

Mitigation: Expect compatibility or account-access changes if Untappd changes its mobile API behavior, and review this dependency before deployment.

Risk: Toasts, comments, and check-ins affect the user's public Untappd account.

Mitigation: Verify every write preview and use confirm:true only when the public action is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, API calls, Guidance]

**Output Format:** [Markdown or structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read operations may return paginated or cached results; write operations require confirm:true before posting to the user's public Untappd account.]

## Skill Version(s):

1.8.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
