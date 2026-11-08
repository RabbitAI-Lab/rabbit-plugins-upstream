## Description:

在创作者明确确认后，执行短剧项目的图片、视频、TTS/配音或时间线音乐生产任务，并把结果与精简运行记录存回项目。用户说“生成这张图/这段视频/这句配音/这段配乐”“开始跑图/跑视频/合成语音/生成音乐”“把已确认提示词送去生产”，或要求批量执行已确认媒体任务时使用；不负责创作提示词、镜头、台词、歌词或声音身份，也绝不把预览、继续、预算说明或既有接受状态当作本次付费生产确认。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者可用它将已写好并确认的图片、视频、配音或音乐规格提交给配置好的生成服务，并把媒体结果与运行记录保存到项目中。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security report flags paid-job authorization and network redirect/download risks; its review is incomplete because two local path-like references were unresolved.

Mitigation: Review each complete job preview and require a fresh explicit confirmation before paid production. Keep credentials in the environment or system credential store, with adapter configuration outside the project.

Risk: An interrupted provider task may already have been submitted, and retrying can duplicate paid work.

Mitigation: Run the documented audit and collect workflow to recover an existing provider job before preparing a retry.

## Reference(s):

- [Adapter contract](references/adapter-contract.md)
- [GPT Image 2 adapter](references/providers/gpt-image-2.md)
- [GPT Image 2 model](https://developers.openai.com/api/docs/models/gpt-image-2)
- [GPT image generation API](https://developers.openai.com/api/reference/resources/images/methods/generate)
- [GPT image edits API](https://developers.openai.com/api/reference/resources/images/methods/edit)
- [MiniMax H3 video adapter](references/providers/minimax-h3-video.md)
- [MiniMax video generation API](https://platform.minimax.io/docs/api-reference/video-generation-v2-create)
- [MiniMax Music adapter](references/providers/minimax-music.md)
- [MiniMax Music API](https://platform.minimax.io/docs/api-reference/music-generation)
- [MiniMax speech adapter](references/providers/minimax-speech.md)
- [MiniMax Text to Speech API](https://platform.minimax.io/docs/api-reference/speech-t2a-http)
- [Seedance adapter](references/providers/seedance.md)
- [Volcengine video generation API](https://www.volcengine.com/docs/82379/1520757)

## Skill Output:

**Output Type(s):** [Image files, Video files, Audio files, Production run records]

**Output Format:** [Generated media files with concise JSON run records]

**Output Parameters:** [1D — one modality and bounded job per confirmed run]

**Other Properties Related to Output:** [Results are saved under the project; each paid production requires a fresh preview and explicit confirmation.]

## Skill Version(s):

1.0.7 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
