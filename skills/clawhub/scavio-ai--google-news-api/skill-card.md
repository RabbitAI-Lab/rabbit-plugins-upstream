## Description:

Search Google News for headlines by keyword, topic, or publication as structured JSON — headline, source, date, and link. Use for current events, monitoring, and news research. v2 engine, 1 credit per request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, researchers, journalists, and agents use this skill to retrieve fresh Google News headlines for current-events questions, media monitoring, and news research. It supports keyword, topic, section, story, publication, and entity-based news lookups with regional and language options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News queries and the SCAVIO_API_KEY are sent to Scavio.

Mitigation: Use the skill only when that disclosure is acceptable, keep the API key in environment or secret storage, and avoid placing secrets in source files or prompts.

Risk: Each API request consumes one Scavio credit.

Mitigation: Inform users before broad pagination or repeated monitoring calls, and stop or narrow requests when credit use may exceed expectations.

Risk: News results may be regionally or linguistically mismatched if localization is omitted.

Mitigation: Set gl and hl to match the user's intended country and language whenever location or language matters.

Risk: Current-events answers can be misleading if headlines, sources, dates, or links are fabricated or summarized without attribution.

Mitigation: Use only returned API data for news claims and cite the returned source and link when summarizing results.

## Reference(s):

- [Scavio Google News API documentation](https://scavio.dev/docs/google-news?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-news-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-news-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/google-news-api)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance]

**Output Format:** [Structured JSON from the API, with optional markdown summaries, shell setup commands, and code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Each request costs one credit and may use gl and hl parameters for country and language targeting.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
