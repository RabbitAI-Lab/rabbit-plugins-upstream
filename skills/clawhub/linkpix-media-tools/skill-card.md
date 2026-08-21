## Description:

LinkPix routes video cleanup and image editing requests through qhkit workflows for watermark or subtitle removal, upscaling, background changes, object or text edits, compression, and watermarking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare ecommerce media by routing video watermark/subtitle removal, video upscaling, image background work, object/text edits, compression, and watermarking through LinkPix/qhkit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload local media to an external service for processing.

Mitigation: Confirm the user is comfortable sending the selected media to the service before running qhkit processing commands.

Risk: The skill may reuse an existing local qhkit credential file or require a provided token.

Mitigation: Prefer explicit credentials or a reviewed local qhkit configuration, and avoid exposing tokens in chat or logs.

Risk: Automatic setup can install or upgrade Node/qhkit and make persistent host-level changes.

Mitigation: Use a preinstalled, pinned qhkit runtime where possible and review installation commands before execution.

Risk: Some generate actions consume account credits and may not be cancelable after submission.

Mitigation: Run estimates where supported and obtain explicit user confirmation of key parameters and expected credit use before submitting generation tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-media-tools)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, status updates, media URLs, and credit usage from qhkit workflows.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
