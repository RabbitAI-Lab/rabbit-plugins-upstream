## Description:

This skill helps ecommerce teams use LinkPix/qhkit with GPT Image 2 to generate or refine product listing images, ad creatives, hero images, and social commerce visuals from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, product photography teams, brand teams, and social commerce teams use this skill to create marketplace product images, listing assets, ad key visuals, posters, and refined product images. The skill guides agents through qhkit model selection, prompt polishing, cost estimation, generation, and delivery workflows for LinkPix image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to qhkit/LinkPix during generation.

Mitigation: Use the skill only when sharing those inputs with qhkit/LinkPix is acceptable, and avoid submitting sensitive product, customer, or unreleased campaign material unless approved.

Risk: The skill includes chat-based API key handoff guidance.

Mitigation: Do not paste API keys into chat; configure the token through a secure local secret mechanism and rotate any key that was shared.

Risk: The skill installs unpinned global npm or npx tools.

Mitigation: Prefer pinned, isolated installs and review the package before execution, especially in shared or production environments.

Risk: Image generation can consume credits.

Mitigation: Run the estimate step and confirm model, inputs, image count, quality, and expected credits with the user before submitting a generation request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-gpt-image-2)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit image-generation requests, cost estimates, progress/status handling, and generated image URLs after user confirmation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
