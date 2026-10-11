## Description:

Guides agents in creating TikTok marketing videos with Qinghu AI, from selecting a model and preparing assets through estimating costs, submitting a task, and delivering the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border sellers, agencies, and advertisers use this skill to plan and generate short-form TikTok Shop and TikTok Ads videos, including multilingual product pitches and promotional clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests an API key and may store it for qhkit use.

Mitigation: Use a controlled environment variable or managed secret store instead of pasting the key into chat.

Risk: Setup may install or upgrade Node and npm tools on the host.

Mitigation: Review the installation steps and run the skill in an isolated environment where possible.

Risk: Submitting a video task consumes credits and cannot be cancelled.

Mitigation: Check generation parameters and available credit estimates, then obtain explicit approval before submitting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-tiktok-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video links]

**Output Format:** [Markdown with task details and generated video URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task IDs and credit usage; video generation is asynchronous.]

## Skill Version(s):

0.1.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
