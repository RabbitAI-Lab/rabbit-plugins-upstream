## Description:

Helps WeChat Channels merchants and marketing teams plan and generate short promotional videos through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

WeChat Channels merchants and marketing teams use this skill to prepare product promotions, storytelling videos, and livestream teasers for social distribution. It guides model selection, creation, cost confirmation, task tracking, and delivery through Qinghu AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to send an API key in chat.

Mitigation: Do not share API keys in chat; configure the token locally using an environment variable or trusted secret store.

Risk: The skill directs automatic installation of qhkit and related tools.

Mitigation: Review installations before running them and prefer a vetted, version-pinned qhkit package.

Risk: Reference media is uploaded to the Qinghu service, and video generation can spend service credits.

Mitigation: Upload only approved media and confirm the proposed parameters and estimated credits before submitting a generation task.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-shipinhao-viral-video)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and generated-video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model recommendations, credit estimates, task IDs, and completion status.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
