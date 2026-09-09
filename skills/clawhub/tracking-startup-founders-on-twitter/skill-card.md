## Description:

Tracks startup founders and their activity on Twitter using apidojo's Twitter scrapers, returning founder handles, companies, stages, follower counts, recent topics, and build-in-public signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as venture capital teams, accelerators, partnership teams, and startup ecosystem researchers use this skill to discover, classify, score, and monitor startup founders on Twitter/X by sector, funding stage, and activity signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apify credentials may be exposed if token-bearing URLs are pasted into logs, shared terminals, or saved command history.

Mitigation: Store APIFY_TOKEN in an environment variable or secret manager and prefer MCP or helper tooling that avoids placing tokens directly in URLs.

Risk: Unbounded or overly broad actor runs can increase cost and return unnecessary personal data.

Mitigation: Set maxItems deliberately and scope searches to the minimum sector, stage, or watchlist needed for the task.

Risk: Founder classifications can include solopreneurs, side-project builders, or noisy matches that are not venture-backed founders.

Mitigation: Verify funding mentions, accelerator affiliations, company identity, and recent product-building signals before using results for outreach or decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/tracking-startup-founders-on-twitter)
- [Apify actor: apidojo/twitter-user-scraper](https://apify.com/apidojo/twitter-user-scraper)
- [Apify actor: apidojo/tweet-scraper](https://apify.com/apidojo/tweet-scraper)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summary and table, with optional JSON or CSV actor results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include founder classification, relevance score, recent topics, and data quality notes.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
