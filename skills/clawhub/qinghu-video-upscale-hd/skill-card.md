## Description:

Qinghu AI upscales short product videos by improving resolution and adding frame interpolation while preserving audio-video sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit authorized short product videos to Qinghu AI for video clarity enhancement, upscaling, and smoother motion. It is intended for blurry, low-bitrate, screen-recorded, compressed, or older video assets up to 60 seconds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may modify the host environment by installing or upgrading Node and qhkit.

Mitigation: Prefer preinstalling qhkit in a controlled environment and review any global package installation or runtime download before execution.

Risk: The workflow uploads target videos to an external Qinghu service and consumes Qinghu credits after confirmation.

Mitigation: Use only authorized media, run an estimate first, disclose expected credit use, and wait for explicit user approval before generation.

Risk: The skill handles persistent Qinghu API credentials.

Mitigation: Configure credentials through a secure secret mechanism or existing config path instead of asking users to paste API keys into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-upscale-hd)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, Qinghu credentials, user confirmation before paid generation, and status polling for video URLs.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
