## Description:

This skill helps an agent use LinkPix/qhkit to remove hard subtitles from videos and repair the affected frames to produce clean, subtitle-free footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to remove hard subtitles from 1-10 videos before translation, localization, or editing. It submits LinkPix/qhkit video-edit jobs, polls for completion, and returns the generated subtitle-free video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install or upgrade a mutable global qhkit CLI.

Mitigation: Use a pinned, task-scoped install where possible and require explicit approval before running install or upgrade commands.

Risk: Local video files may be uploaded to LinkPix/qhkit for processing.

Mitigation: Use only videos the user is comfortable uploading, and avoid sensitive or confidential footage unless the service is trusted for that content.

Risk: The external CLI may return upgrade or configuration messages that affect execution.

Mitigation: Review CLI messages before acting, retry only after the requested install, upgrade, or token configuration is understood, and report user-facing failure messages without repeated retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-subtitle-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to submit qhkit jobs, poll status, report failures, and return completed video URLs with credit usage when available.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
