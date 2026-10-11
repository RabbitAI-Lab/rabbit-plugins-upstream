## Description:

Guides short-video creators in adapting a reference video's script and pacing for their own products and generating a new video through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Short-video creators, marketing teams, and sellers use this skill to analyze a shared video link, adapt the resulting script for a product, and request an AI-generated promotional video after approving the script and estimated credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-run installation or upgrades of qhkit may execute unreviewed package code.

Mitigation: Install only if the qhkit service is trusted; prefer a preinstalled, pinned version and review upgrades.

Risk: Sharing an API key in chat may expose credentials.

Mitigation: Provide the key through a secure secret store or environment variable rather than pasting it into chat.

Risk: Video generation can spend credits on unintended tasks or settings.

Mitigation: Review the script, task parameters, and credit estimate before approving paid generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-seedance-25-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video links]

**Output Format:** [Markdown with script comparisons, commands, and generated-video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires user approval and may consume paid credits.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
