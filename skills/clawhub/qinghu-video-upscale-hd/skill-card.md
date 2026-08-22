## Description:

青虎AI 商品视频画质超清提升 helps agents upscale short product videos and apply frame interpolation while preserving audio-video synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to improve blurry, low-bitrate, compressed, or older product videos through Qinghu AI video upscaling and frame interpolation. The skill guides the agent through estimating cost, confirming paid generation, polling task status, and returning the completed video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload a local video file to an external paid service.

Mitigation: Confirm the exact video file, expected upload, and estimated credit charge with the user before running generation.

Risk: Generation consumes Qinghu credits and may require a paid subscription or available entitlement.

Mitigation: Run an estimate first, stop when balance or entitlement checks fail, and wait for explicit user approval before submitting the task.

Risk: The workflow is limited to short videos and online field definitions may change.

Mitigation: Use the live options response for field names and ask the user to trim videos longer than 60 seconds before processing.

Risk: Commercial use of unlicensed source videos can create rights issues.

Mitigation: Remind users to process only videos they own or are authorized to use, especially for commercial outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-upscale-hd)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and status/result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs and a final Qinghu credit-consumption line after successful completion.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
