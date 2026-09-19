## Description:

ElevenLabs music_v1 generates 10-300 second original music from a natural-language prompt for background music, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and agents use this skill to request original music from the ElevenLabs music_v1 model through the dLazy CLI and retrieve generated results for media workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and invokes a third-party npm CLI.

Mitigation: Review the package source and pin before installing or run it on demand with npx where appropriate.

Risk: Prompts and generation parameters are sent to dLazy cloud services and generated files are hosted on files.dlazy.com.

Mitigation: Avoid submitting sensitive prompts or media unless that data handling is acceptable for the intended use.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Use OS account protections, rotate or revoke keys from the dLazy dashboard, or pass DLAZY_API_KEY per invocation when persistent storage is not desired.

Risk: The artifact examples describe image/png output even though the skill is for music generation.

Mitigation: Treat media examples as documentation issues and verify actual audio outputs during acceptance testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown instructions with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a generated result URL, an asynchronous task identifier, or save the generated asset to a local path when requested.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
