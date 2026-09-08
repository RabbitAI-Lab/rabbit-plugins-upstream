## Description:

Tracks product launch buzz and reactions on Twitter/X using apidojo's Twitter Search scraper and summarizes volume, sentiment, top voices, geographic spread, and a buzz score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Product marketing teams, PR professionals, and competitive analysts use this skill to monitor Twitter/X reaction to product launches and competitor announcements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter/X search terms, product names, competitor names, filters, and usage patterns are sent to Apify.

Mitigation: Avoid confidential launch plans, regulated data, sensitive internal codenames, and other private information in search queries.

Risk: Broad or unlimited searches may consume Apify service quota.

Mitigation: Set explicit result limits and monitor Apify account usage during launch monitoring.

Risk: Older launches or overly narrow filters can produce low-volume or misleading launch-buzz signals.

Mitigation: Run monitoring within 24-72 hours of launch when possible, broaden search terms when result counts are low, and note filtered or missing data in the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/tracking-product-launch-buzz-on-twitter)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with summary text, tables, and optional CSV or JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes tweet volume, sentiment distribution, top voices, geographic spread, buzz classification, and a buzz score.]

## Skill Version(s):

1.0.0 (source: release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
