## Description:

Scrape structured news data from Google News for topical news searches, trend tracking, and PR monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phheng](https://clawhub.ai/user/phheng)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to run BrowserAct-backed Google News searches with keywords, date ranges, and result limits, then retrieve structured article data for monitoring or research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for a BrowserAct API key in chat.

Mitigation: Configure the key locally as BROWSERACT_API_KEY or through an approved secret store, and do not paste it into chat.

Risk: Search keywords and task parameters are sent to BrowserAct.

Mitigation: Use the skill only for queries that are appropriate to share with that third-party service.

Risk: The polling loop may keep waiting if the remote task never completes.

Mitigation: Monitor execution and stop the task if it does not return in an acceptable time window.

## Reference(s):

- [BrowserAct Console integrations](https://www.browseract.com/reception/integrations)
- [ClawHub skill page](https://clawhub.ai/phheng/skills/google-news-api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Structured news data as text or JSON-like output, with setup and error-handling guidance in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns headline, source, news link, published time, and author when available.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
