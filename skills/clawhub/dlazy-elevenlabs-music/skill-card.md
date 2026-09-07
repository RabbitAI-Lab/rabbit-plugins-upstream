## Description:

Generates 10-300 second original music from a natural-language prompt using the ElevenLabs music_v1 model through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate background music, advertising music, and short-video soundtracks from text prompts through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a pinned third-party npm CLI and the hosted dLazy service.

Mitigation: Review the dLazy CLI source or npm package before installation in sensitive environments, and prefer the pinned npx invocation when a persistent global install is unnecessary.

Risk: The skill requires a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Use a revocable API key, keep the local config file restricted to the OS user, and rotate or revoke the key if exposure is suspected.

Risk: Prompts and any local media paths supplied to the CLI are sent or uploaded to dLazy endpoints for generation.

Mitigation: Only submit prompts and local files that are intended for processing by the dLazy hosted API.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted output URLs, async task identifiers, or save generated assets to a local path when requested.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
