## Description:

Unofficial Go client for the ElevenLabs REST API, generated with oapi-codegen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers can use this skill to integrate the go-elevenlabs client into a project and call ElevenLabs REST endpoints for voices, speech generation and transcription, sound effects, dubbing, and account information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An ElevenLabs API key could be exposed if placed in source code, committed, or logged.

Mitigation: Read the key from an environment variable, such as ELEVENLABS_API_KEY, and do not commit it or print request headers.

Risk: Requests may send text, audio, or voice samples to ElevenLabs; generation uses account credits, and voice cloning or deletion changes the account.

Mitigation: Use these operations only when requested, and clone only voices the user has rights to.

Risk: The security review was benign with medium confidence, but some references could not be resolved.

Mitigation: Review unresolved references and confirm relevant API behavior before relying on it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-elevenlabs)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [go-elevenlabs project](https://github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Go code and concise Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples configure a Go API client; API calls can send text or audio to ElevenLabs and use account credits.]

## Skill Version(s):

0.10.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
