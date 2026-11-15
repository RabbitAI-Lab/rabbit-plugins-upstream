## Description:

支持通过 AI 生成文章和图文卡片，并推送到微信公众号（无需泄露公众号 Secret，无需配置 IP 白名单）或经由云电脑推送至全球任意站点；兼容其它技能产出的文章、图片与视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lihengdao](https://clawhub.ai/user/lihengdao)

### License/Terms of Use:

MIT-0

## Use Case:

面向内容创作者和开发者，用 AI 生成文章或图文卡片，并将 HTML、图片链接或公网视频 URL 推送到微信公众号草稿箱或已配置的云电脑站点。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports automatic replacement of installed skill code during updates.

Mitigation: Verify the update source and destination before use; disable automatic updates with autoUpdate=false or AIGC_WEB_PUSH_NO_UPDATE=1 if you do not want code replaced automatically.

Risk: The security assessment reports draft-clearing capability.

Mitigation: Review the intended account and the protections around draft deletion before using cleanup functionality.

Risk: The security guidance notes that executable files were not fully scanned.

Mitigation: Review the executable files and publishing destinations before relying on the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lihengdao/aigc-web-push)
- [虾评技能页](https://xiaping.coze.com/skill/015db5c8-8dc6-4c44-b16c-b865ea3c06f0)
- [HTML design guidance](artifact/design.md)
- [Cover design guidance](artifact/design_cover.md)

## Skill Output:

**Output Type(s):** [HTML, Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [HTML content, Markdown guidance, JSON configuration examples, and command-line instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can submit existing image links and public video URLs; the skill does not generate video.]

## Skill Version(s):

3.2.13 (source: artifact/package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
