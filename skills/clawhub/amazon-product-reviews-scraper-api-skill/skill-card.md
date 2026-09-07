## Description:

This skill helps agents run BrowserAct's Amazon Product Reviews Scraper Bot template to extract structured public Amazon review data for research, monitoring, reporting, or downstream automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation users use this skill to collect structured public Amazon review fields by marketplace URL, ASIN, and review count. The returned review data can support market research, competitive monitoring, dataset enrichment, reporting, and API-driven workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a BrowserAct API key, and the security evidence notes that missing-key guidance may lead users to provide the key through agent chat.

Mitigation: Configure BROWSERACT_API_KEY locally or through a secrets manager; do not paste the key into chat, and rotate it if it has already been shared.

Risk: Requested Amazon product parameters and resulting review data are sent to BrowserAct.

Mitigation: Use the skill only when sharing those parameters and results with BrowserAct is acceptable for the workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/amazon-product-reviews-scraper-api-skill)
- [BrowserAct API Key Console](https://www.browseract.com/reception/integrations?co-from=amazon-product-reviews-scraper)
- [BrowserAct API Base URL](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with an inline shell command and JSON task output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BROWSERACT_API_KEY. Runtime inputs are marketplace URL, ASIN, and review count; execution prints timestamped status logs and returns BrowserAct task results when available.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
