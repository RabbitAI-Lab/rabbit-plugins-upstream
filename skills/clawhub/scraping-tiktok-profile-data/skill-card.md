## Description:

Scrapes TikTok profile statistics and metadata for account lists using apidojo's TikTok Profile Scraper on Apify, returning fields such as follower count, following count, total likes, video count, bio, and verified status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to collect TikTok profile metadata in bulk for influencer vetting, audience analysis, and data enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok usernames, profile URLs, and query parameters are sent to Apify under the user's Apify account.

Mitigation: Run only with inputs appropriate for Apify processing, and review Apify account, dataset retention, and deletion settings after each run.

Risk: APIFY_TOKEN exposure could allow unauthorized actor runs or dataset access.

Mitigation: Keep APIFY_TOKEN in an environment variable or managed secret store and avoid placing it in shared command history, logs, or skill artifacts.

Risk: Creator lists and exported datasets may contain sensitive business or personal-interest data.

Mitigation: Limit dataset sharing, avoid storing sensitive account lists in shared logs, and delete exported files when they are no longer needed.

Risk: TikTok profile data may be stale or unavailable for private, deleted, banned, or renamed accounts.

Mitigation: Treat profile statistics as time-sensitive, re-run when freshness matters, and verify missing or important accounts directly on TikTok.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-tiktok-profile-data)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with tables, shell commands, and optional JSON or CSV dataset files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs profile-level TikTok fields and flags missing, private, banned, deleted, or renamed accounts when the upstream actor provides that status.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
