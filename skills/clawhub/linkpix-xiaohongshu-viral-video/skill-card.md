## Description:

LinkPix helps agents prepare and run qhkit workflows for Xiaohongshu product-seeding and promotional short videos, including model selection, media upload, cost confirmation, generation polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, marketers, and agent users use this skill to create Xiaohongshu-style product notes, video notes, and traffic-driving promotional clips through LinkPix/qhkit. It guides setup, model discovery, user confirmation for paid generation, media upload, status polling, and delivery of generated videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and uses npm-based qhkit tooling.

Mitigation: Install only when the agent is expected to use the qhkit/LinkPix service, and review the package and installation environment before deployment.

Risk: The skill requires an API token for the qhkit/LinkPix service.

Mitigation: Configure credentials through the documented qhkit token flow or environment variable, and avoid exposing the token in conversation or logs.

Risk: The skill uploads selected media files and can trigger paid video-generation tasks.

Mitigation: Review selected media and require explicit user approval of model, duration, references, and estimated credits before any generate step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-xiaohongshu-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON payload examples, cost-confirmation steps, polling instructions, and generated video delivery links.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
