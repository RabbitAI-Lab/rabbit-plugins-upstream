## Description:

青虎AI 爆款视频模仿（女装） helps an agent use Qinghu AI to transfer motion from a reference video onto a user-provided womenswear model reference image and generate short apparel-commerce videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agent users use this skill to prepare, price, confirm, submit, and poll Qinghu AI womenswear video imitation jobs. It is suited for authorized source videos and model images where the user wants motion transfer for womenswear product or promotional clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads user-selected videos and images to Qinghu AI for processing.

Mitigation: Use only media that the user owns or is authorized to process, and confirm that uploading the selected files is acceptable before submission.

Risk: The generation workflow is paid and consumes Qinghu credits once submitted.

Mitigation: Run an estimate first, repeat the selected workflow, field values, assets, and expected credit use, and submit only after explicit user approval.

Risk: The online field schema may change after the documented 2026-08 snapshot.

Mitigation: Call qhkit workflow options for wf_007 before preparing final parameters and use the returned labels exactly.

Risk: The generated task is asynchronous and may take significant time to complete.

Mitigation: Preserve the returned logId and poll status until the workflow reaches a terminal state before reporting completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-womens)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit shell commands, JSON command payloads, status summaries, generated media URLs, and a final credit-consumption line when a job succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the qhkit CLI and Qinghu credentials; generation is paid, asynchronous, and returns media URLs after polling.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
