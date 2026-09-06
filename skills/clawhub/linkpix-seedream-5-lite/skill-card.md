## Description:

Helps e-commerce operators, designers, and store managers generate Chinese-language product images, posters, and promotional graphics with LinkPix/qhkit using Seedream 5.0 Lite or related Qwen-Image model options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, visual designers, and store managers use this skill to prepare prompts, estimate credits, and generate product images or promotional graphics through qhkit. It is intended for workflows such as product hero images, promotional posters, sale badges, and Chinese text-heavy e-commerce layouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external Qinghu/qhkit image service and may upload prompts or reference images.

Mitigation: Review prompts and source images for sensitive content before use, and use an approved API token and account for the target workflow.

Risk: Image generation can consume paid credits once submitted.

Mitigation: Run an estimate first and require explicit user confirmation of model, image count, quality, size, reference images, and expected credits before generating.

Risk: The artifact instructs agents to install or upgrade Node, npm, qhkit, and related tooling automatically.

Mitigation: Prefer a pre-provisioned qhkit installation, or require explicit approval before changing the user environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedream-5-lite)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit command examples and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit image-generation commands that upload prompts or reference images to an external Qinghu service and may consume paid credits after user confirmation.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
