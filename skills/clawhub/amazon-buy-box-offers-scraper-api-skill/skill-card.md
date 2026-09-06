## Description:

This skill helps users run the Amazon Buy Box Offers Scraper BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and automation developers use this skill to retrieve structured Amazon Buy Box offer data for a supplied marketplace URL and ASIN. Typical uses include pricing checks, competitive monitoring, dataset enrichment, and operational reporting based on public product and seller fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The target Amazon marketplace URL and ASIN are sent to BrowserAct for processing.

Mitigation: Use the skill only for targets you are comfortable submitting to BrowserAct and confirm the marketplace URL and ASIN before execution.

Risk: The BrowserAct API key could be exposed if pasted into chat or logs.

Mitigation: Configure BROWSERACT_API_KEY through the environment or a secret manager rather than sharing the key in conversation.

Risk: Broad routing language may cause the skill to be used for general research tasks outside its intended scope.

Mitigation: Use it as an Amazon Buy Box ASIN scraper, not as a general lead-generation, trend-research, or content-research tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/amazon-buy-box-offers-scraper-api-skill)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=amazon-buy-box-offers-scraper)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Terminal status logs followed by a JSON BrowserAct API response when the run completes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BROWSERACT_API_KEY and sends the supplied Amazon marketplace URL and ASIN to BrowserAct.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
