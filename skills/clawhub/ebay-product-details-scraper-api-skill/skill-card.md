## Description:

This skill helps users run the eBay Product Details Scraper BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to run BrowserAct's eBay product-detail scraper for market research, dataset enrichment, public web data monitoring, and repeatable API automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses BrowserAct for eBay scraping and sends product URLs and task parameters to a third-party service.

Mitigation: Use the skill only for explicit eBay product URL scraping tasks where sharing those URLs and parameters with BrowserAct is acceptable.

Risk: The skill requires a BrowserAct API key and the security summary notes that users may be asked to provide it in chat.

Mitigation: Set BROWSERACT_API_KEY locally through an environment variable or secret manager and do not paste the key into chat.

Risk: Broad trigger language could cause the skill to run for requests that are not intended to use a third-party scraping service.

Mitigation: Confirm the user intends to run the BrowserAct eBay product scraper before invoking the helper script.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/ebay-product-details-scraper-api-skill)
- [Publisher profile](https://clawhub.ai/user/browseract-cli)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=ebay-product-details-scraper)
- [BrowserAct bots API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API response output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; the helper script polls BrowserAct task status and prints the final API response.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
