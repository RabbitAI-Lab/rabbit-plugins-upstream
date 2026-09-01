## Description:

Audio Generate helps an agent choose and run a dlazy CLI audio, TTS, music, or sound-effect model from a user prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate speech, dialogue, music, and sound effects through the dlazy CLI. The skill is suited for agents that need to select an appropriate hosted audio model, check command parameters, and execute a generation command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates the skill as suspicious because it routes a broad third-party CLI and is not clearly limited to audio.

Mitigation: Review the skill before installation and keep agent use limited to the documented audio, TTS, music, voice-search, and sound-effect commands unless broader dlazy CLI use is intended.

Risk: Prompts and user-provided media paths may be sent to dLazy cloud services, with generated media hosted by dLazy.

Mitigation: Use the skill only when dLazy cloud processing is acceptable, and avoid sending sensitive prompts or local media files unless the user has approved that disclosure.

Risk: The skill requires a dLazy API key stored locally or supplied through an environment variable.

Mitigation: Use the documented dLazy authentication flow, protect the local configuration file, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands; dlazy CLI invocations return JSON envelopes and hosted media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy API and media endpoints.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
