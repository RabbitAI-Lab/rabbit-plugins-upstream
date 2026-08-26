## Description:

Generates realistic ecommerce product scene images from product photos and scene instructions through the LinkPix qhkit image workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and content teams use this skill to turn product photos into lifestyle, atmosphere, and use-case scene images for product listings, ads, and detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a qhkit/LinkPix API key for configuration.

Mitigation: Use only an intended LinkPix API key, prefer environment or qhkit configuration mechanisms, and avoid exposing the token in shared transcripts or files.

Risk: Product images are uploaded to the qhkit/LinkPix service during generation.

Mitigation: Use only images approved for that service and confirm that any customer, brand, or product data can be shared with LinkPix before upload.

Risk: Image generation jobs may consume paid credits.

Mitigation: Estimate credits when supported, summarize model, image count, size, reference images, and expected cost, and get explicit user confirmation before running generation.

Risk: The skill may install or upgrade qhkit and, when needed, Node.js.

Mitigation: Prefer official npm and Node.js sources, use the documented checksum validation for manual Node installs, and report installation or network failures instead of bypassing verification.

Risk: Generated product scene images can alter small product details, text, logos, or structure.

Mitigation: Ask users to review generated images for product accuracy before using them in listings, ads, or customer-facing materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-scene-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / iqinghu service](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON responses, generated image URLs, and credit usage after an approved generation job.]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
