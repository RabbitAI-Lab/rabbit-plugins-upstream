## Description:

Helps creators adapt the structure of a reference short video into a product-focused script and generate a new video using Kling 3.0 through LinkPix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Short-video creators, social media teams, and online sellers use this skill to analyze a reference video's pacing and shots, adapt its script to a product, and request a newly generated video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to share an API key in chat.

Mitigation: Do not paste keys into chat; configure QHKIT_TOKEN or qhkit locally through a secure channel.

Risk: Suggested automatic installation may modify Node, npm packages, PATH, or shell startup files.

Mitigation: Review and approve installation commands and host changes before execution.

Risk: Reference links and local media may be sent to qhkit/iqinghu, and video tasks consume credits.

Mitigation: Share only approved media and confirm the parameters and expected credit cost before submitting a task.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-kling-3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video links]

**Output Format:** [Markdown with script drafts, command examples, and generated-video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires user confirmation and may consume paid credits.]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
