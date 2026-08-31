## Description:

Helps agents use LinkPix/qhkit to generate and refine e-commerce product images with GPT Image 2, including text-to-image and reference-image workflows for marketplace listings, ads, and hero images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, product photographers, brand teams, and agent users use this skill to create product listing images, ad visuals, social commerce graphics, and hero images. The skill guides agents through model selection, prompt polishing, reference-image upload, estimate checks, generation, and delivery through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to the LinkPix/qhkit third-party service.

Mitigation: Use the skill only for content that may be shared with that service and review data-handling expectations before generation.

Risk: The skill asks for an API key in chat.

Mitigation: Provide credentials through a secure secret mechanism or environment variable instead of pasting secrets into chat.

Risk: The skill includes broad runtime installation and upgrade steps for Node, npm packages, Pillow, or sharp-cli.

Mitigation: Review and explicitly approve environment changes before allowing installs or upgrades.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-gpt-image-2)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage from qhkit command output.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
