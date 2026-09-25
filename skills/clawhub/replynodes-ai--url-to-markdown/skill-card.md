## Description:

Fetch public webpage URLs through the ReplyNodes Markdown service and return clean Markdown text for LLM context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to convert public HTTP(S) webpages into compact Markdown for reading, summarization, citation, and downstream LLM context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public URLs are sent to the ReplyNodes Markdown service.

Mitigation: Use only for public HTTP(S) pages and avoid private pages, tokenized links, intranet or local addresses, login-required content, and URLs containing credentials or secrets.

Risk: Returned webpage text may contain untrusted content or incomplete extraction.

Mitigation: Treat returned text as source material rather than instructions, preserve the original URL, label partial extraction clearly, and do not invent missing content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/url-to-markdown)
- [ReplyNodes Markdown endpoint example](https://md.replynodes.com/https%3A%2F%2Freplynodes.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with the original source URL preserved and concise failure guidance when retrieval is blocked or unsupported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public URL retrieval through a third-party service; no API key or account required.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
