## Description:

LINE 貼圖生成與製作工作流。使用於規劃角色與貼圖套組、產生 4x3 網格圖提示詞、製作繁體中文貼圖文字、檢查角色一致性與文字可讀性，以及搭配 line-sticker-factory 切圖、去背、預覽和 ZIP 匯出時。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qpooqp777](https://clawhub.ai/user/qpooqp777)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, and agent users use this skill to plan LINE sticker packs, draft 12-panel Traditional Chinese sticker scripts, generate 4x3 image prompts, and review character consistency, text readability, background removal, and export readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may treat publisher-maintenance notes as sticker-generation instructions.

Mitigation: Review or remove artifact/todo.md before deployment when maintenance tasks should not be visible to agents.

Risk: Optional companion project commands or image uploads may be performed unintentionally.

Mitigation: Run companion project commands and upload images only when the user explicitly intends to use those tools.

Risk: Sticker text or source imagery may involve real people, brands, third-party characters, confidential information, or public marketplace requirements.

Mitigation: Confirm rights and platform rules before commercial use, avoid unpublished sensitive information, and review official LINE submission requirements separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qpooqp777/skills/line-sticker-master)
- [line-sticker-factory](https://github.com/qpooqp777/line-sticker-factory)
- [Little Monk Kind Words Site](https://qpooqp777.github.io/little-monk-kind-words-site/)
- [little-monk-kind-words-site repository](https://github.com/qpooqp777/little-monk-kind-words-site)
- [Traditional Chinese copy check](references/zh-tw-copy-check.md)
- [Workplace meme catalog](references/workplace-meme-catalog.md)
- [Top 10 sticker copy guide](references/top-10-sticker-copy-guide.md)
- [LINE sticker prompt template](templates/line-sticker-prompt-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured sticker scripts, prompt code blocks, review tables, and optional setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce 12-panel sticker scripts, 4x3 image-generation prompts, Traditional Chinese copy checks, quality-control tables, and guidance for background removal and ZIP export.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
