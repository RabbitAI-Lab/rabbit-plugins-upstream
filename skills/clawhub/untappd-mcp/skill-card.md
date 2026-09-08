## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Untappd beer, brewery, venue, and user data and to manage their own Untappd interactions such as check-ins, toasts, and comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to an Untappd password, extracted mobile app credentials, private account data, and public posting actions.

Mitigation: Install only when those permissions are acceptable, store credentials securely, and confirm account-changing actions before execution.

Risk: The local cache can contain sensitive location and activity history.

Mitigation: Treat the cache as sensitive data and avoid shared or synced storage for the cache database.

Risk: The integration uses unofficial private Untappd mobile API behavior that may change.

Mitigation: Run the health check before relying on the skill and prefer compact views or documented freshness fields when assessing returned data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown or structured tool responses describing Untappd data, actions, cache status, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools support compact or full response views; write actions are confirm-gated and cache-backed queries can report freshness and incomplete coverage.]

## Skill Version(s):

1.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
