## Description:

AI生成电商视频 | LinkPix helps agents route e-commerce video requests to LinkPix/qhkit workflows for product videos, short-form promotional clips, ads, storyboards, and multi-image video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce operators, and content creators use this skill through an agent to plan, configure, price, submit, and monitor LinkPix/qhkit video-generation jobs for product showcases, advertisements, and platform-specific short videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install local tooling before use.

Mitigation: Install only the documented qhkit package, prefer the official npm source, and follow the documented SHA256 check before unpacking a downloaded Node runtime.

Risk: The skill may upload selected product media and use a stored API token.

Mitigation: Confirm which files will be uploaded, keep API keys out of chat history where possible, and use the configured token or environment variable only for the intended provider account.

Risk: Generation jobs can consume paid credits and cannot be cancelled after submission.

Mitigation: Before any generate command, confirm the selected model, media, duration, orientation, language, and estimated cost with the user.

Risk: Model availability, pricing, and constraints are dynamic.

Mitigation: Query qhkit options for the current model list and rules before choosing a model, and avoid treating examples in the skill text as defaults.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model-selection guidance, cost-estimate prompts, task IDs, status checks, and generated video URLs returned by qhkit.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
