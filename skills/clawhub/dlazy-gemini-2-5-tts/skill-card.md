## Description:

Generate multilingual, natural-sounding audio from text using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn text into Chinese or English speech with Gemini 2.5 TTS and choose a voice. It provides CLI usage and authentication guidance for the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had partial coverage and flagged the API-key login/setup flow for confirmation.

Mitigation: Review the CLI install source and confirm the dLazy API-key flow is expected before installing or using the skill.

Risk: Text prompts are sent to the dLazy hosted API for speech generation.

Mitigation: Avoid sending sensitive text unless your organization permits processing it through that service.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio]

**Output Format:** [Generated audio file or hosted audio URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio is returned through the dLazy service; prompts are sent to its hosted API.]

## Skill Version(s):

1.3.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
