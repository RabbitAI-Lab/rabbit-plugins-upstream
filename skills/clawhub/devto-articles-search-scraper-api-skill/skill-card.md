## Description:

This skill helps users run the DEV Community Articles Search Scraper BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run a BrowserAct template that collects public DEV Community article search results for market research, dataset enrichment, reporting, monitoring, and repeatable API automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags guidance that could lead a user to share a BrowserAct API key with an agent.

Mitigation: Configure BROWSERACT_API_KEY privately through the environment or a secret manager, and do not paste the key into chat.

Risk: The documented output may include contact fields beyond the stated DEV article-search purpose.

Mitigation: Review returned data before storing, sharing, or enriching downstream systems, especially if email, phone, address, or other unexpected contact fields appear.

Risk: The skill depends on a third-party BrowserAct workflow and public web scraping behavior.

Mitigation: Install only when BrowserAct use for public DEV search scraping is acceptable for the deployment context, and validate results before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/devto-articles-search-scraper-api-skill)
- [Publisher profile](https://clawhub.ai/user/browseract-cli)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=devto-articles-search-scraper)
- [DEV Community](https://dev.to)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and a BROWSERACT_API_KEY environment variable; the BrowserAct run may take several minutes and returns public article metadata when successful.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
