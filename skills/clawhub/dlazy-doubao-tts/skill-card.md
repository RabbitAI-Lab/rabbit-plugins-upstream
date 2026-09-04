## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn text prompts into natural speech through dLazy's hosted Doubao TTS service. It supports Chinese and English voices, speech speed selection, asynchronous generation, and optional local saving of generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts and referenced media may be sent to dLazy's hosted service.

Mitigation: Use this skill only for content appropriate for dLazy processing, avoid unnecessary sensitive inputs, and review service terms before deployment.

Risk: The skill stores or uses a dLazy API key for authenticated requests.

Mitigation: Prefer explicit user requests before invocation, use the documented dLazy authentication flow, and keep the API key rotation and revocation path available.

Risk: Generated outputs are hosted remotely and API usage may consume credits.

Mitigation: Use dry-run or explicit confirmation for cost-sensitive work, monitor account credits, and save required outputs locally when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON, Audio files]

**Output Format:** [JSON responses from the dLazy CLI, with hosted output URLs and optional local files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated outputs are hosted remotely by dLazy unless saved locally.]

## Skill Version(s):

1.3.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
