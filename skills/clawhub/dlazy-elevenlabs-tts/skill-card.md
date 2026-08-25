## Description:

语音合成 ElevenLabs TTS helps agents generate ElevenLabs eleven_v3 text-to-speech through the dLazy CLI with curated multilingual voices and stability, similarity, and style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to create multilingual voiceover, audiobook, dubbing, and character-dialog audio from text prompts through a hosted dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found that the skill asks users to save a dLazy API key while the referenced CLI does not enforce the user-only file permissions claimed by the skill.

Mitigation: Prefer supplying DLAZY_API_KEY per invocation, manually restrict permissions on ~/.dlazy/config.json after dlazy login or dlazy auth set, and rotate the dLazy API key if it may have been exposed.

Risk: Prompts, parameters, and referenced local media paths are sent to dLazy services for processing and hosted output delivery.

Mitigation: Review content before submission and avoid sending sensitive material unless the user's policy permits processing by dLazy services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses; generated assets can be downloaded with --save.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; API calls use api.dlazy.com and file outputs are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.8 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
