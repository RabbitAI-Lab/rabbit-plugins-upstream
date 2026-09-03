## Description:

Helps short-video creators and ecommerce teams use Qinghu qhkit to analyze viral video structure and generate HappyHorse 1.1-style recreated video assets after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External short-video creators, ecommerce operators, and advertising teams use this skill to derive a script from a reference short video, adapt it to their own product, estimate credits, and submit a HappyHorse-style video generation task through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to configure a reusable qhkit API key and may prompt users to share credentials in chat.

Mitigation: Use a least-privilege or disposable API key when possible, avoid pasting production credentials into chat, and prefer environment-variable or local CLI configuration paths.

Risk: Video generation sends user media, source video links, prompts, and task parameters to an external service.

Mitigation: Confirm that the user intends to use Qinghu/qhkit and is comfortable sending the relevant media or links before submitting generation tasks.

Risk: Generation can consume credits and create tasks that may not be cancellable after submission.

Mitigation: Run estimates where supported and confirm the exact model, inputs, duration, and expected credit cost with the user before calling generate.

Risk: Recreating viral videos can create copyright, endorsement, or platform-policy issues if original creative work is copied too closely.

Mitigation: Use the source video only for structure and creative direction, rewrite scripts for the user's product, and avoid copying original footage, voices, branding, or dialogue.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-happyhorse-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rewritten video scripts, command parameters, credit estimates, task IDs, status updates, and result URLs.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
