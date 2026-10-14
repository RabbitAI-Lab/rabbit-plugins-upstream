## Description:

Uses Scavio's API to retrieve ChatGPT answers, cited pages, search queries, and product recommendations for AI visibility and brand monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketers use this skill to inspect ChatGPT answers, citations, searches, and recommended products for brand visibility and share-of-voice analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts sent to the service are shared with Scavio's API.

Mitigation: Send only prompts you are comfortable sharing with Scavio.

Risk: API keys could be exposed if embedded in shared code or messages.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store.

Risk: Large prompt batches can consume Scavio credits.

Mitigation: Confirm the batch size and expected credit spend before running it.

## Reference(s):

- [Scavio ChatGPT API documentation](https://scavio.dev/docs/chatgpt-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=chatgpt-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=chatgpt-scraper-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Code]

**Output Format:** [Markdown with cited sources and structured JSON excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers can vary across runs; cited pages and product details may be incomplete.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
