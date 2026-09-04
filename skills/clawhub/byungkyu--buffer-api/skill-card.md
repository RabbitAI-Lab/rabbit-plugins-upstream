## Description:

Buffer API integration with managed authentication that helps agents schedule and manage social media posts across multiple platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Buffer accounts, organizations, channels, schedules, posts, and content ideas, and to create or schedule Buffer posts after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or schedule public social media posts in a connected Buffer account.

Mitigation: Require explicit user confirmation of the target channel, post content, and schedule before any write operation.

Risk: Requests could affect the wrong Buffer account when multiple Maton profiles or Buffer connections exist.

Mitigation: Use explicit profile and connection selection, and verify account context with read or list calls before writes.

Risk: Long-lived API keys can leak through logs, shell history, or copied output when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI, never print credentials, and keep any fallback API key in the process environment only.

## Reference(s):

- [Buffer API Documentation](https://developers.buffer.com/reference.html)
- [Buffer API Getting Started](https://developers.buffer.com/guides/getting-started.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/buffer-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces API call guidance and command examples for Buffer operations through the Maton CLI or SDKs.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
