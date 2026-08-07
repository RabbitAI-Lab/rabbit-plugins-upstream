## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Untappd beer, brewery, venue, and account activity data, maintain a local check-in cache, and prepare confirm-gated write actions such as check-ins, toasts, and comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Untappd login credentials and unofficial mobile API credentials.

Mitigation: Install only in a trusted runtime, store credentials as secrets, and avoid sharing logs or environment dumps that could expose them.

Risk: The skill can cache account and social-activity data locally or in a per-user remote store.

Mitigation: Treat the cache as sensitive data, restrict profile lookups to public or explicitly intended users, and remove cached data when it is no longer needed.

Risk: Confirm-gated actions can post check-ins, toasts, or comments to a public Untappd account.

Mitigation: Review each dry-run preview carefully and only set confirm:true when the account action is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, environment variables, and action parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dry-run previews for confirm-gated posting actions before any public Untappd account change is made.]

## Skill Version(s):

1.8.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
