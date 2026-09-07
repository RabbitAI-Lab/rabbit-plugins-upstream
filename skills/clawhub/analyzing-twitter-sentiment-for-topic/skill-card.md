## Description:

Analyzes public sentiment on Twitter/X for any topic, brand, or event using apidojo's Tweet scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, PR teams, market researchers, political analysts, and social listening teams use this skill to collect public Twitter/X posts for a topic and produce sentiment distribution, engagement-weighted signals, themes, notable tweets, and volume trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Topic queries and collected public tweet data may be sent to Apify and processed through Twitter/X scraping services.

Mitigation: Avoid sensitive monitoring targets unless external processing is acceptable for the workflow.

Risk: The skill requires an APIFY_TOKEN for the Apify workflow.

Mitigation: Store APIFY_TOKEN carefully and avoid exposing it in logs, shared prompts, command history, or generated output.

Risk: Lexical sentiment analysis can miss sarcasm, ambiguity, and context.

Mitigation: For high-stakes use, manually review the most influential positive and negative tweets before acting on the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/analyzing-twitter-sentiment-for-topic)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify Tweet Scraper actor endpoint](https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with sentiment percentages, engagement-weighted notes, themes, examples, trend summaries, and optional shell or API command blocks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May also guide the agent to save collected tweet data as CSV or JSON when using the Apify helper workflow.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
