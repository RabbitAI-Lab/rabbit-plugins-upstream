## Description:

Analyzes competitor YouTube channel strategy and content performance using apidojo's YouTube scraper.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External YouTube content strategists, brand video teams, and competitive intelligence analysts use this skill to benchmark competitor channels, evaluate content mix, publishing cadence, and engagement, and produce strategic insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube channel identifiers, search terms, and scraper inputs are sent to Apify.

Mitigation: Use only inputs approved for third-party processing, and avoid submitting confidential strategy data as search terms.

Risk: APIFY_TOKEN or token-bearing URLs can be exposed through logs, shell history, or chat transcripts.

Mitigation: Keep APIFY_TOKEN in an environment variable or secrets manager, avoid pasting token-bearing URLs into logs or chats, and prefer MCP or a helper that does not expose tokens in URLs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/analyzing-youtube-competitor-channel-strategy)
- [Apify YouTube Scraper Actor](https://apify.com/apidojo/youtube-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summary with tables, inline shell commands, optional JSON or CSV files, and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the Apify YouTube scraper with channel URLs, handles, keywords, trending flags, geography, language, duration, upload date, feature, sort, and max item parameters.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
