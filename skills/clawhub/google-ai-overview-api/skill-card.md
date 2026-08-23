## Description:

Get Google's AI Mode answer for a query as structured JSON, including AI-generated text blocks, cited references, and shopping results for commercial queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Google's AI Mode through Scavio and return answer text with cited references for grounding, verification, product research, or regionalized search tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and optional location or language parameters are sent to Scavio's external API.

Mitigation: Avoid sending sensitive searches or precise location data unless those details are necessary for the task.

Risk: Each request costs one Scavio credit and may be subject to rate or usage limits.

Mitigation: Confirm the query before calling the API and handle 429 responses by waiting before retrying.

Risk: The returned AI Mode answer and cited references come from an external service and may be incomplete or unavailable for some queries.

Mitigation: Return only API-provided text_blocks, references, and shopping results, and surface references so users can verify sources.

## Reference(s):

- [Scavio Google AI Mode documentation](https://scavio.dev/docs/google-ai-mode)
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-ai-overview-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response examples and Python API-call snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve API-provided text_blocks, references, shopping_results, credit usage, and error status without fabrication.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
