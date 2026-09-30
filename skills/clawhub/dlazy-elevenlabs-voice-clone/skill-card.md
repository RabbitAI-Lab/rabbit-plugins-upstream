## Description:

Helps agents clone a voice from a clean audio sample for use with ElevenLabs text-to-speech through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to submit an authorized voice sample and create a custom voice for ElevenLabs text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloning a voice without the speaker's permission may enable impersonation.

Mitigation: Only submit recordings you are authorized to clone, with the speaker's consent.

Risk: Voice samples and request parameters are sent to dLazy-hosted services.

Mitigation: Review data-sharing implications before uploading sensitive recordings.

Risk: The documented example and sample output appear to describe a different modality.

Mitigation: Check the installed CLI's voice-cloning help and actual response before relying on the examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown instructions and CLI JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice-cloning results may be returned asynchronously as a task ID.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; skill files state 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
