## Description:

LINE 貼圖生成與製作工作流。使用於規劃角色與貼圖套組、產生 4x3 網格圖提示詞、製作繁體中文貼圖文字、檢查角色一致性與文字可讀性，以及搭配 line-sticker-factory 切圖、去背、預覽和 ZIP 匯出時。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qpooqp777](https://clawhub.ai/user/qpooqp777)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, and agents producing Traditional Chinese LINE sticker sets use this skill to plan character consistency, draft 12-panel sticker copy, generate image prompts, and check readability and background-removal quality before export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maintainer TODO and release notes may be mistaken for normal sticker-generation steps.

Mitigation: Treat todo.md and release sections as maintenance context, and run git, npm, publishing, or release commands only after explicitly choosing to work on those related projects.

Risk: Generated sticker images can contain incorrect Traditional Chinese text, cropped lettering, inconsistent characters, or background-removal defects.

Mitigation: Use the skill's per-panel quality checklist before export, and regenerate or post-process only the failing panel when a defect is found.

Risk: Sticker concepts involving real people, brands, workplace jokes, or third-party characters can create rights, privacy, or harassment concerns.

Mitigation: Confirm authorization for protected material and apply the Traditional Chinese and workplace-risk review rules to replace sensitive or targeted copy with neutral alternatives.

## Reference(s):

- [line-sticker-factory integration reference](references/line-sticker-factory.md)
- [Traditional Chinese sticker copy check rules](references/zh-tw-copy-check.md)
- [Workplace meme catalog](references/workplace-meme-catalog.md)
- [Top 10 sticker copy and layout guide](references/top-10-sticker-copy-guide.md)
- [Little monk kind-words site integration reference](references/little-monk-kind-words-site.md)
- [LINE sticker 4x3 grid prompt template](templates/line-sticker-prompt-template.md)
- [line-sticker-factory reference project](https://github.com/qpooqp777/line-sticker-factory)
- [Little monk kind-words public site](https://qpooqp777.github.io/little-monk-kind-words-site/)
- [Little monk kind-words site repository](https://github.com/qpooqp777/little-monk-kind-words-site)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with structured sticker scripts, prompt templates, checklists, and occasional shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs usually describe a 12-panel sticker plan, image-generation prompt, Traditional Chinese copy checks, and post-generation quality review steps.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
