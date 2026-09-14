## Description:

This skill helps users run the eBay Product Listings Scraper BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a BrowserAct template that collects structured public eBay search listing data for market research, dataset enrichment, reporting, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party BrowserAct API to run scraping workflows.

Mitigation: Use it only for intentional public eBay listing collection and avoid submitting sensitive search terms or business targets unless sharing them with BrowserAct is acceptable.

Risk: Unsafe onboarding language may lead users to paste an API key into chat.

Mitigation: Store BROWSERACT_API_KEY locally in a protected environment variable or secret manager and do not paste API keys into chat.

Risk: The security verdict is suspicious.

Mitigation: Review the skill before installing or executing it, with particular attention to credential handling and third-party API use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/ebay-product-listings-scraper-api-skill)
- [BrowserAct Console](https://www.browseract.com/reception/integrations?co-from=ebay-product-listings-scraper)
- [BrowserAct Bots API Endpoint](https://api.browseract.com/v3/bots)
- [eBay Marketplace](https://www.ebay.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API response text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; successful runs return BrowserAct API response data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
