## Description:

Gets Google's AI Mode answer for a query as structured JSON, including AI-generated text blocks, cited references, and shopping results for commercial queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to call Scavio's Google AI Mode API, return AI answer text with cited sources, and surface shopping results for commercial queries. It is useful when a workflow needs structured Google AI Mode output instead of an uncited free-form answer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, optional location or locale fields, and account-linked API usage are sent to Scavio.

Mitigation: Do not use the skill with secrets, credentials, regulated data, or private personal content unless that data sharing has been approved.

Risk: Returned AI Mode answers may be incomplete, unavailable for some queries, or dependent on cited sources returned by the API.

Mitigation: Present API-provided references with the answer and avoid fabricating answers, sources, or product results when the API response is empty.

## Reference(s):

- [Google AI Mode API documentation](https://scavio.dev/docs/google-ai-mode)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-ai-mode-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON from the API, usually summarized for users in Markdown with cited source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; requests may include query, device, language, country, Google domain, location, safe-search, and HTML-inclusion options.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
