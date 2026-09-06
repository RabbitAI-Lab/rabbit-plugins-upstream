## Description:

This skill runs BrowserAct's Amazon Product Details Scraper template to retrieve structured public Amazon product data for a marketplace URL and ASIN.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a BrowserAct workflow that collects public Amazon product fields such as title, price, ratings, reviews, description, feature bullets, and availability for research, monitoring, reporting, or dataset enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: BrowserAct API keys may be exposed if pasted into an agent conversation.

Mitigation: Configure BROWSERACT_API_KEY through the local environment or a secret manager, do not paste it into chat, and rotate the key if it was previously shared.

Risk: The skill initiates BrowserAct automation against Amazon for the supplied marketplace URL and ASIN.

Mitigation: Use the skill only when the user intentionally requests Amazon product-detail scraping for a specific marketplace and ASIN, and review the returned fields before downstream use.

Risk: The skill has broad routing language for public data collection use cases.

Mitigation: Keep use constrained to the documented Amazon product-details workflow and avoid expanding it to unrelated scraping tasks without review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/amazon-product-details-scraper-api-skill)
- [BrowserAct integration console](https://www.browseract.com/reception/integrations?co-from=amazon-product-details-scraper)
- [BrowserAct API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with a shell command invocation and JSON or text API response output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BROWSERACT_API_KEY, accepts marketplace_url and asin inputs, emits timestamped task status logs, and polls for up to 900 seconds.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
