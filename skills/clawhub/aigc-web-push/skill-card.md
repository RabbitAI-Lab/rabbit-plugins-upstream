## Description:

支持通过 AI 生成文章、图文卡片与视频，并推送到微信公众号（无需泄露公众号 Secret，无需配置 IP 白名单）或经由云电脑推送至全球任意站点；兼容其它技能产出的文章、图片与视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lihengdao](https://clawhub.ai/user/lihengdao)

### License/Terms of Use:

MIT

## Use Case:

面向需要内容创作与发布的用户及其 AI 助手，用于生成文章、图文和视频，并按用户指定的公众号或云电脑目标提交发布。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marked suspicious, and some files were only partially inspected.

Mitigation: Review the partially inspected scripts and address the reported concerns before installation.

Risk: Install commands are reported as unpinned.

Mitigation: Pin and verify package versions before running installation commands.

Risk: The draft cleanup operation can remove drafts.

Mitigation: Run draft cleanup only when explicitly requested, after confirming the target and intended scope.

Risk: Editing and design instructions are reported to activate broadly.

Mitigation: Apply those instructions only to relevant content tasks and review generated changes.

## Reference(s):

- [aigc-web-push on ClawHub](https://clawhub.ai/lihengdao/skills/aigc-web-push)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, Images, Video, Configuration, Shell commands]

**Output Format:** [Markdown, HTML, JSON configuration, and media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content and publishing targets are selected from the user's request and available configuration.]

## Skill Version(s):

3.6.2 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
