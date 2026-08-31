## Description:

This skill helps an agent generate realistic product mockups by applying a print pattern to apparel, hats, mugs, and other POD merchandise with natural perspective, fabric folds, lighting, and placement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to turn print artwork and product images into POD mockup guidance and qhkit image-generation commands. It is intended for workflows such as showing a design on a T-shirt, hoodie, hat, mug, or other custom product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask the user to provide an API key during qhkit setup.

Mitigation: Configure the QHKIT token through a secure environment variable or secret store, and avoid pasting API keys into chat.

Risk: The skill can modify the local tool environment by installing qhkit and related Node or Python tooling.

Mitigation: Review global npm installs, PATH changes, and shell startup file edits before allowing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-apply)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu LinkPix workspace](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs through qhkit after user-confirmed image generation; requires qhkit and a QHKIT token.]

## Skill Version(s):

0.1.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
