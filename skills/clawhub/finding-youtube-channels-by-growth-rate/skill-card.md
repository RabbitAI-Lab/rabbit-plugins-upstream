## Description:

Finds fast-growing YouTube channels in a niche using apidojo's YouTube scraper and returns channel names, subscriber counts, growth signals, view momentum, upload frequency, and growth tiers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Brand partnership managers, talent scouts, sponsorship teams, and other external users use this skill to find YouTube creators with rising momentum in a topic area before they become large channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends user-provided niche terms, YouTube URLs, and scraper inputs to Apify under the user's APIFY_TOKEN.

Mitigation: Avoid placing secrets, private data, or confidential research terms in scraper inputs or custom mapping code.

Risk: Growth classifications can be misleading when source data is sparse, stale, or missing key fields.

Mitigation: Broaden or adjust search terms when result counts are low, remove entries with missing key fields, and note data quality limits in the final output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/finding-youtube-channels-by-growth-rate)
- [Apify YouTube Scraper Actor](https://apify.com/apidojo/youtube-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown table and summary with optional JSON or CSV result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include channel metrics, growth classifications, view momentum, upload frequency, scores, and troubleshooting notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
