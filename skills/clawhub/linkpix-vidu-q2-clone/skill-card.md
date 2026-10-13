## Description:

Helps sellers adapt a reference video's shot structure and pacing to their products, then generate a Vidu Q2 promotional video through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketing teams use this skill to analyze a short-form video, adapt its shot structure into a product-specific script, and generate a promotional video after approving the script and credit cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit may introduce unreviewed package changes.

Mitigation: Use a sandbox or managed environment with a vetted, pinned qhkit version before running the skill.

Risk: An API token may be exposed if shared in chat or stored insecurely.

Mitigation: Provide the token through a secure secret store rather than pasting it into chat.

Risk: Reference and product media are uploaded to an external service.

Mitigation: Confirm that the media is authorized for external processing before upload.

Risk: Video generation consumes credits and submitted tasks cannot be canceled.

Mitigation: Confirm the model, inputs, duration, and estimated credit cost with the user before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-vidu-q2-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with script comparison, generation parameters, and video result link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports estimated and actual credit charges when available; generated media is delivered through a video URL.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
