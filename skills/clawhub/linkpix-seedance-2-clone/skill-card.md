## Description:

Helps short-form video marketers adapt the structure and pacing of a reference video into a product-focused script and generate a new video through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External short-video and ecommerce marketers use this skill to analyze a reference clip, adapt its shot structure to their own product, and generate a promotional video after reviewing the script and estimated cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading live Node/npm packages and changing local tooling may affect the user's environment.

Mitigation: Review proposed installs, upgrades, and any shell-profile changes before allowing them.

Risk: Sharing a Qinghu API key in chat may expose credentials.

Mitigation: Set QHKIT_TOKEN through a secret or environment mechanism rather than pasting the key into chat.

Risk: Generating a video consumes credits and submits reference materials to an external service.

Mitigation: Confirm the source materials, model, duration, and estimated credits with the user before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-seedance-2-clone)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with script comparisons, command examples, and a generated-video link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task status and credits charged when available; video generation requires user approval before submission.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
