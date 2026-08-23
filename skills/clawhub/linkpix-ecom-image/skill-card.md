## Description:

LinkPix helps agents generate ecommerce product images, carousel sets, long-form detail pages, and commercial marketing images through the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and agent users use this skill to route product-image requests into qhkit modes for main images, carousel image sets, detail-page images, and prompt-based commercial visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A long-lived API key could be exposed if pasted into chat or stored by the agent.

Mitigation: Set QHKIT_TOKEN or run qhkit config locally instead of sharing the secret in chat.

Risk: Product images and prompts are sent to the qhkit service for generation.

Mitigation: Use only product assets approved for third-party processing and avoid sensitive unreleased materials unless policy permits it.

Risk: The skill depends on installing and running a third-party npm CLI.

Mitigation: Review the qhkit package and install it in a controlled environment before using the skill for production work.

Risk: Generation commands can create tasks that consume credits.

Mitigation: Run estimate first and require explicit user confirmation for model, image count, references, quality, and expected credits before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu service](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with qhkit shell commands, JSON arguments, configuration steps, and generated image URLs when tasks complete.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include credit estimates, confirmation prompts before billable generation, and qhkit JSON error messages.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
