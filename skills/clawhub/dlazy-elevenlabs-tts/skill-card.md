## Description:

Generates multilingual speech from text using ElevenLabs eleven_v3 through dLazy, with voice and delivery controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to create voiceovers, audiobooks, and character dialogue from text with a choice of multilingual voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts and explicitly supplied media are sent to the external dLazy service.

Mitigation: Share only content you are comfortable sending to dLazy.

Risk: The CLI may store a dLazy API key in local configuration.

Mitigation: Protect the local key or use the DLAZY_API_KEY environment variable instead.

Risk: The documented PNG output example is inconsistent with text-to-speech output.

Mitigation: Check the returned audio format before using or sharing the result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and links to generated speech]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide a local saved result or an asynchronous task ID; verify the actual audio format.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
