## Description:

Helps Wildberries and Russian cross-border ecommerce teams use LinkPix/qhkit to generate product main images, carousel sets, detail images, campaign posters, white-background images, street-style outfit images, material detail images, and Russian-language image layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, cross-border ecommerce operators, and agent users use this skill to prepare Wildberries-ready product visuals and marketing images through qhkit. It guides model-option lookup, cost estimation, user confirmation before paid generation, image upload handling, and delivery of generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install mutable qhkit package versions, including @latest upgrades.

Mitigation: Review and pin package versions before installation or run the skill in an isolated project or container.

Risk: Product images and a qhkit API token may be handled by the qhkit workflow.

Mitigation: Use only approved product assets, protect the API token, and configure it through the intended qhkit configuration or environment variable path.

Risk: Image compression command examples can be unsafe when file paths are not quoted or are assembled dynamically.

Mitigation: Use safely quoted paths or a fixed reviewed script for image compression before retrying uploads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-wildberries-image)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing workflow guidance; qhkit commands return single-line JSON and generated image URLs when generation succeeds.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
