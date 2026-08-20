## Description:

Uses the qhkit CLI to generate ecommerce product main-image and carousel image sets from a product photo and optional marketing copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and creative teams use this skill to turn a product image and optional sales copy into platform-specific main images and carousel sets for storefront listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may install or upgrade qhkit globally and may install Node when missing, changing the host environment.

Mitigation: Review installation steps before execution and prefer a controlled, preinstalled qhkit package or npx fallback where appropriate.

Risk: Generating images can upload product images to the provider service and use qhkit credentials.

Mitigation: Run only where provider API calls, product-image uploads, and qhkit token use are approved for the data being processed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-main-image-set)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image option, estimate, and generate calls; generated image URLs and credit usage are returned by the CLI.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
