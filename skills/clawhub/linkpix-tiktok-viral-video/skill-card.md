## Description:

Helps cross-border sellers and advertisers create multilingual TikTok product and promotional videos through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, MCN agencies, and ad specialists use this skill to plan and request short-form TikTok product videos, select available models, estimate credits, and retrieve completed video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to share an API key in chat.

Mitigation: Do not paste API keys into chat; set QHKIT_TOKEN or use a trusted secret store yourself.

Risk: Runtime installation or upgrades may fetch tools from live package sources.

Mitigation: Preinstall reviewed, pinned versions of qhkit and media tools instead of allowing runtime npm, npx, pip, or Node installations.

Risk: Selected media is uploaded to the Qinghu service for video generation.

Mitigation: Upload only media you are comfortable sharing with the service and review selections before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-tiktok-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands, task updates, and video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model options, credit estimates, task IDs, and completed video URLs.]

## Skill Version(s):

0.1.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
