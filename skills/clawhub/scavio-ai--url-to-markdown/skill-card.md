## Description:

Read any URL and get it back as clean Markdown, plain text, or raw HTML. One core endpoint, three fetch tiers (1/1/2 credits), and only a successful extraction is billed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public HTTP(S) pages and return clean Markdown, plain text, or raw HTML for summarization, quotation, RAG ingestion, or downstream parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs and extracted page contents are sent to Scavio, which can disclose sensitive data if users submit private, authenticated, or token-bearing links.

Mitigation: Use only public HTTP(S) URLs unless disclosure is intended, and avoid password-reset links, signed downloads, private documents, query strings with personal data, and internal pages.

Risk: The skill depends on a Scavio API key and a third-party extraction service.

Mitigation: Store SCAVIO_API_KEY as a secret, run in an isolated environment when appropriate, and confirm third-party use is acceptable before deployment.

## Reference(s):

- [Scavio Extract documentation](https://scavio.dev/docs/extract)
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/url-to-markdown)
- [ClawHub publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Markdown, Text, HTML, JSON, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with code blocks and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; extraction mode controls fetch behavior and credits used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
