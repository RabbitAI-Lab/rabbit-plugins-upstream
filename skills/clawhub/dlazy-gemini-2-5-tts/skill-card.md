## Description:

Generate multilingual speech audio from text using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn text prompts into multilingual speech audio, choosing a supported language and voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and submitted media are sent to dLazy's hosted service, and local media files may be uploaded for processing.

Mitigation: Submit only content approved for cloud processing; review the service terms and data-retention practices before sending sensitive material.

Risk: The CLI stores an API key locally, and this review does not establish the external package's safety or the service's data-retention practices.

Mitigation: Protect the local configuration file, review the pinned CLI package before installing, and rotate or revoke the key if needed. Confirm available service credits before generating audio.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio]

**Output Format:** [Generated speech audio, returned through a hosted output URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return a task ID for asynchronous generation.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
