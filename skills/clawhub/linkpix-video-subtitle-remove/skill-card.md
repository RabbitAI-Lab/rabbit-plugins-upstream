## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）自动识别并去除视频字幕，智能修复画面，生成无字幕的干净视频素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to remove hard subtitles from videos before editing, translation, or creating clean source material. It guides an agent through qhkit setup, subtitle-removal task submission, polling, and delivery of processed video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local videos may be uploaded to a third-party service for processing.

Mitigation: Confirm with the user before uploading local media, and avoid private or proprietary videos unless the service terms and token handling are acceptable.

Risk: The skill may install or upgrade npm/Node packages as part of setup.

Mitigation: Ask for confirmation before installing or upgrading packages, and report permission or network failures without retrying repeatedly.

Risk: The workflow may reuse stored qhkit API credentials.

Mitigation: Confirm the credential source before reuse and avoid exposing tokens in logs, command output, or user-facing responses.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-video-subtitle-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit generate/status calls and returns task IDs, polling guidance, credits, and processed video URLs when available.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
