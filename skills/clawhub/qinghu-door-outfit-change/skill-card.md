## Description:

青虎AI 女装开门换装爆款仿拍：上传一张模特图和最多 4 套服饰图，快速生成「开门换装」变装视频，可选配音频，成本低出片快，适配女装带货与穿搭创作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agents use this skill to prepare and run Qinghu AI door-opening outfit-change video jobs from one model image, up to four clothing images, and optional audio. It is intended for paid video generation workflows where the agent estimates credits, confirms billable submission, polls job status, and returns generated media URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billable Qinghu workflow submissions consume credits and cannot be cancelled after submission.

Mitigation: Run an estimate first, summarize the selected workflow, field values, media inputs, and expected credit cost, then wait for explicit user approval before calling generate.

Risk: The workflow uploads user-provided model, clothing, and optional audio files to Qinghu for processing.

Mitigation: Use only media the user owns or is authorized to process, and confirm sensitive or commercial inputs before upload.

Risk: The qhkit setup may install CLI dependencies and store or use a Qinghu API key locally.

Mitigation: Install only the declared @iqinghu/qhkit package, prefer official sources, validate Node downloads when bootstrapping, and use the documented token configuration or QHKIT_TOKEN.

Risk: Online Qinghu workflow fields can change after the documented 2026-08 snapshot.

Mitigation: Call qhkit workflow options and use the returned labels exactly before estimating or submitting a job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-door-outfit-change)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with shell commands and JSON workflow parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent instructions for estimating, submitting, polling, and delivering Qinghu workflow video generation jobs.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
