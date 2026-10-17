## Description:

Helps agents create e-commerce promotional posters and discount graphics for campaigns, product launches, and brand marketing with LinkPix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and marketers use the skill to create promotional posters for seasonal campaigns, product launches, discounts, and brand advertising, with or without a product image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and updating the external qhkit npm CLI introduces a software supply-chain dependency.

Mitigation: Review the package provenance and use a controlled environment or pinned package version when required.

Risk: Product images and prompts are sent to the LinkPix service using a configured token.

Mitigation: Get permission before uploading sensitive assets, and protect the token as a secret.

Risk: Image generation may consume service credits and produce incorrect promotion text or product details.

Mitigation: Check the credit estimate before generation and review text, numbers, logos, and product details before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-promo-poster)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Image links]

**Output Format:** [Markdown guidance and links to generated poster images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated poster copy, numbers, logos, and product details require review before publication.]

## Skill Version(s):

0.1.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
