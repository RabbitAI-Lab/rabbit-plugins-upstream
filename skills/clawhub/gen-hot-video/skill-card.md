## Description:

Generates product remake videos through the Flyelep hot-video recreation API by applying the style of a reference viral video to supplied product footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing operators use this skill to collect product and reference video inputs, call Flyelep's asynchronous video-generation API, poll for completion, and return the generated video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local videos may be uploaded to permanent public URLs without a clear consent checkpoint.

Mitigation: Ask for explicit user confirmation before uploading local media and avoid private, proprietary, or sensitive videos unless the user accepts the exposure.

Risk: The workflow sends the selected videos and API key to Flyelep.

Mitigation: Use a user-provided key only at runtime and do not store credentials in skill files, examples, repositories, or persistent configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/gen-hot-video)
- [Flyelep publisher profile](https://clawhub.ai/user/flyelepai)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)
- [Flyelep generateHotVideo API](https://www.flyelep.cn/prod-api/poster-design/api/v1/aiTool/generateHotVideo)
- [Flyelep queryTaskResult API](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)
- [Flyelep file upload API](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON request bodies and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided Flyelep API credentials and product/reference video URLs or uploaded files.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
