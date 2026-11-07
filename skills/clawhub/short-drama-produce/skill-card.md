## Description:

在创作者明确确认后，执行短剧项目的图片、视频、TTS/配音或时间线音乐生产任务，并把结果与精简运行记录存回项目。用户说“生成这张图/这段视频/这句配音/这段配乐”“开始跑图/跑视频/合成语音/生成音乐”“把已确认提示词送去生产”，或要求批量执行已确认媒体任务时使用；不负责创作提示词、镜头、台词、歌词或声音身份，也绝不把预览、继续、预算说明或既有接受状态当作本次付费生产确认。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者在提示词和素材已准备好后，用此技能预览并提交图片、视频、配音或音乐生产任务。它要求创作者对当前任务明确确认，并将结果和运行记录保存到项目中。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags uncertainty about whether paid jobs always require current confirmation; its coverage was partial.

Mitigation: Review the full preview and require explicit confirmation for the exact paid job. Reprepare and reconfirm after any job input or output changes.

Risk: The security review flags whether previously produced results can be saved to newly selected locations.

Mitigation: Check every output destination in the preview and use the audit report to verify saved files against their run records.

Risk: The security review flags whether network redirects are safely constrained; its analysis was partial.

Mitigation: Use a reviewed adapter configuration with documented provider endpoints, and review redirect behavior before enabling production.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/short-drama-produce)
- [Adapter Contract](references/adapter-contract.md)
- [GPT Image 2 adapter](references/providers/gpt-image-2.md)
- [GPT Image 2 model documentation](https://developers.openai.com/api/docs/models/gpt-image-2)
- [MiniMax H3 video adapter](references/providers/minimax-h3-video.md)
- [MiniMax video generation API](https://platform.minimax.io/docs/api-reference/video-generation-v2-create)
- [MiniMax Music adapter](references/providers/minimax-music.md)
- [MiniMax Music Generation API](https://platform.minimax.io/docs/api-reference/music-generation)
- [MiniMax Speech adapter](references/providers/minimax-speech.md)
- [MiniMax Text to Speech API](https://platform.minimax.io/docs/api-reference/speech-t2a-http)
- [Seedance adapter](references/providers/seedance.md)
- [Volcengine video generation API](https://www.volcengine.com/docs/82379/1520757)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, JSON job and run records, Production guidance]

**Output Format:** [Image, video, and audio files; JSON job and run records; Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each job covers one media modality and uses the creator-confirmed prompt, references, parameters, and output targets.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
