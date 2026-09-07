## Description:

This skill helps users run the Airbnb Property Listings Scraper BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to run a BrowserAct workflow that collects structured public Airbnb listing data for market research, pricing checks, monitoring, reporting, dataset enrichment, and downstream automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt users to provide a BrowserAct API key through agent chat when BROWSERACT_API_KEY is missing.

Mitigation: Configure BROWSERACT_API_KEY through a protected local environment or secret manager, and rotate the key if it was pasted into an agent conversation.

Risk: Using the skill sends requested parameters and returned results through BrowserAct.

Mitigation: Use the skill only when BrowserAct Airbnb listing extraction is acceptable for the data and workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/airbnb-property-listings-scraper-api-skill)
- [BrowserAct API endpoint](https://api.browseract.com/v3/bots)
- [BrowserAct API key setup](https://www.browseract.com/reception/integrations?co-from=airbnb-property-listings-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill configures location and maximum property count, starts a BrowserAct template run, polls status, and prints returned listing fields when available.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
