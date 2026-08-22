## Description:

LinkPix helps agents create realistic ecommerce product scene and lifestyle images from product references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and developers use this skill to turn product images into scene, atmosphere, and lifestyle visuals for product detail pages and ads while confirming cost before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit, Node, or npm packages on the host.

Mitigation: Prefer an administrator-managed, pinned qhkit installation and review install or upgrade commands before deployment.

Risk: Product images and prompts may be uploaded to the qhkit service, and generation can consume account credits.

Mitigation: Use approved images and tokens only, run cost estimation when supported, and require explicit user confirmation before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-scene-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image generation, option lookup, cost estimation, confirmation, polling, and delivery of generated image URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
