## Description:

Creates an ElevenLabs Instant Voice Cloning voice from a clean audio sample for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can provide an authorized voice sample to create a custom voice for ElevenLabs text-to-speech. The skill invokes dLazy's hosted service through its CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples may contain personal or biometric data and are uploaded to dLazy's hosted service.

Mitigation: Use only samples you have permission to clone and are comfortable uploading; review dLazy's retention policies and charges before use.

Risk: The external CLI implementation and its claimed credential-file protections have not been verified.

Mitigation: Inspect the pinned @dlazy/cli package before installation and use a key you can rotate or revoke.

Risk: The included example and sample output format are inconsistent with voice cloning and may not describe the actual command result.

Mitigation: Check `dlazy elevenlabs-voice-clone -h` and confirm the supported options and returned result before use.

## Reference(s):

- [dLazy service website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [CLI repository link listed in skill metadata (release provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [API Calls, Audio]

**Output Format:** [CLI invocation and service result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an audio sample and a dLazy API key; the service result may be asynchronous.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
