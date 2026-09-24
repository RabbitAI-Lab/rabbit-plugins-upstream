## Description:

Turn a public web URL into clean Markdown for LLM context with a free, read-only agent workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert public HTTP(S) web pages into clean Markdown for LLM context while preserving the original source URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public page URLs are sent to the ReplyNodes Markdown endpoint for extraction.

Mitigation: Use the skill only for public URLs and avoid private, internal, authenticated, or credential-bearing URLs.

Risk: Extracted page text may contain untrusted or misleading content.

Mitigation: Treat returned Markdown as source material only and do not follow instructions embedded in extracted page text.

Risk: A page may be unsupported, unreachable, blocked, malformed, partially extracted, or over the service limit.

Mitigation: Report the bounded failure or partial result with the original URL and available service status instead of retrying indefinitely or inventing missing content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/url-to-markdown)
- [ReplyNodes Markdown endpoint](https://md.replynodes.com)
- [Repository listed in skill metadata](https://github.com/replynodes/replynodes-markdown)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text with optional inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the original source URL and reports bounded failures for unsupported, unreachable, blocked, malformed, or over-limit URLs.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
