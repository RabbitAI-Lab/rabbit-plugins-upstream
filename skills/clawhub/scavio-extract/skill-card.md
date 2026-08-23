## Description:

Read any URL and get it back as clean Markdown, plain text, or raw HTML. One core endpoint, three fetch tiers (1/1/2 credits), and only a successful extraction is billed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to fetch public web pages into clean Markdown, plain text, or raw HTML for summarization, quoting, RAG chunks, and page-content analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: URLs requested through the skill are shared with Scavio for extraction.

Mitigation: Use the skill only for URLs that are appropriate to disclose to Scavio.

Risk: The skill requires a Scavio API key in the environment.

Mitigation: Store SCAVIO_API_KEY in a secret manager or local environment variable and do not commit it to source control.

Risk: Private, logged-in, or paywalled pages may expose sensitive access expectations or fail to extract correctly.

Mitigation: Use the skill for public pages only and avoid sending authenticated, private, or paywalled content.

Risk: The ultra extraction mode costs more credits than normal or advanced mode.

Mitigation: Start with normal or advanced mode and escalate to ultra only when cheaper tiers return blocked or empty content.

## Reference(s):

- [Scavio Extract documentation](https://scavio.dev/docs/extract)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response examples and Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and can return extracted page content as Markdown, plain text, or HTML.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
