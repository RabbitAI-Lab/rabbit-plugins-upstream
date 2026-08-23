## Description:

Uses LinkPix/qhkit to remove watermarks, logos, or corner marks from one to ten videos while preserving visual clarity for authorized media cleanup and reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit local video files or public video URLs to LinkPix/qhkit for watermark, logo, or corner-mark removal. It is intended for videos the user owns or is authorized to edit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video files or URLs may be uploaded to the third-party qhkit/LinkPix service for processing.

Mitigation: Use the skill only when the user is comfortable sending the selected videos to that service, and avoid submitting sensitive or unauthorized media.

Risk: Generating video-edit tasks may consume paid credits and submitted tasks may not be cancellable.

Mitigation: Before submission, confirm the exact video inputs and disclose the estimated credit cost when the command supports estimates.

Risk: API keys may be needed outside managed OpenClaw environments.

Mitigation: Prefer secure secrets or environment variables such as QHKIT_TOKEN, and avoid asking users to paste API keys into plain chat when a safer channel is available.

Risk: Removing watermarks from third-party videos can create copyright or licensing risk.

Mitigation: Remind users to process only videos they own or are allowed to edit, especially for commercial reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-watermark-remove)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit installation, configuration, generate, estimate, and status-polling guidance; processed media is returned by service URLs after task completion.]

## Skill Version(s):

0.1.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
