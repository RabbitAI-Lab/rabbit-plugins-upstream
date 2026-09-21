## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and friend activity feeds; and post check-ins, toasts, and comments to an Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Untappd users use this skill to search beer, brewery, venue, and profile information, inspect account activity, maintain a local check-in cache, and perform confirm-gated Untappd account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Untappd username and password values plus mobile client credentials, and the security evidence flags the use of raw account credentials and reverse-engineered client secrets.

Mitigation: Use a dedicated or low-risk Untappd account where possible and store UNTAPPD_USERNAME, UNTAPPD_PASSWORD, UNTAPPD_CLIENT_ID, and UNTAPPD_CLIENT_SECRET securely.

Risk: Confirm-gated write tools can post check-ins, toasts, and comments to a public Untappd account when confirm: true is used.

Mitigation: Review dry-run previews carefully and use confirm: true only when the intended public account action is acceptable.

Risk: The local SQLite cache may contain personal and social drinking-history data.

Mitigation: Store the cache in a protected location, restrict access to the cache file, and clear it when it is no longer needed.

Risk: Security evidence notes an unresolved wishlist capability ambiguity.

Mitigation: Resolve the wishlist behavior against current documentation or tested behavior before relying on wishlist actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)
- [Skill source evidence](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown and structured tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dry-run previews or receipts for confirm-gated account actions and compact or full Untappd response views depending on tool support.]

## Skill Version(s):

2.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
