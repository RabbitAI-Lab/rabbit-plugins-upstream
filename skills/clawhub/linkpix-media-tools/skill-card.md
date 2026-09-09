## Description:

LinkPix media tools route agent requests for video watermark and subtitle removal, video super-resolution, image background changes, object or text edits, compression, and watermarking through qhkit-backed media workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to optimize ecommerce and marketing media by submitting local files or public URLs for LinkPix/qhkit video and image processing tasks. It is suited for guided media cleanup, enhancement, compression, watermarking, and delivery of processed media URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images and videos may be uploaded to the external LinkPix/qhkit service for processing.

Mitigation: Use the skill only with media you are permitted and comfortable to send to that service, especially when handling private, proprietary, or regulated content.

Risk: The skill includes broad setup and upgrade instructions for an unpinned globally installed qhkit CLI.

Mitigation: Review the package source before installation, prefer pinned package versions in controlled environments, and avoid automatic @latest upgrades unless future behavior changes are acceptable.

Risk: API token configuration is required for qhkit service access.

Mitigation: Prefer a scoped or disposable API token and keep credentials out of prompts, logs, shell history, and committed files.

Risk: Watermark and subtitle removal workflows can be misused on media the user does not own or have rights to modify.

Mitigation: Confirm rights and intended use before processing third-party media, especially for commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-media-tools)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide delivery of processed image or video URLs returned by qhkit after estimation, generation, and polling.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
