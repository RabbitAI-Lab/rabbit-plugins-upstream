## Description:

快速生成电影级商品广告视频：基于物理渲染的光影场景、细腻画面质感，适合品牌宣传与高端商品展示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and marketing teams use this skill to prepare and run LinkPix/qhkit workflows for cinematic product advertisement videos, including model selection, prompt refinement, credit estimation, task submission, status polling, and final video handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a globally installed qhkit CLI and Node runtime setup.

Mitigation: Confirm the user is comfortable installing or using qhkit before running setup commands, and report installation failures clearly.

Risk: Referenced product images or videos may be uploaded to the provider during generation.

Mitigation: Confirm the user is comfortable uploading the selected media files before submitting generation requests.

Risk: Video generation can consume paid credits and submitted tasks cannot be canceled by the skill.

Mitigation: Run estimates when supported and require explicit user approval of model, duration, referenced files, and expected credits before any generate action.

Risk: qhkit credentials may be required outside preconfigured OpenClaw environments.

Mitigation: Use existing configured credentials when available and ask the user to provide or configure tokens through qhkit or QHKIT_TOKEN when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ad-film)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit command plans, confirmation summaries before paid generation, task IDs, status updates, and generated video URLs when available.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
