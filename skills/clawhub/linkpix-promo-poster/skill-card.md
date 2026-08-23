## Description:

Generates ecommerce promotion posters and discount marketing images for campaigns such as Double 11, Black Friday, Christmas, new product launches, and brand promotions using LinkPix/qhkit image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, ecommerce operators, and agent developers use this skill to prepare campaign poster prompts, configure qhkit image generation, and deliver generated marketing images from product references or text-only campaign briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to install or update Node/npm tooling globally.

Mitigation: Prefer a preinstalled qhkit binary or review any installation or upgrade command before allowing it to run.

Risk: The skill uses LinkPix/qhkit with referenced product images and account credits for generation.

Mitigation: Use only approved product images, confirm generation parameters before submission, and prefer platform-managed secrets for API tokens.

Risk: Generated poster text, numbers, logos, or product details may be inaccurate.

Mitigation: Review generated images before publication and regenerate or edit outputs when campaign copy or product details are wrong.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-promo-poster)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs, qhkit status messages, and credit usage after user-confirmed generation.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
