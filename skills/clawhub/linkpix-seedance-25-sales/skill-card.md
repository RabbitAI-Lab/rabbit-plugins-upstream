## Description:

Helps e-commerce teams create Seedance 2.5 product-promotion videos from product images and prompts using qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Brand teams, e-commerce creatives, and marketers use this skill to generate product demonstrations and promotional videos from product images and selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to share an API key in chat.

Mitigation: Keep API keys out of chat; use a secure local environment variable or platform secret instead.

Risk: Installing or upgrading packages can make persistent host changes, especially with unpinned versions.

Mitigation: Review and approve package installations before execution, and prefer pinned, trusted versions.

Risk: Product media is sent to qhkit, and video-generation tasks consume paid credits.

Mitigation: Approve the media and estimated cost before submitting a generation task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-seedance-25-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [qhkit API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with commands and a finished video link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task status and credits charged; video generation requires user confirmation.]

## Skill Version(s):

0.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
