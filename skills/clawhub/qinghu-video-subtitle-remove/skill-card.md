## Description:

Automatically identifies and removes hard subtitles from videos, repairs the affected frames, and returns clean subtitle-free video material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare videos for reuse, editing, translation, or localization by removing existing hard subtitles and polling for the completed output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading the third-party npm CLI can execute mutable third-party code locally.

Mitigation: Review and pin @iqinghu/qhkit before installation, avoid sudo, global @latest, and npx where possible, and run the workflow in a sandbox.

Risk: Selected videos and API tokens may be sent to the Qinghu service during processing.

Mitigation: Use the skill only with trusted inputs and tokens, and confirm before uploading private videos or setting QHKIT_TOKEN.

Risk: Submitted video tasks can consume credits and may run for a long time.

Mitigation: Disclose credit estimates when supported, confirm before starting credit-consuming work, preserve returned task IDs, and poll status instead of resubmitting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-subtitle-remove)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill submits video-edit jobs, reports task identifiers and credit information when available, polls status, and returns generated video URLs.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
