## Description:

一键去除视频水印，保持视频画质清晰，适用于素材整理及二次创作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content workflow agents use this skill to submit one to ten videos for LinkPix/qhkit watermark or logo removal, then poll for generated video URLs. It is intended for video cleanup and material preparation when the user has confirmed the files, expected cost, and account/token to use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload local videos or remote video URLs to a third-party cloud service for processing.

Mitigation: Require explicit user confirmation of the exact files or URLs before upload and use only material the user is authorized to process.

Risk: The qhkit CLI may reuse an existing Qinghu/OpenClaw token or require a user-provided token.

Mitigation: Confirm the account and token source before use, and avoid exposing tokens in chat, logs, or command output.

Risk: Setup can install or upgrade global Node/npm tooling on the host.

Mitigation: Ask for approval before host installation or upgrade steps, and use npx or a user-scoped install path when global permissions are not appropriate.

Risk: Video generation tasks can consume account credits and cannot be canceled after submission.

Mitigation: Run only read-only estimate or status calls before confirmation, then restate key parameters and expected or actual credit handling before generate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-watermark-remove)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit generate and status calls; completed tasks return video URLs through the service.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
