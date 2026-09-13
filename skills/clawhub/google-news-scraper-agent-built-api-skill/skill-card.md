## Description:

This skill helps agents run a BrowserAct Google News scraper template and return structured public news search data for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to collect structured Google News search results through a BrowserAct API workflow for market research, dataset enrichment, monitoring, and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API key exposure could occur if users paste BrowserAct credentials into chat or logs.

Mitigation: Configure BROWSERACT_API_KEY through a local environment variable or approved secret manager, and avoid sharing the key with the agent.

Risk: Google News search parameters and returned data are sent to BrowserAct during execution.

Mitigation: Install and invoke the skill only where BrowserAct processing is acceptable for the intended data collection workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/google-news-scraper-agent-built-api-skill)
- [BrowserAct API Key Console](https://www.browseract.com/reception/integrations?co-from=google-news-scraper)
- [BrowserAct Bots API Endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Terminal status logs and JSON API response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python and BROWSERACT_API_KEY; polls BrowserAct run status until completion, failure, cancellation, or timeout.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
