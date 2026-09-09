## Description:

This skill guides an agent to create ecommerce virtual try-on images with Qinghu AI qhkit commands using garment photos and optional model references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and agents use this skill to turn clothing product images into virtual model try-on visuals for product listings and localized variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install or update mutable command-line software.

Mitigation: Prefer an administrator-managed, pinned qhkit installation and review package updates before use.

Risk: Qinghu/qhkit receives the images used for generation.

Mitigation: Use only images that may be shared with Qinghu/qhkit services.

Risk: API tokens may be needed for qhkit configuration.

Mitigation: Provide tokens through a managed secret mechanism where available.

Risk: Tool output may suggest upgrade commands.

Mitigation: Avoid executing upgrade commands copied directly from tool output without review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-model-outfit-swap)
- [AutoAGC Publisher Profile](https://clawhub.ai/user/autoagc)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated image URLs through qhkit when the agent runs the documented commands with user-provided images and credentials.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
