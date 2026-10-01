## Description:

Helps agents query Google Ads campaigns, ad groups, keywords, and performance metrics through a managed Google Ads connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Advertisers, analysts, and developers use this skill to inspect Google Ads accounts and performance through GAQL, and to manage campaigns with explicit approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granting a connection gives Maton access to the authorized Google Ads account.

Mitigation: Confirm the account and requested access before authorizing a connection; use read and list operations first.

Risk: Changes to budgets, bids, ads, or campaign state can affect spending or live advertising.

Mitigation: Confirm the specific target, payload, and intended effect before any write.

Risk: Persistent functions, triggers, or API keys can automate actions or expose account data beyond a single request.

Mitigation: Create them only when needed and after reviewing the exact data flow and credential handling.

## Reference(s):

- [Google Ads skill release](https://clawhub.ai/byungkyu/skills/google-ads-api)
- [Google Ads API overview](https://developers.google.com/google-ads/api/docs/start)
- [Google Ads Query Language overview](https://developers.google.com/google-ads/api/docs/query/overview)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with commands and summarized Google Ads results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GAQL queries and account performance metrics.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
