## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can turn Chinese or English text into spoken audio using Doubao TTS, selecting a voice and speech speed as needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports CLI login behavior that is not clearly tied to the text-to-speech purpose; its inspection of referenced details was partial.

Mitigation: Review the CLI behavior and confirm what login stores or sends before use; use a dedicated, revocable dLazy API key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Audio, JSON result metadata]

**Output Format:** [Generated audio file or URL, with JSON task and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs and saving generated assets to a local path.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
