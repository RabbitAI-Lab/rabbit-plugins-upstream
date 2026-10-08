## Description:

Helps sellers analyze a reference short video, adapt its shot structure and pacing to their product, and generate a promotional video through LinkPix's Vidu Q3 workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketing teams use this skill to turn a short-video link into a reviewed, product-specific script and then request a promotional video that follows the reference's camera angles and pacing without copying its footage or dialogue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requests an API key, which could be exposed if pasted into chat or command history.

Mitigation: Configure the key locally using a secret mechanism or environment variable; do not paste it into chat.

Risk: The workflow can make broad local changes by installing Node and qhkit from npm.

Mitigation: Review installation steps first, use an isolated environment where practical, and prefer pinned package versions.

Risk: Generating a video consumes credits and a close recreation may copy protected creative content.

Mitigation: Confirm parameters and estimated credits before submitting; adapt only the reference's structure and ideas, not its footage or dialogue.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-vidu-q3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video links]

**Output Format:** [Markdown script comparison, task updates, and a generated-video link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires user confirmation of parameters and estimated credits; completion includes the resulting video URL and actual credits charged.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
