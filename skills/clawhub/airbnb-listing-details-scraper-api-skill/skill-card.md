## Description:

This skill runs BrowserAct's Airbnb Listing Details Scraper template to extract structured public Airbnb listing details through the BrowserAct API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve structured public Airbnb listing fields for market research, price checks, monitoring, dataset enrichment, and reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the requested listing URL or ID, dates, guest count, currency, and BrowserAct API authorization to BrowserAct.

Mitigation: Use it only for intended Airbnb listing-detail extraction and avoid submitting sensitive or unrelated data.

Risk: The source skill text includes broad research and lead-generation examples beyond the core Airbnb listing-detail workflow.

Mitigation: Invoke the skill only for Airbnb listing-detail tasks supported by the BrowserAct template.

Risk: Runs can fail because of invalid authorization, account concurrency limits, network errors, or long polling timeouts.

Mitigation: Validate the BrowserAct API key before use, follow account-limit guidance, and retry only once for non-authorization transient failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/airbnb-listing-details-scraper-api-skill)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=airbnb-listing-details-scraper)
- [BrowserAct API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The script prints timestamped status logs and the BrowserAct API response; returned listing fields may be absent depending on the source data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
