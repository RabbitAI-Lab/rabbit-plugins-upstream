## Description:

LinkPix helps agents route video watermark or subtitle removal, video super-resolution, image background editing, object cleanup, text editing, watermarking, and compression work through qhkit and related LinkPix tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce sellers, and agent operators use this skill to prepare media assets by cleaning or improving videos and editing, compressing, or watermarking product images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade npm/Node tooling and modify the runtime environment.

Mitigation: Review installation commands first and require explicit user approval before installing packages or changing PATH configuration.

Risk: Media files may be uploaded to the qhkit/LinkPix service for processing.

Mitigation: Confirm that the user is allowed to upload the selected media and avoid sending sensitive or unauthorized assets.

Risk: Generation requests can consume service credits and may require a local service token.

Mitigation: Confirm parameters and expected credit usage before submission, and configure tokens through local secret storage or environment variables rather than chat.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-media-tools)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return processed image or video URLs and task status details from qhkit responses.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
