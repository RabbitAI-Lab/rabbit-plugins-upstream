## Description:

Tracks trending YouTube topics and video formats in a specific niche using apidojo's YouTube scraper on Apify, returning trending video titles, view counts, engagement metrics, format patterns, and topic themes for creators, marketers, and video strategists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video marketers, and brand strategists use this skill to research high-performing YouTube videos in a niche and turn title formulas, topic themes, and engagement signals into content ideas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an Apify token to run YouTube scraping workflows.

Mitigation: Install and run it only in environments where use of an Apify token for YouTube research is approved.

Risk: Generated search inputs can affect what YouTube data is collected and analyzed.

Mitigation: Review the proposed keywords, URLs, country, language, and filtering inputs before executing the Apify actor.

Risk: Saved CSV or JSON outputs may contain YouTube research results from the user's query.

Mitigation: Store exported result files according to the user's data handling requirements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/apidojo-io/skills/tracking-youtube-trending-topics-by-niche)
- [Apify YouTube Scraper run endpoint](https://api.apify.com/v2/acts/apidojo~youtube-scraper/runs)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown trend brief with tables, recommendations, and optional inline bash, JSON, or CSV workflow outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference YouTube trend data, engagement metrics, Apify actor inputs, and saved CSV or JSON result files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
