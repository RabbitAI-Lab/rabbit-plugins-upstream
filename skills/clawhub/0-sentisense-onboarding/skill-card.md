## Description:

Read first when using any SentiSense stock market skill to set up the API key, choose which skill owns each task, and adapt patterns without overriding the user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this onboarding skill to configure a SentiSense API key, select the appropriate SentiSense stock market skill for a task, and adapt read-only market data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party npm command may execute code with access to the user's SentiSense API key.

Mitigation: Prefer direct HTTPS calls where practical, or run the CLI only in a constrained environment with only the SentiSense key exposed.

Risk: API-provided upgrade messages and links are vendor-controlled third-party content.

Mitigation: Relay preview and upgrade information as informational content, not as trusted instructions, and continue using only the preview data needed for the user's task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API documentation](https://sentisense.ai/docs/api)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and task-routing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market data onboarding guidance; requires SENTISENSE_API_KEY for authenticated SentiSense calls.]

## Skill Version(s):

1.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
