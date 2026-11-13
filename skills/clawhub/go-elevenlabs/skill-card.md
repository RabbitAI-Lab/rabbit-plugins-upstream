## Description:

Provides Go developers with a typed client for calling ElevenLabs REST API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use the skill to integrate ElevenLabs REST API features, including voice listing, speech generation, transcription, and account queries, into a Go project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed ElevenLabs API key could allow unauthorized account access.

Mitigation: Read the key from an environment variable; do not hardcode, commit, or log it, and do not print request headers.

Risk: Requests send text, audio, and voice samples to ElevenLabs for processing.

Mitigation: Send only content intended for processing by ElevenLabs.

Risk: Generation can use account credits, while voice cloning and delete operations change the account.

Mitigation: Call credit-consuming or account-changing endpoints only when the user requests the action, and clone only voices the user has rights to use.

Risk: The security scan marked its analysis incomplete because some path-like references could not be resolved.

Mitigation: Review the skill instructions and unresolved references before installing.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [go-elevenlabs project](https://github.com/psyb0t/go-elevenlabs)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed REST API calls with JSON responses or raw audio bytes.]

## Skill Version(s):

0.14.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
