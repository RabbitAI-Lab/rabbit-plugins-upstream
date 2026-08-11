## Description:

ElevenLabs eleven_v3 multi-voice dialogue renders full conversations by assigning different voices to dialogue lines, with support for audio tags such as [giggling] and [whispers].

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate multi-speaker dialogue audio for character dialogue, podcasts, and short skits through the dLazy hosted CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue prompts and explicitly supplied media files are sent to dLazy cloud endpoints for processing.

Mitigation: Avoid submitting sensitive content unless the user accepts dLazy processing for that data.

Risk: A saved dLazy API key may persist in the local CLI configuration.

Mitigation: Use a trusted machine for saved login, prefer DLAZY_API_KEY for temporary use on shared systems, and rotate or revoke the organization key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, text, files]

**Output Format:** [Markdown guidance with CLI commands and JSON result references to hosted output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous runs may return a generateId for later polling.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
