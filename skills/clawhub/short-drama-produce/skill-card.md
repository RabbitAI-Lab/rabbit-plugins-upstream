## Description:

在创作者明确确认后，为短剧项目执行图片、视频、配音或音乐生成，并保存成果和简要运行记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者可在确认具体媒体规格后，运行图片、视频、配音或音乐生成任务，并将生成文件和简要运行记录保存到项目中。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery may bypass approval or overwrite results.

Mitigation: Use a corrected version before production; keep backups, recover against the original confirmed specification, preserve successful records, and avoid simultaneous run and collect operations.

Risk: Credential-bearing redirects may expose API keys.

Mitigation: Use a corrected version before supplying real API keys or valuable output files; prevent credential-bearing redirects and restrict download destinations.

## Reference(s):

- [Adapter contract](references/adapter-contract.md)
- [GPT Image 2 provider guide](references/providers/gpt-image-2.md)
- [MiniMax H3 video provider guide](references/providers/minimax-h3-video.md)
- [MiniMax music provider guide](references/providers/minimax-music.md)
- [MiniMax speech provider guide](references/providers/minimax-speech.md)
- [Seedance provider guide](references/providers/seedance.md)
- [OpenAI GPT Image 2 model documentation](https://developers.openai.com/api/docs/models/gpt-image-2)
- [OpenAI image generation API](https://developers.openai.com/api/reference/resources/images/methods/generate)
- [OpenAI image editing API](https://developers.openai.com/api/reference/resources/images/methods/edit)
- [MiniMax music generation API](https://platform.minimax.io/docs/api-reference/music-generation)
- [MiniMax speech generation API](https://platform.minimax.io/docs/api-reference/speech-t2a-http)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, JSON run records]

**Output Format:** [Generated media files and JSON run records saved in the project]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provider calls require confirmation for the specific production job; available formats depend on the configured provider.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
