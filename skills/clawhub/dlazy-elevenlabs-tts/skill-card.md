## Description:

Helps agents generate multilingual speech from text using ElevenLabs eleven_v3 through the dLazy CLI, with voice and delivery controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text into speech for dubbing, audiobooks, and character dialogue using selectable voices and speech settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts are sent to the dLazy hosted API.

Mitigation: Review prompts for sensitive content before submitting them to the third-party service.

Risk: The dLazy API key is stored locally or provided via an environment variable.

Mitigation: Protect the key and restrict access to the local CLI configuration.

Risk: The documented output example shows an image rather than audio.

Mitigation: Check actual audio output type and format before depending on generated artifacts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown guidance and CLI JSON responses with generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs may return a task ID; verify the actual audio output before automating downstream use.]

## Skill Version(s):

1.3.32 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
