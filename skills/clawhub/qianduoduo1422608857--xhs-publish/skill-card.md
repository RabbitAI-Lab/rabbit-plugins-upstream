## Description:

Xhs Publish helps an agent create Xiaohongshu notes by drafting titles and body copy, generating cover images, knowledge cards, or videos, and publishing after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qianduoduo1422608857](https://clawhub.ai/user/qianduoduo1422608857)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and operators use this skill to prepare Xiaohongshu posts, review generated titles, body text, and media assets, and publish through a configured account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automate publishing through a live Xiaohongshu account.

Mitigation: Require an explicit final confirmation before any live post, and review the title, body, and generated media in preview.

Risk: The workflow uses API keys, cookies, or login state for generation and publishing services.

Mitigation: Configure secrets outside chat, avoid pasting cookies or API keys into prompts, and rotate any credential that may have been exposed.

Risk: The documented setup uses latest downloads for MCP packages or binaries.

Mitigation: Pin and verify the MCP package or binary before installation instead of relying on an unverified latest download.

## Reference(s):

- [Title Guide](references/title-guide.md)
- [Content Guide](references/content-guide.md)
- [Cover Guide](references/cover-guide.md)
- [XHS Content Vetter](references/xhs_content_vetter.md)
- [MD2Card setup and account page](https://md2card.cn/zh/login)
- [Xiaohongshu MCP release download](https://github.com/xpzouying/xiaohongshu-mcp/releases/latest/download/xiaohongshu-mcp-linux-amd64.tar.gz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown and plain text with shell command snippets and generated media file references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce titles, body copy, cover images, knowledge-card images, video assets, and publish requests after user confirmation.]

## Skill Version(s):

1.4.5 (source: package.json, _meta.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
