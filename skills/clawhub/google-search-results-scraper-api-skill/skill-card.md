## Description:

This skill runs the BrowserAct Google Search Results Scraper template to collect structured public search-result data for analysis, enrichment, monitoring, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation users use this skill to run a BrowserAct search-results scraping workflow and return structured public Google result data for market research, dataset enrichment, monitoring, and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: BrowserAct API keys could be exposed if pasted into an agent conversation.

Mitigation: Set BROWSERACT_API_KEY through a secure local environment or secret manager, and rotate the key if it was previously shared in chat.

Risk: Search inputs are sent to BrowserAct.

Mitigation: Use the skill only for non-sensitive search queries that are acceptable to send to BrowserAct.

Risk: External API execution may fail because of invalid authorization, concurrency limits, transient failures, or polling timeout.

Mitigation: Review output before relying on results, follow the documented stopping rules, and handle missing or partial fields gracefully.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/google-search-results-scraper-api-skill)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=google-search-results-scraper)
- [BrowserAct bots API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API response output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; task polling may take several minutes and can time out after 900 seconds.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
