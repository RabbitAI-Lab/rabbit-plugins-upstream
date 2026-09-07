## Description:

Scrapes tweets, replies, and media from public Twitter/X accounts using apidojo's Tweet scraper on Apify, returning tweet text, engagement counts, media URLs, and timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, journalists, competitive analysts, and data engineers use this skill to collect public Twitter/X account timelines and export tweet metadata for review or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apify API tokens could be exposed through chat transcripts, shell history, or command-line examples.

Mitigation: Use environment-based authentication or a local .env file where available, and avoid pasting real tokens directly into chat or command lines.

Risk: The documented actor options can perform broader Twitter/X search behavior than account-only timeline collection.

Mitigation: Confirm the intended collection scope before running and configure account-specific inputs, filters, and maxItems explicitly.

Risk: Tweet collection requests and results are sent through Apify.

Mitigation: Use the skill only for public Twitter/X data when third-party processing through Apify is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-tweets-from-account)
- [Apify Tweet Scraper actor](https://apify.com/apidojo/tweet-scraper)

## Skill Output:

**Output Type(s):** [Markdown, JSON, CSV, Shell commands, Guidance]

**Output Format:** [Markdown table with optional JSON or CSV dataset files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Apify API token; use explicit maxItems limits to bound collection size.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
