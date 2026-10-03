## Description:

Helps agents generate ElevenLabs eleven_v3 speech through dLazy with curated multilingual voices and voice-style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate narrated audio, dubbing, and character dialogue from text with selectable voices and speech controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts and selected options are sent to the third-party dLazy service, and generated audio is hosted there.

Mitigation: Avoid sending sensitive text without approval and review the service's data-handling terms before use.

Risk: Local media paths supplied to the CLI may be uploaded, and login can store an API key locally.

Mitigation: Review file paths before submission and protect the local CLI configuration and API key.

Risk: The documented sample response shows PNG image output for a text-to-speech skill.

Mitigation: Check actual response media types and expect audio rather than relying on the sample image fields.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Speech generation returns audio links or a task ID for asynchronous jobs; the documented image output example is inaccurate.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
