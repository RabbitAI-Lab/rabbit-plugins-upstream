## Description:

Searches Google News for headlines by keyword, topic, or publication and returns structured JSON with headline, source, date, and link fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, journalists, and agent builders use this skill to retrieve current Google News headlines by keyword, topic, section, story, or publication for monitoring, current-events research, and news summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News search terms are sent to Scavio when the agent calls the API.

Mitigation: Use search terms appropriate for third-party processing and choose locale settings that match the user's requested region and language.

Risk: The required SCAVIO_API_KEY can be exposed or API credits can be consumed unexpectedly.

Mitigation: Keep the API key in an environment variable or secret store, and inform the user before broad pagination or repeated searches.

Risk: Current-events answers can become misleading if headlines, sources, dates, or links are fabricated or stale.

Mitigation: Return only API-provided news data and cite source links when summarizing results.

## Reference(s):

- [Scavio Google News API documentation](https://scavio.dev/docs/google-news?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-news-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-news-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-news-api)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell and Python examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses Scavio API credits; Google News requests cost 1 credit each.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
