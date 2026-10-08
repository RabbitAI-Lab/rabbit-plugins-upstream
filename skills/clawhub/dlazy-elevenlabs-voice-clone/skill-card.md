## Description:

Guides users in cloning a custom voice from a clean audio sample for ElevenLabs text-to-speech through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to submit a voice sample through dLazy and create a custom voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples and request metadata are sent to dLazy's hosted service, and the CLI requires a dLazy API key.

Mitigation: Send only voice samples you are comfortable sharing with dLazy and protect or rotate the API key as needed.

Risk: The documented examples and output schema appear inconsistent with voice cloning.

Mitigation: Check the installed CLI help and confirm its actual parameters and results before relying on the examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return JSON with a hosted result URL or an asynchronous task ID.]

## Skill Version(s):

1.3.25 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
