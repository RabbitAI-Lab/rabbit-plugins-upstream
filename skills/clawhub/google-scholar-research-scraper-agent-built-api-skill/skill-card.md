## Description:

This skill helps users run the Google Scholar Research Scraper Bot BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to run a BrowserAct workflow that searches public Google Scholar results and returns structured research metadata for reporting, monitoring, enrichment, or downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may return personal contact-style fields along with Google Scholar metadata.

Mitigation: Use the skill only for lawful and appropriate public-data collection, and avoid broad enrichment or outreach workflows unless there is a clear basis to process that data.

Risk: The skill sends search tasks to BrowserAct using the user's API key.

Mitigation: Confirm the user intends to use BrowserAct for the task and require BROWSERACT_API_KEY before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/google-scholar-research-scraper-agent-built-api-skill)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=google-scholar-research-scraper)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Terminal logs and JSON API response payload]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python and BROWSERACT_API_KEY; accepts keyword and count inputs; task polling may run for several minutes.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
