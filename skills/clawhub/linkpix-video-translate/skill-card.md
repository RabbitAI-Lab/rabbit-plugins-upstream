## Description:

自动识别视频语音并翻译为多国语言，支持 AI 配音、字幕与对口型，帮助视频快速面向全球市场。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, localization teams, and marketers use this skill to translate video speech, add foreign-language subtitles, generate dubbed audio, and request lip-sync options for global video distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a paid-service API key and may ask users to provide it during configuration.

Mitigation: Prefer setting QHKIT_TOKEN locally or using a managed secret mechanism; avoid pasting API keys into chat when possible.

Risk: Generate commands can upload video inputs and consume service credits after approval.

Mitigation: Review the uploaded video inputs, language settings, package choice, and estimated credit cost before approving a generate command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command invocations, status polling instructions, package and language selection guidance, and delivery details for generated video URLs.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
