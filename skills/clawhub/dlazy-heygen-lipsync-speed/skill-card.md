## Description:

Generates fast lip-synchronized media using dLazy's hosted HeyGen Lipsync Speed service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to synchronize supplied audio with a video through dLazy's hosted HeyGen Lipsync Speed service. They can adjust timing and audio options, request captions, and retrieve the generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio and video are uploaded to dLazy for processing, and generation uses service credits.

Mitigation: Send only media approved for cloud processing, review the request and expected cost, and confirm available credits before generating.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the key and its configuration file, avoid exposing it in shared logs, and rotate or revoke it when no longer needed.

## Reference(s):

- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Generated lip-synchronized video or media, JSON task and result metadata]

**Output Format:** [Hosted media URL with JSON result metadata; optionally a downloaded media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when run without waiting; optional captions and audio adjustments are available.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
