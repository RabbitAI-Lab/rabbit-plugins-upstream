## Description:

Search Google News for headlines by keyword, topic, or publication as structured JSON -- headline, source, date, and link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agent builders use this skill to retrieve fresh Google News headlines for current-events research, media monitoring, and news-aware agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if SCAVIO_API_KEY is written into prompts, source files, or logs.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and avoid echoing it in agent output.

Risk: Sensitive private topics used as news queries are sent to Scavio.

Mitigation: Avoid sending confidential or sensitive private topics unless the user accepts Scavio as the news provider.

Risk: Broad pagination or monitoring can consume paid credits because each request costs one credit.

Mitigation: Tell the user before making wide or repeated requests and monitor remaining credit usage.

## Reference(s):

- [Scavio Google News API documentation](https://scavio.dev/docs/google-news?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-news-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-news-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-news-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API examples and shell setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses include structured JSON news results.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
