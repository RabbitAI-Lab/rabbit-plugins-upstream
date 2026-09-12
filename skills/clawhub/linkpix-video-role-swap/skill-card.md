## Description:

Uploads an original video and a new character image, then uses LinkPix/qhkit to replace the person in the video while preserving motion and lip movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to perform authorized video role replacement, face/model replacement, and localized creative variants from a source video plus a character image. The skill is intended for media where the user has rights to process the likeness and uploaded assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad install and upgrade authority for qhkit, including upgrades suggested by CLI output.

Mitigation: Install only in a sandbox or controlled environment, pin and review qhkit before use, and require explicit approval before installs or upgrades.

Risk: Video role replacement can misuse a person's likeness or process sensitive uploaded media.

Mitigation: Use only media and likenesses the user is authorized to process, confirm consent for real-person likenesses, and treat uploaded videos/images as sensitive.

Risk: QHKIT_TOKEN and related configuration can expose account access if logged or shared.

Mitigation: Treat QHKIT_TOKEN as a secret, avoid printing it, and store it only in approved secret or environment-variable mechanisms.

Risk: Remote video tasks may consume credits and can run for a long time after submission.

Mitigation: Estimate credits where supported, communicate task IDs and expected timing, and preserve status identifiers for follow-up.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-role-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task identifiers, status JSON, video URLs, credit estimates, and user-facing CLI error messages.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
