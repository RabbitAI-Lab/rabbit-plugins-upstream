## Description:

Creates an ElevenLabs Instant Voice Clone from a clean voice sample for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to create an ElevenLabs voice clone from a clean audio sample for text-to-speech projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are uploaded to dLazy's hosted media service.

Mitigation: Use only samples you have permission to clone and are comfortable uploading.

Risk: Authentication stores a reusable API key in local CLI configuration.

Mitigation: Prefer device-code login, keep the key private, and rotate or revoke it from the account dashboard if needed.

Risk: Voice-cloning requests may consume paid credits.

Mitigation: Use the CLI dry-run option to review the payload and cost estimate before submitting.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands]

**Output Format:** [Hosted voice asset reference with JSON task or result metadata, invoked through the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts an audio URL or local path, voice name, and description; supports a dry run, asynchronous return, and configurable timeout.]

## Skill Version(s):

1.3.34 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
