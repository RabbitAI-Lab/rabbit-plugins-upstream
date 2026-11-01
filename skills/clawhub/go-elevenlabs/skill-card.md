## Description:

Provides a typed Go client for calling the ElevenLabs REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and call the go-elevenlabs client when integrating an application with ElevenLabs REST endpoints such as text to speech, transcription, and voice management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text, audio, and voice samples sent in requests are processed by ElevenLabs.

Mitigation: Send only content approved for external processing and use a restricted API key.

Risk: Generation requests can spend account credits, and voice cloning or delete requests can change account data.

Mitigation: Review and confirm credit-spending or account-changing requests before sending them; clone only voices the user has rights to.

Risk: An exposed API key could allow unauthorized account use.

Mitigation: Load the key from an environment variable; never hardcode, commit, or log it.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-elevenlabs)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers the REST API; realtime WebSocket APIs are outside the documented client scope.]

## Skill Version(s):

0.6.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
