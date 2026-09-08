## Description:

Generates ecommerce image-and-text marketing assets, including ad images, promotional posters, and marketing copy derived from product videos through the LinkPix qhkit workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce operators, and developers use this skill to have an agent generate advertising visuals, promotional images, and product-marketing text posts from image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade mutable external software with broad local authority.

Mitigation: Use a reviewed, pinned qhkit package version in an isolated environment and supervise all install or upgrade commands.

Risk: The workflow requires a QHKIT token and can upload local media to an external service.

Mitigation: Use only trusted tokens and approved media, avoid sensitive assets, and confirm service terms before uploading content.

Risk: Generated advertising images can contain incorrect or malformed visible text.

Mitigation: Review generated assets before publishing and visually verify any text embedded in images.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with qhkit command examples, generated copy, media URLs, task status, and credit usage when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs, generated text, task IDs, CLI status messages, and billed credits from qhkit responses.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
