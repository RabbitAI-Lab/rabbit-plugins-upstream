## Description:

LinkPix helps agents generate commercial ecommerce images from text prompts or optional reference images using the qhkit image CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce creators, and agents use this skill to create product or scene images from a prompt, optionally using local or URL reference images. Agents use it to select a LinkPix model, estimate credits, request explicit confirmation for paid generation, run qhkit image commands, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may change the host environment by installing or upgrading qhkit or Node tooling.

Mitigation: Use a managed or sandboxed environment with qhkit preinstalled, or require explicit user approval before npm installs, Node bootstrap steps, or upgrades.

Risk: The skill may use credentials, upload local reference images, and submit paid image-generation tasks.

Mitigation: Require explicit user approval before credential use, local image upload, or any paid generate call; run estimate first when supported.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-generate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON CLI arguments; generated image URLs are returned by qhkit.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, Node/npm, and an API token; paid generate calls require an estimate and explicit user approval before submission.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
