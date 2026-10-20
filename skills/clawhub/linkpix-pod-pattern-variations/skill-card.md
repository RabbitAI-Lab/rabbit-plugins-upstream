## Description:

Helps POD sellers generate coordinated print-pattern variants from a reference image by changing colors, motifs, and layout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

POD sellers and designers use this skill to produce several coordinated variations of an existing print for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update qhkit and change local Node or qhkit settings without enough user control.

Mitigation: Require approval before installation or configuration changes, and pin the qhkit version when possible.

Risk: Switching between domestic and international account settings can overwrite a working configuration.

Mitigation: Confirm which account and site the user uses before changing qhkit credentials or settings.

Risk: Generated variants may alter important details of the original design.

Mitigation: Review key visual elements in each image before publishing or printing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-variations)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Text with image links and generation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated patterns should be reviewed for changes to important details; image generation may consume credits.]

## Skill Version(s):

0.1.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
