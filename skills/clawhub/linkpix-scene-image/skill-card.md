## Description:

根据商品自动生成真实、高质感的商品场景图，适用于家居、美妆、服饰、数码等行业。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to generate lifestyle and product scene images from product photos for detail pages, ads, and category-specific merchandising.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to install or upgrade Node/npm tooling and run qhkit from npm or npx.

Mitigation: Review installation steps before use, prefer a preinstalled qhkit binary where available, and confirm package installation is allowed in the target environment.

Risk: Product images are uploaded to the provider for generation.

Mitigation: Use only images approved for provider processing and avoid submitting confidential, regulated, or rights-restricted product assets without authorization.

Risk: The workflow may require a qhkit API key and generate actions can consume credits.

Mitigation: Use platform-managed secrets when available, avoid exposing raw API keys in chat, and confirm estimated credits before any generate action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-scene-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent through qhkit image generation, setup, cost confirmation, and delivery of generated image URLs.]

## Skill Version(s):

0.1.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
