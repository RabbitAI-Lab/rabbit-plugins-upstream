## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query Untappd beer, brewery, venue, user, activity, wishlist, and cache data, and to prepare account actions such as check-ins, toasts, and comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires raw Untappd account credentials and mobile app client credentials.

Mitigation: Use only in an environment where those credentials can be stored securely, limit access to the runtime configuration, and rotate or revoke credentials if exposure is suspected.

Risk: Confirm-gated tools can post check-ins, toasts, and comments to a public Untappd account.

Mitigation: Review each dry-run preview and call write tools with confirmation only when the target account action is intended.

Risk: The skill caches Untappd history locally and cached results may be incomplete until sync finishes.

Mitigation: Protect the local cache location and check freshness or sync progress before relying on negative cache results.

Risk: The security evidence notes inconsistent write-tool documentation.

Mitigation: Review the actual MCP tool registry and available parameters before enabling account-write workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, configuration notes, and action parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact or full Untappd response guidance, confirm-gated write previews, sync progress, and local cache freshness caveats.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
