## Description:

自动识别视频语音并翻译为多国语言，支持 AI 配音、字幕与对口型，帮助视频快速面向全球市场。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate video speech into supported target languages with subtitles, AI dubbing, and optional lip-sync through qhkit video-translate workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed if pasted into chat or supplied directly on the command line.

Mitigation: Have users configure QHKIT_TOKEN themselves in a local environment or use a secure local configuration flow, and avoid asking them to send API keys in chat.

Risk: Local video files supplied to qhkit are uploaded to the provider for processing.

Mitigation: Confirm the user is comfortable uploading the selected media and avoid processing sensitive or unauthorized content.

Risk: Generate actions can spend credits and submitted video tasks cannot be cancelled.

Mitigation: Run supported estimate or options actions first, summarize key parameters and expected credit impact, and wait for explicit user approval before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, status summaries, generated video URLs, and credit estimates or actual credit usage.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
