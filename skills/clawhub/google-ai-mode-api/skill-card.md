## Description:

Get Google's AI Mode answer for a query as structured JSON: AI-generated text blocks, cited references, and shopping results for commercial queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch Google AI Mode answers with cited sources as structured JSON. It is suited for research, verification, and commercial-query workflows that need answer text, references, and shopping results from Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to Scavio's API and each request consumes one credit.

Mitigation: Confirm the third-party data flow and credit cost before use, and reserve calls for queries where Google AI Mode output is needed.

Risk: The skill requires SCAVIO_API_KEY for authentication.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret manager and keep it out of source code.

## Reference(s):

- [Scavio Google AI Mode API Documentation](https://scavio.dev/docs/google-ai-mode)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/google-ai-mode-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response examples and Python code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for calling Scavio's Google AI Mode API and presenting returned text blocks, references, shopping results, and credit metadata.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
