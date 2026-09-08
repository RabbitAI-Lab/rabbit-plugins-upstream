## Description:

Seedream 5.0 Pro 爆款电商图 | LinkPix helps ecommerce teams generate product images, hero images, posters, and marketplace creatives from text prompts or reference images through the qhkit image workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce designers, product photographers, brand visual teams, and commerce operators use this skill to prepare Seedream 5.0 Pro image-generation prompts, check current model options and credit estimates, and run qhkit image generation for marketplace assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request an API key through chat-based setup steps.

Mitigation: Use a local secrets mechanism such as QHKIT_TOKEN and avoid pasting API keys into chat.

Risk: The workflow can install or upgrade a persistent global CLI package.

Mitigation: Review npm global installs or upgrades for @iqinghu/qhkit before running them, and install only when the qhkit/LinkPix provider is trusted.

Risk: Image generation creates tasks that consume credits.

Mitigation: Run estimate first and confirm expected credit usage before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedream-5-pro)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides qhkit image option lookup, credit estimation, prompt polishing, image generation, and delivery of generated image URLs.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
