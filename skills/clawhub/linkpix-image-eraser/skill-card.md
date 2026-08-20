## Description:

Uses the qhkit CLI and LinkPix image service to erase specified people, watermarks, text, or unwanted objects from product images and refill the background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare cleaner ecommerce product images by directing qhkit to remove visible elements such as watermarks, text, people, or miscellaneous clutter. It is most relevant when an agent needs to generate shell commands and configuration guidance for LinkPix-powered image inpainting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload user images to qhkit/LinkPix and consume API credits.

Mitigation: Use it only with approval for the target images and confirm credit estimates before generation when cost matters.

Risk: The skill can ask the agent to run npm, Node, PATH, or qhkit upgrade and configuration commands.

Mitigation: Require explicit approval before installation, upgrade, PATH, or token configuration steps, and prefer a preinstalled qhkit with an explicitly provided token.

Risk: The skill describes automatic reuse of root-level qhkit credentials when present.

Mitigation: Prefer explicit user-provided credentials and review any credential reuse before running qhkit commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-eraser)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit commands, installation or upgrade steps, token configuration guidance, credit estimates, and generated image URLs returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
