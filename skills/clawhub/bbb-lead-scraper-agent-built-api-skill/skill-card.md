## Description:

This skill helps users run the BBB Lead Scraper Bot BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a BrowserAct BBB lead scraping workflow for market research, dataset enrichment, public web data monitoring, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: BrowserAct API key exposure through chat or logs.

Mitigation: Configure BROWSERACT_API_KEY through a local environment variable or approved secret manager before running the script.

Risk: Broad BBB/business contact scraping may collect data that needs careful handling.

Mitigation: Use the skill only for lawful, terms-compliant collection and apply appropriate retention, access, and downstream-use controls to returned contact data.

Risk: Running the skill contacts BrowserAct and can consume account quota or hit concurrency limits.

Mitigation: Confirm intended query parameters and account limits before execution, and stop rather than retrying when authorization or concurrency errors occur.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/bbb-lead-scraper-agent-built-api-skill)
- [BrowserAct API Key Console](https://www.browseract.com/reception/integrations?co-from=bbb-lead-scraper)
- [BrowserAct Bots API](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python and BROWSERACT_API_KEY; successful runs may return business names, websites, email addresses, phone numbers, addresses, ratings, and related public listing fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
