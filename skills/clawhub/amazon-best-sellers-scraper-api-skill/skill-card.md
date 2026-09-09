## Description:

This skill runs BrowserAct's Amazon Best Sellers Scraper Bot API template to extract structured public Amazon Best Sellers data for research, monitoring, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a BrowserAct workflow that collects ranked Amazon Best Sellers product records, including product names, URLs, ratings, review counts, prices, images, and categories. It supports market research, competitive monitoring, dataset enrichment, pricing checks, and operational reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: BrowserAct API keys may be exposed if users paste credentials into the agent conversation.

Mitigation: Configure BROWSERACT_API_KEY through the runtime environment or a secret manager, avoid sharing it in chat, and rotate any key that was previously exposed.

Risk: Selected Amazon category, requested count, task metadata, and returned results are sent to BrowserAct.

Mitigation: Use the skill only for data and workflows that are acceptable to process through BrowserAct.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/amazon-best-sellers-scraper-api-skill)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=amazon-best-sellers-scraper)
- [BrowserAct bot API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON, guidance]

**Output Format:** [Terminal status logs followed by JSON returned from the BrowserAct API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; accepted inputs are marketplace_category and count.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
