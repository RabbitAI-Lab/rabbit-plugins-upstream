## Description:

This skill helps agents generate WeChat Channels commerce videos with LinkPix and qhkit by selecting current video models, preparing platform-specific prompts, confirming credit-spending generation, polling task status, and returning generated video links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, marketers, and agent users use this skill to create WeChat Channels product-promotion, seeding, knowledge-talk, emotional-story, livestream-funnel, and private-traffic conversion videos. It guides model discovery, media upload, cost estimation, user confirmation, generation, status polling, and delivery through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can install qhkit and possibly Node on the user's machine.

Mitigation: Review the package source and install command before execution, and prefer existing trusted Node and qhkit installations when available.

Risk: The workflow can save or use a qhkit API token.

Mitigation: Treat the token as a secret, prefer environment-variable or configured secret storage, and avoid exposing it in shared logs or prompts.

Risk: Referenced media files may be uploaded to the provider during generation.

Mitigation: Confirm that selected files are intended for upload and do not contain sensitive or unauthorized content before submitting a task.

Risk: Video generation may spend credits after confirmation.

Mitigation: Show the selected model, files, duration, orientation, language, and estimated credits, then wait for explicit user approval before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-shipinhao-viral-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit setup steps, model and parameter recommendations, credit estimates, generation confirmations, polling instructions, and generated video URLs.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
