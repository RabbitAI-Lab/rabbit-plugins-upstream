## Description:

Generates ecommerce promotion posters and campaign images for product launches, discounts, seasonal sales, and brand marketing using the Qinghu AI qhkit image workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to prepare qhkit prompts, options checks, estimates, and generation commands for promotional posters with or without product reference images. The skill also guides installation, token setup, polling, delivery, and failure handling for the Qinghu image generation CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade a third-party npm CLI globally without pinning the package version.

Mitigation: Review the package before installation and prefer a pinned or local qhkit install when operating in controlled environments.

Risk: The skill handles an API token and includes a token-setting command that can expose secrets through command history or chat logs.

Mitigation: Prefer environment-based secret handling, avoid pasting tokens into shared transcripts, and rotate any token that may have been exposed.

Risk: Product images and poster prompts are sent to the Qinghu/qhkit service for generation.

Mitigation: Only submit images, logos, campaign text, and product details that are approved for use with that third-party service.

Risk: Generated poster text, prices, logos, and product details can be inaccurate or changed by the image model.

Mitigation: Review generated images before publication and regenerate or edit when campaign copy, discounts, brand marks, or product structure are wrong.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-promo-poster)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit CLI commands, JSON command parameters, and generated image URLs from the CLI response.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs, estimated or actual credit usage, and user-facing qhkit error messages.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
