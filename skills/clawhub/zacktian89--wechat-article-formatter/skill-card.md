## Description:

生成、规范化、主题化和预览 HTML 优先的微信公众号文章，让正文可复制到微信后台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zacktian89](https://clawhub.ai/user/zacktian89)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and developers use this skill to turn topics, briefs, notes, outlines, Markdown, or existing HTML into WeChat-friendly article HTML. It supports copy-ready article bodies, local preview pages, theme presets, and image inlining for WeChat Official Account publishing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted HTML or preview content could carry unsafe behavior into the local preview and copy workflow.

Mitigation: Use only trusted article drafts or review third-party HTML before previewing, copying, or publishing it.

Risk: Untrusted local image paths, absolute paths, or parent-directory paths could expose local files during Base64 image inlining.

Mitigation: Use trusted local assets only, avoid absolute and parent-directory image paths, and inspect generated Data URLs before handoff.

Risk: Untrusted custom theme or style JSON could change preview behavior or styling unexpectedly.

Mitigation: Prefer the bundled theme presets and use custom theme/style JSON only after review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zacktian89/skills/wechat-article-formatter)
- [Output Contract](artifact/references/output-contract.md)
- [Preview Page Contract](artifact/references/preview-implementation.md)
- [Image Rules](artifact/references/image-rules.md)
- [Theme Presets](artifact/references/theme-presets.md)
- [Visual & Formatting Guidelines](artifact/references/visual-guidelines.md)
- [Style Completeness Checklist](artifact/references/completeness-checklist.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with HTML snippets, shell commands, and generated self-contained HTML preview files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write copy-ready article#wechatArticle HTML or a complete local preview page, normally under dist/.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
