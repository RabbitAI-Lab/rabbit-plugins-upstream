## Description:

Scrapes Instagram posts for a hashtag using apidojo's Instagram scraper on Apify and returns post URLs, captions, engagement counts, author handles, timestamps, and related metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, social media researchers, UGC collectors, and developers use this skill to collect Instagram hashtag post metadata through Apify for trend analysis, research, and export workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill collects Instagram profile-linked post data, which can create privacy, compliance, platform-terms, and organizational data-handling obligations.

Mitigation: Collect and export only data that is permitted by applicable laws, platform terms, and organizational rules; limit fields, retention, and sharing to the stated use case.

Risk: Apify tokens can be exposed through token-bearing URLs, logs, shell history, or shared terminals.

Mitigation: Use a dedicated Apify token, keep it in APIFY_TOKEN or a local .env file, avoid pasting token-bearing URLs into logs or shared channels, and rotate the token if exposed.

Risk: Unbounded or large collection runs can increase cost, rate-limit, and data-minimization risks.

Mitigation: Set explicit maxItems limits before each run; the artifact troubleshooting guidance recommends maxItems of 200 or fewer per run and spacing runs five minutes apart.

Risk: Instagram hashtag results may be incomplete for banned or restricted hashtags, very popular feeds, private accounts, or platform-side limitations.

Mitigation: Treat output as a sampled dataset, document collection limits, and validate important conclusions against additional sources before relying on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/apidojo-io/skills/scraping-instagram-posts-by-hashtag)
- [ClawHub publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify actor: apidojo/instagram-hashtag-scraper](https://apify.com/apidojo/instagram-hashtag-scraper)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with shell commands, Apify actor input JSON, REST API examples, tabular dataset summaries, and optional CSV or JSON saved results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires APIFY_TOKEN. Common inputs include hashtag keywords or start URLs, post type filters, date filters, maxItems, and optional custom mapping.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
