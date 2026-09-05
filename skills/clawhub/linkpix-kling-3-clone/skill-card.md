## Description:

Helps short-video operators, editors, and ecommerce sellers use Qinghu qhkit to analyze viral video structure and generate Kling 3.0-style remake videos with revised product messaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce sellers, and agent users use this skill to transform a social video link into an analyzed script, revise the structure for their own product, and submit a confirmed video generation task through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may request a qhkit API token during setup.

Mitigation: Use a secure secret mechanism or environment variable for the token instead of pasting it into chat.

Risk: The skill can install qhkit or Node tooling globally.

Mitigation: Review global npm or Node installation commands before allowing them, and prefer a scoped or temporary execution path when appropriate.

Risk: Video generation tasks consume account credits and may not be cancellable after submission.

Mitigation: Confirm model, inputs, duration, and estimated credit cost with the user before submitting any generation task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-kling-3-clone)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit command arguments, status polling guidance, rewritten scripts, and links to generated video outputs when tasks complete.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
