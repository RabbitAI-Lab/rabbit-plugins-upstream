## Description:

This skill uses the qhkit CLI package @iqinghu/qhkit to generate realistic, high-quality ecommerce product scene and lifestyle images for home, beauty, apparel, and electronics products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and ecommerce operators use this skill to turn product images into realistic lifestyle scene images for product pages, advertisements, and showcase materials. Agents use it to prepare qhkit image-generation commands, configuration guidance, and delivery guidance for generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may make persistent Node/npm changes and configure qhkit credentials.

Mitigation: Use it only in approved environments, review install commands before execution, and confirm credential handling with the user or operator.

Risk: Product assets selected by the user may be uploaded to the provider for image generation.

Mitigation: Use only assets approved for third-party processing and avoid confidential or restricted product imagery unless that upload is explicitly authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-scene-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with qhkit CLI command examples and user-facing status or delivery text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and actual credit usage returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
