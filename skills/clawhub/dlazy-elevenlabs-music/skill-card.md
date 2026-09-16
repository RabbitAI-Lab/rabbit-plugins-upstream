## Description:

Generates 10-300 second original music from a natural-language prompt using ElevenLabs music_v1 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request short music tracks for background music, advertising, and short-video soundtracks from a prompt. It wraps a cloud music generation service and can save returned assets locally when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a third-party npm CLI and sends prompts and explicit file inputs to dLazy cloud endpoints.

Mitigation: Review the CLI package before use, run it per invocation or in an isolated environment when appropriate, and avoid providing sensitive prompts or files unless the cloud processing path is acceptable.

Risk: Authentication uses a dLazy API key that may be stored in a local CLI configuration file.

Mitigation: Prefer DLAZY_API_KEY for per-invocation credentials when persistence is not desired, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs, async task identifiers, or saved local assets when the CLI save option is used.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
