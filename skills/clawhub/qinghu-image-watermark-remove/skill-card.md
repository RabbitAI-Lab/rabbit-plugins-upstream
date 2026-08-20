## Description:

Qinghu AI Image Watermark Remove helps an agent remove full-image, local logo, text, and graphic watermarks from authorized images through Qinghu's qhkit workflow, with modes for watermark-only removal or watermark-and-text removal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare owned or authorized image assets by removing watermarks, logos, or text through Qinghu AI. It is suited to one-image-at-a-time editing workflows where the user can confirm cost before submission and review the generated image afterward.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Watermark removal can create copyright or licensing risk when used on images the user does not own or have permission to modify.

Mitigation: Use the skill only for owned or authorized images, and pause when authorization is unclear before submitting the image to the service.

Risk: The workflow sends images to Qinghu's external service and can spend account credits after user confirmation.

Mitigation: Confirm the user is comfortable with the external upload, run an estimate first, and wait for explicit approval before generation.

Risk: The artifact describes global qhkit installation and persistent credential setup, including token paths that may be sensitive.

Mitigation: Prefer a pre-provisioned, least-privilege qhkit installation and token path; avoid unnecessary global installs or root-level credential writes.

Risk: Choosing the watermark-and-text mode may remove desired visible text, and output resolution may differ from the source image.

Mitigation: Confirm the intended removal mode and warn about possible size changes before processing images with strict layout or resolution requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-watermark-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs, status messages, log IDs, and final credit usage reported by qhkit.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
