## Description:

Creates an ElevenLabs Instant Voice Clone from a clean audio sample for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to submit a clean voice sample to dLazy's ElevenLabs voice-cloning service and create a custom voice for ElevenLabs text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reported a mismatch between the advertised voice-cloning purpose and the login and authentication commands it reviewed; its analysis was partial.

Mitigation: Before providing credentials or media, check that the CLI behavior matches the advertised purpose and review the CLI and its data handling.

## Reference(s):

- [dLazy CLI repository (referenced in skill documentation)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON API results, Voice-cloning result]

**Output Format:** [CLI invocation with a JSON result envelope and generated resource URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio sample is supplied by URL or local path; asynchronous invocation can return a task identifier.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
