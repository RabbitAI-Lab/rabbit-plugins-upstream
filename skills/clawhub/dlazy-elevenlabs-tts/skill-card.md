## Description:

ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate spoken audio for dubbing, audiobooks, and character dialogue through the dLazy ElevenLabs TTS CLI wrapper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, API keys, and any provided local file paths may be sent to dLazy's hosted service during use.

Mitigation: Only provide content suitable for dLazy processing, keep API keys scoped to the intended organization, and rotate or revoke keys when needed.

Risk: A global npm install persists a third-party CLI binary on the user's system.

Mitigation: Review the linked source and npm package before installing, or use the pinned npx command or an isolated environment when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses with hosted result URLs or saved audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task polling and optional local save paths.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
