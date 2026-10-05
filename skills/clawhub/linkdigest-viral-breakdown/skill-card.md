## Description:

分析单条抖音、小红书、TikTok 或 YouTube 内容的钩子、结构节拍、标题和行动号召，核对引用与提取出的原文，并提供可复用模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketers use this skill to study the structure of a single social-media post, compare examples and plan an original adaptation without mistaking generated analysis for original quotes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links or share text are sent to LinkDigest; results for public links may be cached and third-party model services may be used.

Mitigation: Use only public, nonsensitive content and avoid private or login-only links.

Risk: The LinkDigest API key could be exposed if included in chat, code or shared output.

Mitigation: Keep LINKDIGEST_API_KEY in environment variables or private configuration.

Risk: The optional unpinned npx MCP command may run an unexpected package version.

Mitigation: Use the provided Python or curl workflow, or pin and review the MCP package before running it.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest API key setup](https://linkdigest.dev/app/keys)
- [ClawHub skill listing](https://clawhub.ai/jackchew7143/skills/linkdigest-viral-breakdown)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON breakdown of one social-media post]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approximate time or image markers, source-text-checked quotes, missing-information notices, a reusable structure template and a dated engagement snapshot when available.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
