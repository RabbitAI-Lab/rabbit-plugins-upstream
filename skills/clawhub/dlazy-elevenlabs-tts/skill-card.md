## Description:

Provides ElevenLabs eleven_v3 text-to-speech through the dLazy CLI, with curated multilingual voices and stability, similarity, and style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to generate text-to-speech audio for dubbing, audiobook content, and character dialogue through the dLazy-hosted ElevenLabs wrapper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any referenced media are sent to dLazy cloud endpoints, and generated results are hosted by dLazy.

Mitigation: Use only content approved for third-party cloud processing and review dLazy service terms before use.

Risk: A dLazy API key may be stored in the local user configuration when using `dlazy login` or `dlazy auth set`.

Mitigation: Use the per-run `DLAZY_API_KEY` environment variable when persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact's output example describes image/PNG output for a TTS tool, which may mislead users about returned assets.

Mitigation: Verify the actual response media type and saved file extension when invoking the CLI.

Risk: A global npm install persists a third-party CLI on the system.

Mitigation: Use the documented `npx @dlazy/cli@1.2.3` path when you do not want a persistent global CLI installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; results may include asynchronous task IDs or generated media URLs hosted by dLazy.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
