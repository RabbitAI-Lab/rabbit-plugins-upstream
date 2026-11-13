## Description:

Provides ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can generate multilingual voice narration, dubbing, audiobook passages, and character dialogue using ElevenLabs voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial security review reports a mismatch between the advertised ElevenLabs speech purpose and the commands it examined, and did not establish downstream behavior.

Mitigation: Before relying on the skill, confirm that the installed dLazy CLI command and service match the intended ElevenLabs workflow.

Risk: The partial security review did not establish how the CLI handles credentials.

Mitigation: Review the CLI authentication behavior and installation source before storing an API key; use the documented key rotation or revocation controls when needed.

## Reference(s):

- [CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service site](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON response with a generated audio URL or saved audio file; an asynchronous task identifier may be returned.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice and speech-style controls are available; generation may run asynchronously.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
