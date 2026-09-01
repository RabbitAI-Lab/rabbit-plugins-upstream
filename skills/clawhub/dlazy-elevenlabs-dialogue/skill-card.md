## Description:

Generates multi-voice ElevenLabs dialogue through the dLazy CLI, assigning voices per line and returning hosted audio-generation results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to generate character dialogue, podcast dialogue, and short skit audio with separate voices for each line. It is useful when an agent needs to call a hosted dialogue-generation service and optionally save or poll for generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends dialogue text, prompts, parameters, and any referenced media files to dLazy's hosted service.

Mitigation: Only pass content suitable for external processing, and review dLazy service terms and data-handling expectations before use.

Risk: The dLazy CLI stores an API key in local user configuration or reads it from the DLAZY_API_KEY environment variable.

Mitigation: Use standard secret-handling practices, restrict local config access, and rotate or revoke the API key from the dLazy dashboard when needed.

Risk: Installing a global npm CLI creates supply-chain exposure for the local environment.

Mitigation: Review the dLazy CLI source or npm package before installation, and prefer the pinned npx invocation for one-off use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown instructions with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an asynchronous task identifier for polling.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
