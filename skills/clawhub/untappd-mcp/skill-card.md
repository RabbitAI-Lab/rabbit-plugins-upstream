## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and friend activity feeds; and post check-ins, toasts, and comments to the configured Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect an Untappd account to beer, brewery, venue, social activity, and check-in workflows. It is useful for answering Untappd-based beer questions, inspecting a user's activity or wishlist, maintaining a local check-in cache, and performing confirm-gated account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an Untappd username, password, and reverse-engineered mobile client credentials.

Mitigation: Use secure secret storage for credentials and install only when this credential exposure is acceptable.

Risk: The skill can read and cache account and social activity data.

Mitigation: Review the data access scope before installation and protect the local cache path used for check-in history.

Risk: The skill can perform public account actions such as check-ins, toasts, and comments.

Mitigation: Rely on the documented confirm-gated flow and confirm public actions only when the preview matches the intended action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, environment variables, account-action previews or receipts, and structured API-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default compact views are available for selected tools; full upstream responses, progress reports, and cache freshness details are available where the skill documents them.]

## Skill Version(s):

1.11.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
