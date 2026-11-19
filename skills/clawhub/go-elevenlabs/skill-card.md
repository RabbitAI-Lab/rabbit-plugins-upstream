## Description:

A typed Go client for the ElevenLabs REST API, covering voice, speech, transcription, dubbing, and account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use the skill to integrate Go applications with the ElevenLabs REST API for voice discovery, speech generation, transcription, and related account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had partial coverage because three local path-like references were unresolved.

Mitigation: Resolve and inspect the referenced paths before relying on the skill.

Risk: Text, audio, and voice samples sent through the client are processed by ElevenLabs.

Mitigation: Send only content intended for processing by ElevenLabs.

Risk: Generation endpoints use account credits, while voice cloning and delete endpoints can change account state.

Mitigation: Confirm the requested operation before calling it, and clone only voices the user has rights to use.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Project page](https://github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance, Technical guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover typed API calls, authentication setup, and response handling.]

## Skill Version(s):

0.18.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
