## Description:

Turn a photo or character into a set of animated stickers with GPT Image 2.6, then export them for supported messaging platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn an approved photo, pet, or mascot into a coordinated animated sticker pack and prepare files for messaging platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal photos are sent to external image services, and the scan reports a privacy disclosure gap.

Mitigation: Before using a personal photo, confirm which external services will receive it and authorize that transfer.

Risk: The scan reports an output-checking flaw that could leave incorrect sticker frames or captions undetected.

Mitigation: Review each sticker's frames, caption, loop, and exported format before sharing or submitting the pack.

Risk: The export script was only partially inspected, leaving important evidence missing.

Mitigation: Review scripts/export.sh and the generated files before running exports or distributing the results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/gpt-image-sticker-pack)
- [varg sticker pack guide](https://varg.ai/how-to/skills/gpt-image-sticker-pack)
- [Telegram sticker requirements](https://core.telegram.org/stickers)
- [WhatsApp sticker requirements](https://github.com/WhatsApp/stickers/blob/main/Android/README.md)
- [LINE animation sticker guidelines](https://creator.line.me/en/guideline/animationsticker/)
- [WeChat sticker specifications](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html#/makingSpecifications)
- [Discord sticker documentation](https://docs.discord.com/developers/resources/sticker)
- [Slack custom emoji help](https://slack.com/help/articles/206870177-Add-custom-emoji-and-aliases-to-your-workspace)

## Skill Output:

**Output Type(s):** [Files, Guidance, Shell commands]

**Output Format:** [Animated image files (GIF, WebP, APNG, or WebM) with export guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A coordinated pack of 6–8 stickers with platform-specific exports.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
