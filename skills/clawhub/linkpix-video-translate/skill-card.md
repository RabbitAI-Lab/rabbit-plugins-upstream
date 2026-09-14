## Description:

自动识别视频语音并翻译为多国语言，支持生成外语字幕、AI 配音和对口型视频，帮助视频内容面向全球受众本地化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate video speech into supported target languages through LinkPix/qhkit, producing localized subtitles, AI dubbing, and optional lip-sync video for global content workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or auto-upgrade an unpinned global qhkit CLI.

Mitigation: Review the qhkit package before use and prefer a pinned or local install path where the deployment environment supports it.

Risk: The workflow uploads selected local videos to the LinkPix/qhkit service.

Mitigation: Confirm that the user has rights to upload the media and is comfortable sending the content to that provider before starting a job.

Risk: The workflow may persist API credentials or ask for a token.

Mitigation: Provide tokens only when needed, avoid exposing them in shared logs, and rotate or remove stored credentials when access is no longer required.

Risk: Generated video jobs may consume credits and cannot be canceled after submission.

Mitigation: Confirm the requested package and estimated credits before running generate, then preserve the returned task ID for status checks and delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, markdown]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command parameters, task IDs, polling status, produced video URLs, and credit-use notes.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
