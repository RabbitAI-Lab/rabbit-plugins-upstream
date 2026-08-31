## Description:

Helps ecommerce, short-video, and brand content teams use Qinghu/qhkit to generate Kling 3.0 product marketing videos with product images, prompts, model-option checks, task polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, short-video teams, and brand content teams use this skill to prepare product-video generation requests, estimate credits, submit Qinghu/qhkit Kling 3.0 tasks, poll status, and deliver generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask users to provide an API key in chat.

Mitigation: Use a safer local secret mechanism such as a local qhkit token configuration or environment variable instead of pasting credentials into chat.

Risk: Setup can modify the local environment by installing Node.js packages or related tooling.

Mitigation: Review installation commands before running them and install only in an intended environment with appropriate permissions.

Risk: Video generation tasks can consume credits and cannot be canceled after submission.

Mitigation: Confirm key generation parameters and estimated credits with the user before submitting any task.

Risk: Media inputs may be uploaded to the Qinghu/qhkit service.

Mitigation: Use only media that is approved for upload to the service and avoid sending sensitive or restricted assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-kling-3-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated video task IDs, status summaries, credit estimates, and final video URLs returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
