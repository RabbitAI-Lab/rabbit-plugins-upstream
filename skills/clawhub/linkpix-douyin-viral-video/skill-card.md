## Description:

Guides Douyin creators and commerce teams through generating promotional short videos with Qinghu AI, from model selection and media upload to task tracking and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Douyin creators, e-commerce operators, and livestream teams use this skill to plan and request AI-generated promotional short videos, check estimated credits, and retrieve completed video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests an API key in chat, where credentials may be exposed.

Mitigation: Use a platform-managed secret or environment variable instead of sharing the raw key in conversation.

Risk: Installing or upgrading runtime tools may fetch executable packages into the user's environment.

Mitigation: Review installation steps and prefer pinned versions or administrator-preinstalled tooling.

Risk: Provided media is uploaded to the qhkit service for processing.

Mitigation: Only submit media approved for third-party processing.

Risk: Submitting a video task consumes API credits and cannot be canceled.

Mitigation: Show parameters and estimated credits, then obtain explicit user approval before submitting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-douyin-viral-video)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video links]

**Output Format:** [Markdown text with CLI commands and completed video URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation consumes credits after user confirmation; completed media is delivered by URL.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
