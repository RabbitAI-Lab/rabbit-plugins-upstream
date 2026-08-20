## Description:

通过 qhkit CLI 自动识别视频语音并翻译为多国语言，支持 AI 配音、字幕与对口型，帮助视频快速面向全球市场。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, localization teams, and agent users use this skill to translate local or hosted videos into supported target languages with optional subtitles, AI dubbing, and lip-sync output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade global tooling and change PATH or system locations.

Mitigation: Review the skill before installing and run setup only in an environment where global tool and PATH changes are acceptable.

Risk: The skill may upload local video files through qhkit.

Mitigation: Use it only for media that is approved for upload to the configured service.

Risk: The skill can persist or reuse API credentials.

Mitigation: Prefer explicit user confirmation before token configuration and use scoped credentials where available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides task submission, status polling, failure handling, and delivery of translated video URLs returned by the CLI.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
