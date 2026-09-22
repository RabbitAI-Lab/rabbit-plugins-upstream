## Description:

Detects whether an image, video, or audio file is AI-generated, including visual deepfakes and likely generator attribution, and returns confidence scores for decisioning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to check image, video, or audio inputs for AI generation, deepfake indicators, and likely generator attribution before acting on or reporting media authenticity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or audio may be uploaded to dLazy-hosted media storage and analyzed by remote services.

Mitigation: Avoid confidential or private media unless the user understands the provider's retention and privacy terms; prefer public URLs or explicit confirmation before local uploads.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Protect the local config file, use per-invocation credentials when appropriate, and remove or rotate the key if the environment is shared or compromised.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON detection result plus a human-readable text summary, with Markdown command examples in the skill documentation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires exactly one image, video, or audio input; asynchronous mode may return a task id for later polling.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
