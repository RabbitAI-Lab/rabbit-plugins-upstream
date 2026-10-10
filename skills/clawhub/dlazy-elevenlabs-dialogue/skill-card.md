## Description:

Helps agents generate multi-voice dialogue audio from scripted lines using the dLazy-hosted ElevenLabs dialogue service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to assign voices to dialogue lines and generate audio for character scenes, podcasts, and short skits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI adds third-party software to the local environment.

Mitigation: Review the dLazy CLI package before installation; use the documented pinned npx invocation if a persistent global install is unnecessary.

Risk: Submitted prompts, parameters, and intentionally provided files may be sent to the hosted dLazy service.

Mitigation: Check inputs for sensitive content and share only files intended for the hosted service.

Risk: The documented example command and output contain mistakes and may not match the dialogue command's behavior.

Mitigation: Check the CLI help and actual response before relying on the examples or processing generated assets.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown instructions and CLI JSON results containing generated asset links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation and optional saving of the resulting audio asset.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
