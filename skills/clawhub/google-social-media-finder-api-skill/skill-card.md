## Description:

This skill helps users run the Google Social Media Finder BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a BrowserAct workflow that searches Google for public social media profiles associated with a person's name and returns structured records for enrichment, reporting, monitoring, or downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may expose a BrowserAct API key if the key is pasted into chat or stored insecurely.

Mitigation: Configure BROWSERACT_API_KEY through the environment or a secrets manager and avoid sharing the key in chat.

Risk: The workflow may return personal contact details such as email, phone, or address fields.

Mitigation: Use the skill only for legitimate public-data collection and review queries and results for privacy, policy, and compliance requirements before reuse.

Risk: Queries and returned results are handled by the external BrowserAct service.

Mitigation: Confirm that BrowserAct is approved for the intended data and use case before running the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/google-social-media-finder-api-skill)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=google-social-media-finder)
- [BrowserAct v3 bots API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [shell commands, configuration, API calls, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; successful runs print the BrowserAct response payload with available structured public-data fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
