## Description:

Generates multi-pose and multi-angle clothing model image sets from a single model photo for ecommerce detail pages and social media marketing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and agent users use this skill to turn one clothing model image into a set of pose and angle variants for product pages and social media assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The qhkit workflow sends provided model images to an external Qinghu service and may consume account credits.

Mitigation: Use the skill only when the user is comfortable with external processing, has rights to the images, and understands any credit estimate before generation.

Risk: The skill asks agents to install or upgrade external CLI software during use.

Mitigation: Prefer a platform- or administrator-managed qhkit installation pinned to an approved version, and review upgrades before retrying failed commands.

Risk: API tokens may be exposed if pasted into chat or shell history.

Mitigation: Provide qhkit credentials through a secret mechanism or environment variable rather than embedding tokens in shared command text.

Risk: Generated redraws can alter clothing details, logos, text, or product structure.

Mitigation: Inspect generated outputs for brand, text, and garment accuracy before publishing or sending them to customers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-pose-set)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Node.js distribution checksums](https://nodejs.org/dist/v22.22.3/SHASUMS256.txt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and qhkit JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image generation, estimation, setup, and delivery of generated image URLs.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
