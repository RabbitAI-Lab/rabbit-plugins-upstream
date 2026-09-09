## Description:

LinkPix routes ecommerce image requests to qhkit image generation modes for product hero sets, long detail-page images, and prompt- or reference-based commercial images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and agent operators use this skill to generate ecommerce product image sets, detail-page long images, white-background or marketing images, and reference-based variants through LinkPix/qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload product images to external LinkPix/qhkit services and may consume service credits.

Mitigation: Get user consent before uploads or generation, use qhkit estimate when quoting costs, and disclose actual credits used.

Risk: The skill describes automatic installation or upgrades of @iqinghu/qhkit and Node tooling.

Mitigation: Require explicit user approval before global installs, Node downloads, PATH changes, or @latest upgrades, and use trusted package sources.

Risk: The qhkit service token can grant access to paid generation.

Mitigation: Store tokens only through qhkit config or QHKIT_TOKEN, avoid exposing them in logs or shared prompts, and rotate them if disclosed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-ecom-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with qhkit shell commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and credit usage returned by qhkit.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
