## Description:

Helps POD (Print on Demand) sellers generate design assets with LinkPix/qhkit workflows for print extraction, mockup fitting, design variation, and product mockup images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External POD sellers and ecommerce operators use this skill to guide agents through LinkPix/qhkit image-generation workflows for extracting print graphics, creating design variants, fitting designs onto products, and preparing product mockups for listing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkPix/qhkit API keys and may reuse local OpenClaw credentials automatically.

Mitigation: Prefer user-configured credentials through an environment variable or qhkit configuration, and avoid asking the agent to store or expose raw API keys.

Risk: Image generation requests can consume user credits.

Mitigation: Confirm the model, inputs, image count, size or quality, and estimated credits with the user before submitting any generation request.

Risk: Generated or extracted print designs may differ from the source image or raise rights concerns when used commercially.

Mitigation: Ask users to review key visual details after generation and confirm they have rights to use recognizable brands, IP, or third-party artwork.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / iqinghu workspace](https://www.iqinghu.com)
- [iqinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image generation task parameters and generated image URLs through qhkit when the user explicitly approves credit-consuming requests.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
