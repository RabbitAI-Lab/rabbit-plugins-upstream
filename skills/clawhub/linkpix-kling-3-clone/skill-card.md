## Description:

Guides agents through cloning popular short-video structures with Qinghu qhkit by analyzing a source video, rewriting its script for a user's product, and generating a Kling 3.0-style video after confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Short-video operators, editors, and ecommerce sellers use this skill to analyze Douyin, TikTok, Kuaishou, Xiaohongshu, or WeChat Channels clips, adapt the structure to their product, and generate a new marketing video through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to share an API key in chat.

Mitigation: Do not paste reusable API keys into chat; set credentials locally through a secret store, environment variable, or qhkit configuration.

Risk: The skill installs mutable third-party tooling with broad local effects.

Mitigation: Install only after trusting the Qinghu/qhkit provider, prefer pinned versions where practical, and review package changes before upgrading.

Risk: The skill can trigger paid video-generation calls.

Mitigation: Review estimated credits and all generation parameters before submitting a task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-kling-3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, status-check guidance, and generated media URLs from the external qhkit service.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
