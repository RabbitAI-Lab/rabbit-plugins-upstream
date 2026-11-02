## Description:

Creates a custom ElevenLabs voice by uploading a clean voice sample through dLazy's Instant Voice Cloning workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to create a custom voice for ElevenLabs text-to-speech from a clean audio sample. Use only audio you have permission to clone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples may contain identifiable audio and are uploaded to dLazy-hosted storage.

Mitigation: Upload only audio you have permission to clone and are comfortable sharing with dLazy.

Risk: The CLI stores an API key in local configuration, and service usage may incur charges.

Mitigation: Protect or rotate the key, review service charges, and check command help because the examples contain inconsistencies.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [JSON result from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a hosted output URL or, for asynchronous runs, a task identifier and status.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
