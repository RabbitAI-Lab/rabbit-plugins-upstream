## Description:

Generates commercial ecommerce images from text prompts, with optional reference images for image-to-image generation or edits, using the LinkPix qhkit image workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate ecommerce product, scene, concept, and prompt-polished images through LinkPix. It guides model selection, estimation, API-key setup, user confirmation, generation, polling, and delivery of generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkPix/QHKIT API keys could be exposed if pasted into chat or stored through command-line token arguments.

Mitigation: Have users configure credentials locally where possible, prefer environment variables such as QHKIT_TOKEN, avoid asking users to paste secrets into chat, and confirm any token-setting command before execution.

Risk: The workflow may install qhkit, Node tooling, or helper packages before generating images.

Mitigation: Review requested installs, use trusted package sources, and get user approval before allowing package or runtime installation.

Risk: Image generation can upload user-provided images and consume LinkPix credits.

Mitigation: Confirm the selected model, reference images, size, quality, image count, and estimated credits with the user before running a generate action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-generate)
- [QHKIT npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation actions can return image URLs and credit usage; paid or credit-consuming submissions require explicit user confirmation.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
