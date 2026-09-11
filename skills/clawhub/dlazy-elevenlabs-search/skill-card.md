## Description:

Search the ElevenLabs voice library by keyword, source, and category, returning playable previews for matched voices so an agent can help select a voice before TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and voice-workflow agents use this skill to search ElevenLabs voices by keyword, source, and category, then inspect playable preview results before selecting a voice for TTS.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence marks the release suspicious because the documentation mixes voice search with unrelated generation, upload, image-output, save, and async behavior.

Mitigation: Review the dLazy CLI and npm package before installation and treat the documented output schema as unreliable until the publisher clarifies the examples.

Risk: The skill requires a dLazy API key and sends prompts and parameters to the dLazy hosted API.

Mitigation: Use only an API key appropriate for this service, prefer per-invocation or contained local use, and rotate or revoke the key from the dLazy dashboard if needed.

Risk: Artifact behavior states that local media paths passed to applicable fields may be uploaded to dLazy media storage.

Mitigation: Avoid passing sensitive local files unless upload to the dLazy service is intended and permitted for the user's workflow.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; results may include hosted preview URLs and async task identifiers.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
