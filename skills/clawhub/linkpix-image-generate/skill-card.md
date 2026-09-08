## Description:

Generates commercial e-commerce and product images from text prompts, with optional reference images, through LinkPix using the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create product, scene, concept, and reference-guided e-commerce images through LinkPix. It helps agents choose models, estimate credits, pass local reference images, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit can execute mutable global npm packages or CLI-provided upgrade commands with the agent user's privileges.

Mitigation: Prefer a pinned, reviewed qhkit version and independently verify upgrade commands before execution.

Risk: Prompts and selected local image files may be uploaded to LinkPix during generation.

Mitigation: Confirm user intent before uploading sensitive images or prompt content, and avoid sending confidential material unless approved.

Risk: The security verdict is suspicious due to mutable installation and upgrade behavior.

Mitigation: Review the skill and security evidence before installing, and scan releases before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-generate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to call qhkit, report credit estimates, and return generated image URLs from the CLI response.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
