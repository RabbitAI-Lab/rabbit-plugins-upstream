## Description:

PixVerse C1 视频模型支持文生视频、图生视频、首尾帧生成视频和参考图生成视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to submit prompts and optional reference media to PixVerse C1 through the dLazy CLI, then receive generated video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media are sent to dLazy services, and generated assets are hosted there.

Mitigation: Avoid submitting sensitive prompts or media unless they are approved for the service; review dLazy's terms before use.

Risk: The skill requires a dLazy API key, which can grant access to the user's organization account.

Mitigation: Keep the key in the user-only CLI configuration or a protected environment variable, avoid sharing it in logs or commands, and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, Video, JSON]

**Output Format:** [JSON result envelope with generated asset URLs; video assets are hosted by dLazy]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a generation task ID for asynchronous runs; generated outputs may be saved locally.]

## Skill Version(s):

1.2.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
