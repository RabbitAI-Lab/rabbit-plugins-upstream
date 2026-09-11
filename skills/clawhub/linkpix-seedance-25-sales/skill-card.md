## Description:

Helps brand teams, e-commerce designers, and performance marketers use Qinghu AI through qhkit to generate Seedance 2.5 product sales videos from product media, selling points, and current model options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, e-commerce, design, and advertising teams use this skill to create short product promotion, product-detail, and social commerce videos with Seedance 2.5 through the qhkit CLI. It helps agents check available video models, estimate paid generation cost, submit approved jobs, poll status, and return generated video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request Qinghu API credentials during setup.

Mitigation: Do not paste API keys into chat; configure credentials through a protected local secret mechanism or environment variable where available.

Risk: The skill can install or upgrade unpinned qhkit and Node-related tooling.

Mitigation: Preinstall reviewed tool versions in an isolated environment before using the skill.

Risk: Product images, videos, audio, and prompts may be uploaded to the qhkit/Qinghu service.

Mitigation: Use the skill only when the user trusts that service and is comfortable uploading the selected product media.

Risk: Video generation can consume paid credits and submitted tasks may not be cancellable.

Mitigation: Check estimates and submitted parameters first, then run paid generation only after explicit user approval.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-seedance-25-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include current model-option checks, credit estimates, submitted task IDs, polling guidance, and generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
