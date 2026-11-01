## Description:

Clone a voice from reference audio and generate spoken audio for new text with Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to create spoken audio in a selected voice from a reference recording and new text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference audio and text are sent to dLazy, and local audio paths are uploaded for processing.

Mitigation: Use only recordings you have permission to clone; review dLazy's privacy terms before uploading sensitive audio.

Risk: Signing in saves an API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [dLazy CLI source repository (metadata reference; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio with JSON task and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task identifier before audio is available.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
