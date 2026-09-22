## Description:

Generates 10-300 second original music tracks from natural-language prompts using the ElevenLabs music_v1 model through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate background music, advertising music, and short-video soundtracks from prompt text. It is suited for agent workflows that can install or invoke the dLazy CLI and authenticate to the hosted dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party cloud CLI and hosted dLazy endpoints for inference and generated asset storage.

Mitigation: Review the @dlazy/cli package or source before deployment, and use this skill only where calls to api.dlazy.com and files.dlazy.com are acceptable.

Risk: Prompts and referenced local media files may be sent to dLazy services when the CLI is invoked.

Mitigation: Avoid passing sensitive prompts or local files unless they are intended to be uploaded to the hosted service.

Risk: Authentication can persist an API key in the user's local dLazy CLI configuration.

Mitigation: Use npx or the DLAZY_API_KEY environment variable when a persistent global install or saved key is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return generated asset URLs, asynchronous task identifiers, or save generated audio assets to a requested local path.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
