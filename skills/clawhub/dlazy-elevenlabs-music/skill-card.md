## Description:

ElevenLabs music_v1 generates 10-300 second original music from a natural-language prompt for background music, advertisements, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to invoke the pinned dLazy CLI for ElevenLabs music generation from prompts, with optional asynchronous execution and local saving of generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any user-supplied media paths may be sent to dLazy hosted API endpoints.

Mitigation: Do not submit sensitive or restricted content unless the user has approved use of the hosted service.

Risk: The dLazy API key can be saved in the local CLI configuration.

Mitigation: Prefer per-invocation credentials when appropriate, protect the config file, and rotate or revoke the key if exposure is suspected.

Risk: The skill depends on a third-party pinned CLI package.

Mitigation: Confirm trust in the dLazy CLI package before installation, or use the pinned npx invocation to avoid a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON responses from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted output URLs, asynchronous task identifiers, or save generated music assets to a local path.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
