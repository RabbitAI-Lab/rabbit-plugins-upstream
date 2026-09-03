## Description:

Monitors tech acquisition news and M&A activity using apidojo's Google Search scraper, returning acquisition announcements, involved companies, deal size signals, and strategic rationale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, founders, investors, and competitive intelligence teams use this skill to monitor Google results for technology acquisition and M&A activity. It helps classify acquisition news, identify acquirers and targets, and summarize deal significance signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and actor inputs are sent to Apify when the Google Search scraper is run.

Mitigation: Avoid using confidential deal names, secrets, or sensitive internal strategy in searchTerms or customMapFunction unless sharing that data through the configured Apify account is acceptable.

Risk: Breaking M&A news may include rumors, speculation, or incomplete reporting.

Mitigation: Classify results as CONFIRMED, REPORTED, RUMORED, or DENIED and keep unverified reports marked as unconfirmed until an official source is found.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/monitoring-tech-acquisition-news-google)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, summaries, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save Google Search scraper results as CSV or JSON when requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
