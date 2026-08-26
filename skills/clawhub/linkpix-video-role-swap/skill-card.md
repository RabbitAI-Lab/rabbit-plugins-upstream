## Description:

Replaces a person in a source video with a supplied character image through LinkPix/qhkit while preserving the original motion and lip movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent operators use this skill to replace people in videos for role swap, face swap, digital human, model localization, and cross-market creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos and character images are uploaded to the qhkit/iqinghu service.

Mitigation: Install and use the skill only when media upload to that external service is acceptable for the user's data handling requirements.

Risk: Video role replacement involving real people can misuse a person's likeness.

Mitigation: Confirm authorization for real-person likeness use and refuse unauthorized face or identity replacement requests.

Risk: Generate actions consume credits and submitted tasks cannot be canceled.

Mitigation: Review the cost estimate or clearly state actual billing behavior, then obtain explicit user approval before submitting a generate task.

Risk: The skill uses or stores an API key for the qhkit/iqinghu service.

Mitigation: Use the qhkit token configuration or QHKIT_TOKEN environment variable deliberately and avoid exposing the token in user-visible output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-role-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu service](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Links]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit task IDs, status JSON, generated video URLs, credit usage, and user-facing error messages.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
