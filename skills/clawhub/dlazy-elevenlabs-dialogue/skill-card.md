## Description:

ElevenLabs eleven_v3 multi-voice dialogue: assign a different voice per line, up to 10 unique voices, and render the full conversation in one shot with support for audio tags such as [giggling] and [whispers].

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and automation agents use this skill to generate multi-speaker dialogue audio through the dLazy CLI and hosted API. It is suited for character dialogue, podcast segments, and short-form scripted conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text and any user-selected media files are sent to dLazy's hosted service.

Mitigation: Use the skill only for content approved for that service and review account, privacy, and data-handling requirements before automation.

Risk: Saved API credentials may persist in the local dLazy configuration file.

Mitigation: Prefer per-invocation credentials for sensitive environments, or protect and rotate credentials stored in ~/.dlazy/config.json.

Risk: The artifact contains stale image-oriented output and --prompt examples for an audio-dialogue skill.

Mitigation: Confirm the live CLI help and expected output type with dlazy elevenlabs-dialogue -h before building production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns hosted generation result metadata and can save generated assets locally when requested.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
