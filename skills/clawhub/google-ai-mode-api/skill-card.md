## Description:

Get Google's AI Mode answer for a query as structured JSON, including AI-generated text blocks, cited references, and shopping results for commercial queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Google AI Mode responses with source references and optional shopping results for a user query. It is useful when an agent needs grounded answer text from Google's AI Mode through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to Scavio's external API endpoint.

Mitigation: Avoid highly sensitive private queries unless Scavio's terms and data handling meet the user's needs.

Risk: The skill requires a Scavio API key and consumes one Scavio credit per request.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret manager and confirm the user is comfortable with credit usage before repeated calls.

Risk: Returned AI Mode answers, references, or shopping results may be incomplete or unavailable for some queries.

Mitigation: Return only API-provided data, surface references for verification, and handle empty answers or API failures explicitly.

## Reference(s):

- [Scavio Google AI Mode API documentation](https://scavio.dev/docs/google-ai-mode?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-ai-mode-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-ai-mode-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/google-ai-mode-api)

## Skill Output:

**Output Type(s):** [text, json, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and Python examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Each request sends the query to Scavio and consumes one Scavio credit.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
