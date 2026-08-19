## Description:

Read any URL and get it back as clean Markdown, plain text, or raw HTML. One core endpoint, three fetch tiers (1/1/2 credits), and only a successful extraction is billed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public web pages and convert them into clean Markdown, plain text, or raw HTML for summarization, quoting, RAG ingestion, or downstream parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: URLs and resulting page content are sent to Scavio under the user's API key and credit balance.

Mitigation: Use the skill only for URLs where sharing the address and extracted content with Scavio is intended; avoid private or sensitive URLs unless that sharing is acceptable.

Risk: The skill consumes credits by extraction mode when a request succeeds.

Mitigation: Start with normal or advanced mode and escalate to ultra only when cheaper modes return blocked or empty content.

## Reference(s):

- [Scavio Extract Documentation](https://scavio.dev/docs/extract)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/url-to-markdown)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, Python, JavaScript, JSON examples, and extracted page content in Markdown, text, or HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Extraction mode affects credits: normal and advanced use 1 credit; ultra uses 2 credits; only successful extractions are billed.]

## Skill Version(s):

1.0.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
