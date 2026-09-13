## Description:

This skill helps users run the Facebook Ads Library Scraper BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to collect public Facebook Ads Library records for market research, competitive monitoring, dataset enrichment, reporting, and repeatable BrowserAct API automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be used for large-scale scraping, recurring monitoring, contact-like data collection, or CRM enrichment.

Mitigation: Review planned use before installation or execution, collect only fields needed for a lawful and policy-compliant purpose, and avoid storing or reusing unnecessary contact-like data.

Risk: The skill depends on a BrowserAct API key.

Mitigation: Set BROWSERACT_API_KEY through an approved environment or secret store and do not paste API keys into chat.

Risk: Security evidence flags loose scraping scope and secret-handling guidance.

Mitigation: Constrain keyword, region, date range, and maximum ad count for each run, and review outputs before using them in downstream reports, CRMs, or monitoring workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/facebook-ads-library-scraper-api-skill)
- [BrowserAct API key setup](https://www.browseract.com/reception/integrations?co-from=facebook-ads-library-scraper)
- [BrowserAct bots API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; task runs may take several minutes and return public ad fields when available.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
