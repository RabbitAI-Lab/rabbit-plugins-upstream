## Description:

Guides an agent to use LinkPix via the qhkit CLI to improve video resolution and clarity, reduce blur, noise, and compression artifacts, and request output up to 4K/60fps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to prepare qhkit video super-resolution commands, configure authentication, estimate credits where supported, poll status, and deliver the completed enhanced-video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update mutable third-party qhkit tooling.

Mitigation: Confirm the npm package source and version before installation, and avoid unnecessary @latest upgrades unless an explicit version-gate or compatibility issue requires updating.

Risk: Selected local videos may be uploaded to the LinkPix service using an API token.

Mitigation: Confirm the user intends to upload the selected files, protect the qhkit API token, and avoid sending unnecessary or sensitive videos.

Risk: Video enhancement jobs may spend credits and can take a long time to complete.

Mitigation: Run an estimate when supported, confirm the target resolution and frame rate before submission, preserve the returned task ID, and poll at the documented interval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-video-upscale)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits video upscaling jobs through qhkit, then reports task status, media URLs, and credit information when available.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
