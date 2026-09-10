## Description:

This skill runs BrowserAct's Amazon Product Search Scraper API template to extract structured public Amazon product-search data for research, monitoring, reporting, and downstream automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and business users use this skill to run a BrowserAct Amazon product-search workflow, collect structured public product fields, and use the returned data for market research, competitive monitoring, pricing checks, dataset enrichment, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The BrowserAct API key can be exposed if pasted into an agent conversation or stored in chat history.

Mitigation: Configure BROWSERACT_API_KEY as a local environment variable or approved secret, do not paste the key into chat, and rotate the key if it has already been shared.

Risk: Amazon product-search scraping through BrowserAct may be subject to Amazon or BrowserAct terms and user-specific authorization requirements.

Mitigation: Use the skill only for explicit Amazon BrowserAct product-search extraction tasks, limit collection to appropriate public data, and review applicable Amazon and BrowserAct terms before deployment.

Risk: The skill starts external BrowserAct runs that can fail because of invalid credentials, subscription concurrency limits, network errors, or long-running polling.

Mitigation: Stop on invalid authorization or concurrency-limit messages, remediate the account or key, and retry only once for transient failures or empty results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/amazon-product-search-scraper-api-skill)
- [BrowserAct integrations console](https://www.browseract.com/reception/integrations?co-from=amazon-product-search-scraper)
- [BrowserAct bots API endpoint](https://api.browseract.com/v3/bots)
- [BrowserAct plan upgrade page](https://www.browseract.com/reception/recharge)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text status logs followed by a JSON BrowserAct API response when the run succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python and BROWSERACT_API_KEY; accepts marketplace URL, keyword, and count; polls task status for up to 900 seconds.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
