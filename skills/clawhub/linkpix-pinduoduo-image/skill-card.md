## Description:

LinkPix helps Pinduoduo sellers and ecommerce operators generate product images, carousel sets, detail-page images, and promotional campaign graphics through qhkit and Qinghu AI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, operators, and designers use this skill to prepare Pinduoduo-ready product images, main-image sets, detail-page images, and promotional graphics. The skill guides an agent through qhkit options, estimates, generation parameters, credential setup, and result delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on mutable third-party qhkit tooling and external image uploads.

Mitigation: Review the skill before installing, trust the qhkit provider before use, prefer pinned or preinstalled dependencies, and upload only approved product images.

Risk: The artifact includes a workflow that asks the agent to collect an API key in chat.

Mitigation: Configure credentials through protected local or platform secret mechanisms and do not paste API keys into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pinduoduo-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit-based image generation workflows and may produce downloadable image URLs after task execution.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
