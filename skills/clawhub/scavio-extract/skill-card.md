## Description:

Read any URL and get it back as clean Markdown, plain text, or raw HTML. One core endpoint, three fetch tiers (1/1/2 credits), and only a successful extraction is billed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public web pages into Markdown, plain text, or raw HTML for summarization, quoting, RAG chunking, and downstream parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: URLs are sent to Scavio for server-side fetching, and fetched contents may be processed by a third-party service.

Mitigation: Do not use this skill on secret-bearing signed URLs, private documents, internal-only links, or regulated data unless the user explicitly approves that Scavio may process those URLs and contents.

Risk: A successful fetch can still return short or incomplete content when a page is blocked, client-rendered, or otherwise hard to read.

Mitigation: Start with normal mode, escalate to advanced or ultra only when needed, and report an unreadable page instead of inventing page content.

Risk: Using the skill requires a Scavio API key.

Mitigation: Read the key from SCAVIO_API_KEY and avoid embedding it in prompts, checked-in files, URLs, or visible examples.

## Reference(s):

- [Scavio Extract Documentation](https://scavio.dev/docs/extract)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-extract)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with API examples and extracted page content in Markdown, plain text, or HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; extraction mode controls credit cost and fetch behavior.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
