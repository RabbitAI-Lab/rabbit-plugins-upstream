## Description:

Read any URL and get it back as clean Markdown, plain text, or raw HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public web pages and convert them into Markdown, plain text, or raw HTML for summarization, quoting, parsing, prompts, or retrieval workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted URLs and fetched page content are processed by Scavio as a third-party service.

Mitigation: Use the skill only for links appropriate for third-party processing, and avoid private, signed, tokenized, internal, or confidential URLs unless the user explicitly accepts that risk.

Risk: Optional SDK installation can add third-party dependencies to the agent environment.

Mitigation: Prefer isolated environments for optional Python or JavaScript SDK installs.

Risk: Empty or unusually short extracted content can reflect a bot wall or client-rendered page rather than a truly blank source.

Mitigation: Escalate fetch mode as documented before reporting that a page has no readable content, and do not invent page content.

## Reference(s):

- [Scavio Extract API documentation](https://scavio.dev/docs/extract?utm_source=agent-skills&utm_medium=skill&utm_campaign=url-to-markdown-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=url-to-markdown-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/url-to-markdown-api)

## Skill Output:

**Output Type(s):** [Markdown, Text, HTML, JSON, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown, plain text, raw HTML, JSON API responses, and inline code or shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; extraction format and mode affect returned content and credit use.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
