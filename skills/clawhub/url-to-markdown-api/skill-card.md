## Description:

Read any URL and get it back as clean Markdown, plain text, or raw HTML. One core endpoint, three fetch tiers (1/1/2 credits), and only a successful extraction is billed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and external agents use this skill to fetch a public web page and convert it into Markdown, plain text, or raw HTML for summarization, quoting, RAG preparation, or downstream parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested URLs and fetched page content are processed by Scavio.

Mitigation: Use the skill only for URLs and content that are intended to be disclosed to Scavio.

Risk: Private intranet links, secret-bearing URLs, authenticated pages, or sensitive documents may disclose sensitive information if submitted.

Mitigation: Do not use the skill for those resources unless that disclosure is intended and approved.

## Reference(s):

- [Scavio Extract documentation](https://scavio.dev/docs/extract?utm_source=agent-skills&utm_medium=skill&utm_campaign=url-to-markdown-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=url-to-markdown-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/url-to-markdown-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell and code examples; extraction responses are JSON containing Markdown, plain text, or raw HTML content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Fetch mode controls cost: normal and advanced use 1 credit, ultra uses 2 credits, and only successful extractions are billed.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
