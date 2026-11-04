## Description:

Generates ElevenLabs eleven_v3 speech from text through dLazy, with multilingual voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn text into multilingual speech for dubbing, audiobooks, and character dialogue, selecting a voice and adjusting speech style as needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text or media sent for generation is transferred to dLazy's hosted service.

Mitigation: Submit only text or media you intend to share with dLazy.

Risk: Authentication saves a reusable API key locally, and the pinned CLI implementation and its credential protections were not verified.

Mitigation: Review the pinned CLI before installing, use it only in a trusted environment, and rotate or revoke the key if needed.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)

## Skill Output:

**Output Type(s):** [Audio, API calls, Shell commands]

**Output Format:** [Generated audio result URL or saved audio file, with JSON task and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs can return a task ID and status; --save downloads the result locally.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
