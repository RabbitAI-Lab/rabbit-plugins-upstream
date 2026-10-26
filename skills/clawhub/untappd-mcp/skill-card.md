## Description:

Helps users search Untappd beers, breweries, and venues; review profiles and check-ins; and post check-ins, toasts, and comments to their own account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd users can ask an agent about beers, venues, and social activity, or ask it to post activity to their own account after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access tokens or login credentials grant access to the user's Untappd account.

Mitigation: Prefer an existing access token over username and password, and install only if account-level access is acceptable.

Risk: Check-ins, toasts, and comments can become public account activity.

Mitigation: Review each posting preview and avoid configurations that automatically confirm public posts.

Risk: The local cache can retain historical check-ins, venues, and comments, including friends' activity.

Mitigation: Keep the cache private and periodically delete cached users or the database when retention is no longer needed.

## Reference(s):

- [Untappd MCP on ClawHub](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize Untappd search results, account activity, and confirmations for requested posts.]

## Skill Version(s):

2.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
