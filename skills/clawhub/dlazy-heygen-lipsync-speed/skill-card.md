## Description:

HeyGen Lipsync Speed: Fast lip-sync model, ideal for scenarios requiring rapid generation. HeyGen Lipsync Speed：快速唇形同步模型，适合对生成速度要求较高的场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate fast lip-synced media by matching supplied video and audio, with optional captions, duration adjustment, and speech enhancement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reported a mismatch between the lip-sync purpose and the supplied login and authentication steps; several references, including CLI/package and API behavior, could not be resolved.

Mitigation: Review the CLI help and available package/API documentation before authenticating or running the command. The benign scan verdict has medium confidence and is not a safety guarantee.

Risk: Local video or audio paths are uploaded to dLazy media storage, and generated assets are hosted there.

Mitigation: Use only media approved for upload and review the service terms before sending sensitive content.

## Reference(s):

- [dLazy CLI project link](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Media files, JSON]

**Output Format:** [JSON response with generated media URLs; the asset can also be saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may complete asynchronously.]

## Skill Version(s):

1.3.41 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
