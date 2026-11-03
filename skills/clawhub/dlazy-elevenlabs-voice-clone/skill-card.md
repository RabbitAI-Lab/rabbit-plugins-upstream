## Description:

ElevenLabs Instant Voice Cloning (IVC). Upload a clean voice sample to clone a custom voice usable with ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Users can provide a clean audio sample to create an ElevenLabs Instant Voice Clone for use with text-to-speech. Use only recordings they have permission to clone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples can be used to clone a person's voice without their permission.

Mitigation: Upload only audio you have permission to use for voice cloning.

Risk: Audio samples are uploaded to dLazy storage, and authentication saves an API key in local CLI configuration.

Mitigation: Review dLazy's service terms before uploading, protect the local configuration, and rotate or revoke the API key if needed.

Risk: Installing the CLI adds an external package that was not covered by the supplied security review.

Mitigation: Review the pinned CLI package before installing or running it.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [API Calls, JSON, URLs]

**Output Format:** [JSON response with generation status and hosted output URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task identifier for asynchronous generation; requires a dLazy API key and uses service credits.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
