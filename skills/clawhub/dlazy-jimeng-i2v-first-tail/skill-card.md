## Description:

Generate coherent transition videos using Jimeng's first and tail frame models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers provide a prompt plus first and last frames to generate a transition video with Jimeng.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy services, and generated media is hosted by files.dlazy.com.

Mitigation: Provide only content approved for cloud processing and review generated media before use.

Risk: The API key is stored in the local CLI configuration.

Mitigation: Protect access to the configuration and rotate or revoke the key through the dLazy dashboard if exposed.

Risk: The examples use image flags that differ from the documented first-frame and last-frame flags, and the sample result labels output as an image.

Mitigation: Check the command help and verify the expected input flags and returned media type before running a generation.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [CLI project page (metadata link)](https://github.com/dlazy-ai/cli)
- [CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Media files]

**Output Format:** [JSON response with generated media URLs; media file when saved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a prompt, first and last frames, and a 5- or 10-second duration; asynchronous mode can return a task ID.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
