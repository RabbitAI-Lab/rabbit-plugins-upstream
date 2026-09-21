## Description:

Generates music with or without vocals using the Suno music generation model, supporting inspiration mode for automatic lyrics and custom mode for manual lyrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate music from prompts through the dLazy CLI, including lyrical, vocal, and instrumental variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected parameters, and any explicitly provided local media paths are sent to dLazy services for processing.

Mitigation: Use the skill only with content appropriate for dLazy processing, and avoid sending sensitive prompts or media unless the service terms and data handling are acceptable.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Protect the local configuration file, use per-invocation environment variables where appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact's documented sample output shows an image/PNG result even though the command is for music generation.

Mitigation: Verify the actual returned output type and URL before building downstream automation around generated assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON result metadata with generated media URLs or saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous runs can return a task identifier for later polling.]

## Skill Version(s):

1.3.17 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
