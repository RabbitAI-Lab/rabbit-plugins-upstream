## Description:

Guides agents in generating e-commerce product images from prompts and optional reference images through Qinghu AI's qhkit image workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, product photographers, and brand teams use this skill to prepare product listing images and promotional visuals from text or reference photos for online marketplaces and storefronts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic setup or upgrades may run unpinned npm packages and change the local Node environment.

Mitigation: Request approval before installing or upgrading packages, and prefer pinned versions.

Risk: Configuring qhkit may persist a service token on the device.

Mitigation: Ask before storing credentials, keep tokens out of chat and logs, and use a protected environment variable when appropriate.

Risk: Reference photos may be uploaded to iqinghu.com and image generation may consume paid credits.

Mitigation: Confirm which images will be uploaded and obtain explicit approval for the parameters and estimated credits before submitting a generation task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-gpt-image-2)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown with command examples and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports estimated credits before approved generation and actual credits with delivered image links.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
