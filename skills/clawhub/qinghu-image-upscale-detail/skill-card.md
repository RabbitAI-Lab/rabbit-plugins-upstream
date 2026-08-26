## Description:

Uses Qinghu AI to upscale and repair a single image with detail enhancement while preserving the original content and style for product, portrait, scenery, print, or restoration workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to upscale, clarify, and restore detail in one image at a time without intentionally changing style or content. It is intended for images such as product photos, portraits, scenery, old photos, and print-preparation assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads the selected image to Qinghu for processing.

Mitigation: Use it only for images the user is comfortable sending to Qinghu, and avoid sensitive or unauthorized material.

Risk: The skill requires installing and using the Qinghu qhkit CLI with a Qinghu API key.

Mitigation: Install qhkit only when the user accepts that dependency, keep API keys scoped to the user's Qinghu account, and use the documented configuration flow.

Risk: Generation consumes Qinghu credits and submitted jobs cannot be treated as free previews.

Mitigation: Run an estimate first, show the expected credit cost and key parameters, and wait for explicit user confirmation before running generate.

Risk: Large local images may be compressed before upload, which can conflict with strict preservation workflows.

Mitigation: Keep inputs under 10MB or tell the agent not to perform lossy JPEG compression when preservation is more important than automatic retry.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-upscale-detail)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a Qinghu API key, one input image, an estimate before submission, explicit user confirmation before credit-spending generation, and status polling to retrieve image URLs.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
