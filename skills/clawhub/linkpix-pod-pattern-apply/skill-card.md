## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）自动将印花图案精准贴合到服装、帽子、杯子等商品上，随布料褶皱与透视自然变形，快速生成真实展示效果图（mockup）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, POD operators, and ecommerce content creators use this skill to apply a print pattern to product images such as shirts, hoodies, hats, and mugs for realistic mockup generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can modify the host environment through global npm installation or Node installation.

Mitigation: Use a controlled execution environment and prefer preinstalling trusted qhkit and Node dependencies before enabling the skill.

Risk: The workflow can reuse existing qhkit or OpenClaw credentials and upload user-provided images to the provider.

Mitigation: Confirm which credentials will be used and only run the skill when provider image upload is acceptable for the input content.

Risk: Image generation consumes service credits and may produce mockups with altered print details.

Mitigation: Estimate credits before generation when cost matters and review generated images for logo, color, text, and layout fidelity before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-apply)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu Workbench](https://www.iqinghu.com)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage from qhkit image generation commands.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
