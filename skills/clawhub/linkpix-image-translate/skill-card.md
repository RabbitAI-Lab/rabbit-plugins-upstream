## Description:

This skill helps agents use the qhkit/LinkPix workflow to batch translate text in ecommerce product images while preserving the original layout and design style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, localization operators, and agents use this skill to create target-language versions of ecommerce product images with the qhkit CLI and LinkPix service. It is suited to main-image and detail-image translation workflows where generated output is manually reviewed before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected product images to the qhkit/LinkPix service.

Mitigation: Use it only for images that are appropriate to send to that external service and confirm account/token handling before running commands.

Risk: Generated translations, numbers, logos, or product details can be inaccurate because the skill uses generative image rewriting.

Mitigation: Manually review generated images before delivery, especially translated text, prices, specifications, brand names, and product structure.

Risk: Image generation may consume account credits.

Mitigation: Run the documented estimate command before generation when cost matters and warn users if the service reports insufficient balance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit command guidance and delivery instructions; generated image URLs and credit usage come from the external CLI response.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
