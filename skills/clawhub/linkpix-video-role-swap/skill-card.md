## Description:

Uploads an original video and one replacement character image, then helps replace the person in the video while preserving motion and lip movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare LinkPix video character replacement jobs for authorized likeness swaps, video face swaps, model replacement, digital human replacement, and localized marketing videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party qhkit CLI and may require an API key.

Mitigation: Install and configure qhkit only in trusted environments, keep API keys private, and use the documented token or environment-variable configuration path.

Risk: Source videos and replacement images may be uploaded to the provider.

Mitigation: Use only media the user is authorized to process and avoid submitting sensitive or restricted content unless the upload destination is acceptable.

Risk: Video generation can consume account credits after submission.

Mitigation: Confirm the key parameters and expected or actual credit charge with the user before starting a generate action.

Risk: Replacing a real person's likeness can be unauthorized or harmful.

Mitigation: Proceed only when the user has authorization for the likeness, and refuse unauthorized replacement of a real person's face or identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-role-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit commands, status-check instructions, setup guidance, and user confirmation prompts before credit-spending generation.]

## Skill Version(s):

0.1.4 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
