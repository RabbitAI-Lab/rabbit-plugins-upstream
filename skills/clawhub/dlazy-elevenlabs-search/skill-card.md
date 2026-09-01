## Description:

Searches the ElevenLabs voice library by keyword, source, and category, returning playable previews for matched voices before TTS selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to search and compare ElevenLabs voices by descriptor, source, and category before selecting a voice for TTS work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external dLazy CLI and hosted API that requires a dLazy API key and sends search prompts and parameters to dLazy.

Mitigation: Use the pinned npx invocation when avoiding a global install, protect and rotate API keys, and review prompts before sending them to the service.

Risk: Passing local media paths may upload files to dLazy media storage.

Mitigation: Do not pass local file paths unless upload is intended and the files are appropriate for external processing.

Risk: The documented image output and media-generation errors may not match this voice-search behavior.

Mitigation: Treat those sections as documentation drift and validate actual CLI output before automating downstream handling.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON responses containing matched voice preview outputs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
