## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can turn supplied text into speech with Doubao TTS, choose a supported voice and speaking speed, and retrieve the generated audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had medium confidence and did not inspect the CLI package, so it could not fully establish that the commands provide the described Doubao speech synthesis.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package and confirm its Doubao TTS behavior before installing.

Risk: Text prompts are sent to the dLazy API for synthesis.

Mitigation: Avoid sending sensitive text unless its use with the dLazy service is approved.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, Files, Shell commands]

**Output Format:** [Generated audio URL or downloaded audio file; asynchronous runs can return JSON task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice language, voice ID, and speaking speed are configurable.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
