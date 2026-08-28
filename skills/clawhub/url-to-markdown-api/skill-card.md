## Description:

Read any URL and get it back as clean Markdown, plain text, or raw HTML. One core endpoint, three fetch tiers (1/1/2 credits), and only a successful extraction is billed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to read public URLs and return clean Markdown, plain text, or raw HTML for summarization, quotation, RAG ingestion, or manual parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public URLs and fetched content are shared with Scavio during extraction.

Mitigation: Use the skill only for links that are appropriate to share with Scavio; avoid private, internal, authenticated, secret-bearing, or confidential URLs unless that sharing has been approved.

Risk: The Scavio API key could be exposed if copied into source files, prompts, logs, or examples.

Mitigation: Load SCAVIO_API_KEY from the environment or a secret store and keep it out of source control and user-visible output.

Risk: Blocked, empty, or short extraction results could lead the agent to answer from assumptions instead of page content.

Mitigation: Escalate fetch mode as documented and report that the page could not be read when extraction remains empty; do not invent page content.

## Reference(s):

- [Scavio Extract API Documentation](https://scavio.dev/docs/extract)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON response examples and Python or JavaScript snippets; extracted page content may be Markdown, plain text, or raw HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Sends user-requested public http(s) URLs to Scavio and supports normal, advanced, and ultra fetch modes.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
