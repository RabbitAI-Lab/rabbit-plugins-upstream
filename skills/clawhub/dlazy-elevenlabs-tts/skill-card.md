## Description:

Generates multilingual ElevenLabs eleven_v3 text-to-speech audio through the dLazy CLI, with curated voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to create voiceover, audiobook, dubbing, and character-dialog audio from text prompts with selectable ElevenLabs voices and tuning controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts and selected parameters are sent to dLazy's hosted API, and generated files may be hosted by dLazy.

Mitigation: Review data sensitivity before use and avoid submitting confidential text unless dLazy's terms and account controls meet deployment requirements.

Risk: dLazy API credentials may be stored in the local CLI config.

Mitigation: Use per-invocation DLAZY_API_KEY when appropriate, protect ~/.dlazy/config.json, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact's sample output schema describes image output for an audio-generation skill.

Mitigation: Treat the sample output shape as unreliable until confirmed; validate actual CLI responses and use --save or returned URLs according to observed audio output.

Risk: A global npm installation persists the dLazy CLI binary on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution when a persistent install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI may return hosted output URLs or an async task ID; generated audio can be saved locally with --save.]

## Skill Version(s):

1.3.9 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
