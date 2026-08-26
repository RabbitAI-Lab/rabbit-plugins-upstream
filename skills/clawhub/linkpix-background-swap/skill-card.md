## Description:

Helps agents replace ecommerce product-image backgrounds with LinkPix/qhkit while keeping the product subject prominent and generating marketing scene variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce users and operators use this skill to turn product photos, including white-background images, into scene-based marketing images. Developers and agents use it to install or configure qhkit, choose current LinkPix image options, estimate credit use, request confirmation, and deliver generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user-provided images to the LinkPix/qhkit service.

Mitigation: Confirm the user intends to use the external service before generation and avoid uploading images the user has not provided for this task.

Risk: Image generation consumes service credits.

Mitigation: Run an estimate when supported, disclose the expected credit cost, and wait for explicit user confirmation before submitting a generate command.

Risk: Generative background replacement can alter product details such as text, logos, or structure.

Mitigation: Ask the user to review generated images for critical product details before using them in commerce or marketing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-background-swap)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix/qhkit API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API Key Setup Guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide qhkit installation, token configuration, image option lookup, credit estimation, user confirmation, image upload, and generated image URL delivery.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
