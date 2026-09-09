## Description:

Uses Qinghu AI's qhkit video_super_resolve workflow to upscale and enhance videos, reducing blur, noise, and compression artifacts with target outputs up to 4K/60fps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to guide video super-resolution jobs through qhkit, including target resolution and frame-rate selection, task polling, and delivery of completed video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos may be uploaded to Qinghu/QHKit for processing.

Mitigation: Confirm user intent before submitting media, limit uploads to the selected files, and avoid sending sensitive videos unless the user accepts the third-party processing risk.

Risk: The skill may install or update mutable third-party command-line software.

Mitigation: Prefer a pinned and reviewed @iqinghu/qhkit package version in an isolated environment, and avoid executing upgrade commands copied from tool output without review.

Risk: qhkit API tokens may be exposed through shell history, logs, or unsafe configuration handling.

Mitigation: Use secure token storage or environment variables where available, avoid echoing secrets, and redact configuration output before sharing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-upscale)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, status polling instructions, credit estimates, and completed video URLs.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
