## Description:

Finds Twitter Spaces hosts in a specific topic area using apidojo's Twitter scrapers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, PR professionals, thought leaders, and community builders use this skill to discover Twitter Spaces hosts in a topic area and build outreach or collaboration lists. It helps identify host handles, topic focus, frequency signals, co-host networks, audience indicators, classifications, and relevance scores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter search queries are sent to Apify when the scraper workflow runs.

Mitigation: Avoid sensitive search terms and review query contents before execution.

Risk: The Apify API token could be exposed if placed in URLs, logs, or shared command output.

Mitigation: Use the recommended runner or an authenticated client that keeps the token out of URLs, and rotate the token if it appears in logs or shared output.

Risk: Unbounded or broad searches can produce excessive or low-quality scraped results.

Mitigation: Set reasonable maxItems limits and apply the skill's filtering and quality scoring before using results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-twitter-spaces-hosts-by-topic)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify Actor: apidojo/tweet-scraper](https://apify.com/apidojo/tweet-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown table and summary, with optional JSON or CSV result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are derived from Apify Twitter scraper searches and may include host handle, topic focus, frequency signals, co-host network, audience indicators, classification, and relevance score.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
