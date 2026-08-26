## Description:

Generates video storyboard plans with shot scripts, camera movement guidance, copy, and storyboard images through the LinkPix qhkit workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and production teams use this skill to turn product or campaign inputs into a storyboard script and generated storyboard frames. It supports workflows where the user asks for storyboard planning, shot scripts, camera directions, or storyboard images rather than a finished video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may ask for an API key in chat.

Mitigation: Use a protected secret store or the QHKIT_TOKEN environment variable instead of pasting the API key into chat.

Risk: The skill can install Node/npm packages or modify PATH while preparing qhkit.

Mitigation: Run setup only in an environment where developer tooling installation and PATH changes are acceptable, and review installation commands before execution.

Risk: Storyboard script and image generation can consume credits and upload user-provided images.

Mitigation: Confirm credit estimates, selected parameters, and uploaded images with the user before submitting credit-consuming generation tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-storyboard)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Images]

**Output Format:** [Markdown response with storyboard script text, qhkit command guidance, JSON status details, and generated storyboard images or image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require polling for generation status and user confirmation before credit-consuming tasks.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
