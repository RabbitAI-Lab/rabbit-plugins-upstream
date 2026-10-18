## Description:

Helps Douyin Shop merchants and content teams create product image sets, detail images, covers, and promotional visuals through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Douyin Shop merchants, livestream teams, and content creators use this skill to turn product photos into storefront image sets, detail-page graphics, and campaign visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and an API key are supplied to the third-party Qinghu AI service.

Mitigation: Use only approved product assets, protect the API key, and review the service before uploading images.

Risk: Image-generation requests spend credits and cannot be canceled after submission.

Mitigation: Show the selected parameters and estimated credits, then obtain explicit user approval before generating.

Risk: Domestic-site setup could overwrite an existing international AutoAGC configuration.

Mitigation: Check the configured site and preserve international settings when the user has an international account.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-douyin-shop-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Images, Text, Guidance]

**Output Format:** [Markdown with generated image URLs and credit-use details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation requires a product image or copy and explicit approval before spending credits.]

## Skill Version(s):

0.1.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
