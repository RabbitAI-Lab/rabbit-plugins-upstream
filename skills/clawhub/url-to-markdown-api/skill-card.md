## Description:

Read any URL and get it back as clean Markdown, plain text, or raw HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public web pages and convert them into Markdown, plain text, or raw HTML for summarization, quoting, RAG ingestion, or downstream parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: URLs submitted through the skill are sent to Scavio with the user's API key and may consume credits on successful extraction.

Mitigation: Avoid sending private, sensitive, or access-controlled pages unless that is intended, and price each run by mode before use.

Risk: Extracted page content can be incomplete when a page is blocked, client-rendered, or returns a short successful response.

Mitigation: Start with normal mode, escalate to advanced or ultra when needed, and state when a page could not be read instead of inventing content.

## Reference(s):

- [Scavio Extract API documentation](https://scavio.dev/docs/extract)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/url-to-markdown-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with API request examples and response JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and produces guidance for selecting extract format and fetch mode.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
