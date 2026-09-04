## Description:

ElevenLabs eleven_v3 text-to-speech with curated multilingual voices and stability, similarity, and style controls for dubbing, audiobooks, and character dialog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate ElevenLabs text-to-speech audio through the dLazy CLI, choosing curated or custom voices and tuning stability, similarity, and style settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI and sends prompts, selected parameters, and explicitly supplied files to dLazy's hosted service.

Mitigation: Install only after accepting that data flow, and avoid sending sensitive prompts or files unless the use case permits it.

Risk: The dLazy API key may be persisted in ~/.dlazy/config.json without enforced local file-permission protection.

Mitigation: On shared machines, prefer per-invocation DLAZY_API_KEY or verify local config file permissions, then rotate or revoke the key when it is no longer needed.

Risk: A global CLI install leaves a persistent executable and credential configuration on the machine.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 invocation when a non-persistent CLI path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples; generated audio is returned by URL or saved to a local file when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation, dry-run cost estimates, custom voices, and optional local save paths.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
