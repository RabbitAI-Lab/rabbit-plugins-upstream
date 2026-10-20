## Description:

Helps POD sellers generate coordinated variations of a print design by changing colors, styles, and design elements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

POD sellers and designers use this skill to create multiple coordinated print-design variations from a reference image for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating qhkit and Node introduces dependency and supply-chain exposure.

Mitigation: Review the dependencies and prefer a vetted or pinned qhkit version where required.

Risk: The workflow uses an account token, uploads the chosen design image to the qhkit service, and can spend account credits.

Mitigation: Confirm the image may be uploaded, protect the token, and check the credit estimate before generation.

Risk: Generated variations may subtly alter important details of the original print.

Mitigation: Review the resulting designs for critical elements before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-pod-pattern-variations)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI workspace](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Image URLs and concise text with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image links and the actual credits charged are provided on completion; results should be checked against the original design.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
