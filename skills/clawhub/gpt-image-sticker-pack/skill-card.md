## Description:

Turn a photo or a character into an animated sticker pack with GPT Image 2.6 on varg: one approved chibi or mascot still, 6-8 emotions with one short word each, one looping GIF per emotion, then exported and checked against each messenger's animated-sticker spec (Telegram video stickers, WhatsApp animated WebP, LINE APNG, WeChat GIF, Discord, Slack) by scripts/export.sh.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and users can turn an approved photo, pet, or mascot into a coordinated animated sticker pack, then export files for supported messaging platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Photos are sent to Varg and its processing providers; retention and uploaded-link privacy are not established by the bundled files.

Mitigation: Use only photos you are comfortable sending to Varg and its processing providers.

Risk: The export script can incorrectly report success for Discord GIF duration checks.

Mitigation: Independently check the Discord GIF duration before uploading it.

Risk: Sticker generation requires account credentials and incurs generation charges.

Mitigation: Keep VARG_API_KEY private and review expected credits before generating a pack.

## Reference(s):

- [Varg how-to and skill documentation](https://varg.ai/how-to)
- [Varg MCP connection](https://mcp.varg.ai/mcp)
- [Telegram stickers](https://core.telegram.org/stickers)
- [WhatsApp animated sticker requirements](https://github.com/WhatsApp/stickers/blob/main/Android/README.md)
- [LINE animation sticker guidelines](https://creator.line.me/en/guideline/animationsticker/)
- [WeChat sticker specifications](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html#/makingSpecifications)
- [Discord sticker documentation](https://docs.discord.com/developers/resources/sticker)
- [Slack custom emoji help](https://slack.com/help/articles/206870177-Add-custom-emoji-and-aliases-to-your-workspace)

## Skill Output:

**Output Type(s):** [Files, Guidance, Shell commands]

**Output Format:** [Animated sticker files (GIF, WebP, APNG, or WEBM) plus platform-specific export files and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A pack of 6-8 stickers; export scripts prepare files for selected messaging platforms.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
