## Description:

Batch processes ecommerce product photos into clean white-background product images by guiding an agent to use LinkPix/qhkit image-batch workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketplace operators, and agent users use this skill to convert one or more product photos into white-background listing images, estimate credit cost, submit generation jobs, and return generated image links. The skill is intended for normal ClawHub use and requires review before spending credits or handling API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit and related runtime tooling on the host machine.

Mitigation: Review installation commands before running them and prefer an environment where qhkit is already installed or can be installed with expected permissions.

Risk: Product images are sent to qhkit/LinkPix for processing.

Mitigation: Use the skill only for images that are appropriate to share with the external processing service.

Risk: The workflow can require persistent API credentials.

Mitigation: Use a safer secret-management path such as environment variables or existing config instead of pasting API keys into chat.

Risk: Generate commands can spend account credits.

Mitigation: Run the matching estimate command first and obtain explicit user confirmation before submitting any generate command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-white-background)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The qhkit commands return one-line JSON and generated image URLs; generate actions can consume account credits and should be confirmed after estimate.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
