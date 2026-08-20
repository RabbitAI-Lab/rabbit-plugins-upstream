## Description:

青虎AI 商品视频画质超清提升 helps an agent upscale short product videos and apply frame interpolation while preserving audio-video synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to improve blurry, low-bitrate, compressed, or older product videos by submitting an authorized video to Qinghu AI for upscaling and smoother motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install and execute the third-party qhkit CLI.

Mitigation: Install qhkit only when needed, use the disclosed package source, and review installation errors before continuing.

Risk: The workflow uses a Qinghu API token.

Mitigation: Keep the token out of chat output and logs, use the documented configuration path or environment variable, and rotate the token if it is exposed.

Risk: Input videos are uploaded to an external processing service.

Mitigation: Use only videos the user owns or is authorized to process, and avoid submitting sensitive or restricted content.

Risk: The workflow can spend Qinghu credits after estimate approval.

Mitigation: Run an estimate with the same parameters before generation, stop when balance is insufficient, and wait for user confirmation before submitting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-upscale-hd)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Qinghu workflow commands, status guidance, media result links, and final credit usage reporting.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
