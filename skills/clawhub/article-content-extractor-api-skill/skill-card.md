## Description:

This skill helps users run the Article Content Extractor BrowserAct template and extract structured public article data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and operations teams use this skill to run BrowserAct's article extraction template against public article URLs and return structured fields for research, reporting, monitoring, dataset enrichment, or downstream automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article URLs are sent to BrowserAct using the user's BrowserAct API key.

Mitigation: Use public article URLs only, avoid private tokens or internal hostnames in URLs, and install the skill only when BrowserAct processing is acceptable.

Risk: The skill has broad trigger wording around public data extraction and monitoring.

Mitigation: Review and narrow the activation wording before deployment if the skill should activate only for article extraction.

Risk: The skill depends on an external BrowserAct API key and subscription limits.

Mitigation: Confirm BROWSERACT_API_KEY is configured and handle authorization or concurrency-limit errors without repeated retries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/article-content-extractor-api-skill)
- [BrowserAct API Endpoint](https://api.browseract.com/v3/bots)
- [BrowserAct API Key Console](https://www.browseract.com/reception/integrations?co-from=article-content-extractor)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; returns BrowserAct task data as JSON when the API run finishes.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
