## Description:

Runs a BrowserAct Google News Full Article Monitor workflow to collect public Google News article text and metadata by keyword.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation users use this skill to run a repeatable BrowserAct workflow for market research, trend monitoring, dataset enrichment, and public article collection from Google News.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed if pasted into the agent conversation.

Mitigation: Configure BROWSERACT_API_KEY through a local environment variable or approved secret manager before running the skill.

Risk: Search parameters are sent to BrowserAct when the workflow runs.

Mitigation: Use the skill only when BrowserAct execution is intentional and avoid sensitive keywords unless sharing them with BrowserAct is acceptable.

Risk: Broad invocation language could trigger BrowserAct collection when the user expected only advice.

Mitigation: Confirm the user's intent to run the Google News BrowserAct template before executing commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/google-news-full-article-monitor-api-skill)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=google-news-full-article-monitor)
- [BrowserAct bots API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BROWSERACT_API_KEY and sends keyword, date range, and article count parameters to BrowserAct.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
