## Description:

Clone a custom voice from a clean sample using Alibaba Bailian Qwen3-TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to submit a clean voice sample and create a reusable custom voice for later text-to-speech calls through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires dLazy API credentials, and the security review noted that credential setup was not clearly tied to the stated voice-cloning purpose.

Mitigation: Before use, confirm that you trust the pinned dLazy CLI and are comfortable authorizing it with your organization's API credentials.

Risk: A local voice sample provided to the CLI is uploaded to dLazy-hosted media storage for processing.

Mitigation: Submit only voice samples you are authorized to process and comfortable sending to the hosted service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [JSON response with task status and generated result metadata or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result can be returned asynchronously when --no-wait is used.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
