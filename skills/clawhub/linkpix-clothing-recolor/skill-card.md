## Description:

Generates alternate clothing colorway images with LinkPix qhkit while preserving garment shape, material texture, and lighting for ecommerce SKU color cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and developers use this skill to create additional clothing color variants and SKU color-card images from an existing product image through qhkit image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images may be uploaded to the Qinghu/LinkPix service for recoloring.

Mitigation: Use only images approved for that external service and confirm user consent before invoking qhkit generation.

Risk: The skill can consume qhkit API credits when generating images.

Mitigation: Run qhkit estimate before generation when cost matters and report insufficient balance before submitting generation jobs.

Risk: Automatic setup can involve global npm installation, Node download, PATH changes, or token configuration.

Mitigation: Prefer pre-installed qhkit and require explicit approval before installation, runtime download, PATH mutation, or credential changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-clothing-recolor)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown with inline qhkit shell commands and generated image URLs from the CLI response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report qhkit credit estimates or actual credit consumption when the CLI returns those values.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
