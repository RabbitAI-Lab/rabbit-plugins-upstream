## Description:

Generates commercial e-commerce images from text prompts, with optional reference images for image-to-image generation and editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams use this skill to generate product and campaign images from prompts, optionally using supplied product photos as references.

### Deployment Geography for Use:

China (domestic iqinghu.com service)

## Known Risks and Mitigations:

Risk: Prompts and supplied reference images may be sent to the qhkit/LinkPix service.

Mitigation: Share only approved content and use the service only if its data handling is acceptable.

Risk: Setup may install Node and qhkit or change the local PATH; the CLI needs an API token.

Mitigation: Review installation and token handling, and prefer a reviewed or pinned qhkit version in controlled environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-image-generate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Markdown, Image URLs, Shell commands, Configuration guidance]

**Output Format:** [Markdown with image links and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the credits actually charged for generated images.]

## Skill Version(s):

0.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
