## Description:

Helps POD sellers and ecommerce creators use LinkPix/qhkit image generation workflows to extract print designs, create design variants, and fit prints onto product mockups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

POD sellers, ecommerce creators, and supporting agents use this skill to generate product design assets, including print extraction, print variation, product mockups, and listing-ready visual concepts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to install or upgrade a mutable global npm CLI.

Mitigation: Review install and upgrade commands before execution, avoid automatic upgrades, and prefer a pinned local qhkit installation.

Risk: The workflow uses an API token and sends image files to the LinkPix/qhkit service.

Mitigation: Use only trusted tokens and submit only image files that are appropriate to send to the service.

Risk: Generated print extraction or variation may involve copyrighted or branded artwork.

Mitigation: Confirm rights to referenced artwork before commercial use and manually review generated designs before listing products.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / iqinghu workspace](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and qhkit credit usage when image generation commands complete.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
