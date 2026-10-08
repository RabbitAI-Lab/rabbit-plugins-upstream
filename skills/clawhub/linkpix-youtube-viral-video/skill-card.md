## Description:

Guides an agent through creating YouTube product and brand videos with Qinghu AI, from model selection and cost estimation to generation and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Brand marketing teams, creators, and advertising teams use this skill to plan and generate YouTube product reviews, promotional videos, and Shorts using supplied product assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running unpinned Node packages can introduce unreviewed code into the agent's environment.

Mitigation: Review the package before installation and prefer a pinned, preinstalled qhkit version over unpinned installs or npx runs.

Risk: A reusable API key could be exposed when shared in chat or command history.

Mitigation: Keep the key in a managed secret or environment variable instead of pasting it into chat.

Risk: Reference images and videos are uploaded to the external generation provider.

Mitigation: Confirm the user is comfortable sharing each asset and avoid uploading sensitive material.

Risk: Video generation consumes credits and submitted tasks cannot be canceled.

Mitigation: Show the model, inputs, duration, and estimated cost, then obtain explicit user approval before submission.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-youtube-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and generated-video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports selected model, estimated and actual credits, task status, and provider-hosted video URLs when available.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
