## Description:

Generates e-commerce marketing assets, including advertising images, promotional graphics, and shoppable text content derived from sales videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce operators, and marketing teams use this skill to generate image ad assets and text-based shopping-note content for e-commerce promotion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may expose a qhkit API key if the user pastes credentials into chat.

Mitigation: Configure the API key locally with QHKIT_TOKEN or a trusted secret store, and avoid sharing secrets in chat.

Risk: The skill can trigger paid generation requests, media uploads, and global package installs.

Mitigation: Confirm each paid generation request, media upload, and package installation before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-ad-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, image assets]

**Output Format:** [Markdown guidance with inline shell commands, JSON CLI parameters, generated media URLs, and generated marketing text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require qhkit configuration, API credentials, media uploads, paid generation confirmation, and visual review of generated image text.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
