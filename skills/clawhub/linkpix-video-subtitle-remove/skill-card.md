## Description:

AI视频字幕消除工具 | LinkPix removes hard subtitles from videos with LinkPix/qhkit and returns clean video material for translation or reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to remove hard subtitles from one to ten local or public video files before translation or reuse. The skill guides agents through qhkit setup, user confirmation before credit-spending submission, polling, and delivery of returned video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads selected local video files or provided URLs to the LinkPix/Qinghu service.

Mitigation: Use it only for media that the user is permitted and comfortable to submit to that external service.

Risk: The skill uses qhkit/OpenClaw account credentials and may spend account credits when a generation task is submitted.

Mitigation: Require explicit user confirmation of parameters and expected or actual credit usage before calling generate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-subtitle-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash command examples and qhkit JSON request/response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits video-edit remove_subtitle jobs only after explicit user confirmation; returns task IDs, polling status, generated video URLs, and credit information when available.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
