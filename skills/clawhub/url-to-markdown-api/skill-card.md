## Description:

Read a public URL and return its page content as clean Markdown, plain text, or raw HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to extract publicly accessible web pages for reading, summarization, or use in retrieval workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested URLs and fetched page content are sent to Scavio.

Mitigation: Use public URLs only; obtain approval before submitting confidential, internal, regulated, authenticated, or private-network content.

Risk: Extraction requires a Scavio API key.

Mitigation: Keep the API key in an environment variable or secret store, not in shared prompts or source files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/scavio-ai/skills/url-to-markdown-api)
- [Scavio Extract documentation](https://scavio.dev/docs/extract?utm_source=agent-skills&utm_medium=skill&utm_campaign=url-to-markdown-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=url-to-markdown-api)

## Skill Output:

**Output Type(s):** [Markdown, Text, HTML]

**Output Format:** [Extracted page content as Markdown, plain text, or raw HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source URL, content length, and extraction mode in the response.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release; source frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
