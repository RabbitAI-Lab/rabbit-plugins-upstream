## Description:

Extracts print patterns from product or worn-garment images into high-resolution, flat, reusable pattern assets for POD customization and apparel design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and design operators use this skill to guide an agent through extracting a visible garment or product print into a flat bitmap design asset. It is intended for POD reuse workflows where the user can inspect the generated result before downstream design or production use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected local images to Qinghu/qhkit and requires a qhkit API token.

Mitigation: Use it only where uploading those images is acceptable, protect the API token, and confirm selected files before generation.

Risk: The skill gives agents broad software installation and upgrade authority.

Mitigation: Manually approve qhkit or Node installation and upgrade commands, pin trusted versions where practical, and verify command sources before execution.

Risk: Generated extraction may alter print details or be used with protected brand or IP imagery.

Mitigation: Review output against the source image's key elements and confirm reuse rights before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-pod-pattern-extract)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI workspace](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Image URLs]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and actual qhkit credit usage when generation completes.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
