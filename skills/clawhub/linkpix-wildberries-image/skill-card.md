## Description:

Helps Wildberries sellers create Russian-language product image sets, detail images, and promotional graphics from product photos using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Wildberries sellers and cross-border commerce teams use this skill to turn product photos into marketplace main-image sets, detail-page visuals, and Russian-language promotional images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external qhkit tool and its dependencies introduces third-party software into the environment.

Mitigation: Review the package and install it in a sandboxed environment before use.

Risk: Product photos are uploaded to Qinghu AI, and an API token may be stored locally.

Mitigation: Upload only approved images, protect the token in local configuration or environment variables, and rotate or remove it when no longer needed.

Risk: Generating images consumes credits and may create an irreversible paid task.

Mitigation: Check the estimate and confirm the selected inputs and expected cost with the user before submitting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-wildberries-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image links]

**Output Format:** [Markdown with image URLs and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports generated image URLs and actual credits consumed; image generation requires prior user approval.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
