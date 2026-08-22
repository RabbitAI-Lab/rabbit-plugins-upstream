## Description:

Uploads a source video and one replacement character image, then uses LinkPix/qhkit to replace the person in the video while preserving motion and lip movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to localize marketing, model, or digital-human videos by replacing a person in a video with an authorized character image through LinkPix/qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload referenced video and image media to a cloud video/person replacement service.

Mitigation: Use it only with media the user is allowed to process, and confirm that uploads to LinkPix/qhkit are acceptable for the environment.

Risk: Video role swap and face/person replacement can misuse a real person's likeness.

Mitigation: Require confirmation that the user has permission for any real person's likeness and refuse unauthorized impersonation or face replacement requests.

Risk: The skill asks agents to auto-install Node/qhkit tooling and may reuse a local OpenClaw credential file.

Mitigation: Prefer platform-managed installation and secrets, and do not allow auto-installation or local credential reuse unless that is intentional for the deployment.

Risk: Submitting a generate task can consume account credits and cannot be cancelled after submission.

Mitigation: Before generate calls, present the key parameters and estimated or actual-credit caveat, then wait for explicit user approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-video-role-swap)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit CLI calls whose stdout is one-line JSON; generated tasks can consume account credits and return video URLs after polling.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
