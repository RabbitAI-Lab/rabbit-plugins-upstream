## Description:

Get Google's AI Mode answer for a query as structured JSON: AI-generated text blocks, cited references, and shopping results for commercial queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Scavio's Google AI Mode endpoint, retrieve AI-generated answer text, and return cited references or shopping results for user-facing research and commercial queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to Scavio's API.

Mitigation: Use the skill only when external processing by Scavio is acceptable for the query.

Risk: API calls spend Scavio credits.

Mitigation: Treat each request as billable usage and avoid unnecessary retries.

Risk: The Scavio API key could be exposed if placed directly in source or chat transcripts.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store.

Risk: AI Mode answers may omit context or be hard to verify without sources.

Mitigation: Present the returned references with the answer and avoid fabricating missing answer text, sources, or products.

## Reference(s):

- [Scavio Google AI Mode documentation](https://scavio.dev/docs/google-ai-mode)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-ai-mode)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Text, JSON, API Calls, Guidance]

**Output Format:** [Structured JSON from the API with agent-facing Markdown summaries when presenting answers and sources.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each request costs 1 Scavio credit; answers should include returned references for verification.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
