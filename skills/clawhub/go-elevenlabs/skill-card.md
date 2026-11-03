## Description:

Provides typed Go guidance for calling the ElevenLabs REST API with the go-elevenlabs client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to install and integrate the typed go-elevenlabs client, configure API authentication, and call ElevenLabs REST endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key could be exposed through source code or logs.

Mitigation: Read the key from an environment variable; never hardcode, commit, or log it, and never print request headers.

Risk: Requests send text, audio, or voice samples to ElevenLabs, and generation uses account credits.

Mitigation: Send only content intended for ElevenLabs to process and review requests that spend credits.

Risk: Voice cloning and delete operations can change account resources.

Mitigation: Call these operations only when explicitly requested, and clone only voices the user has rights to.

Risk: The unofficial Go dependency's downloaded code has not been fully audited.

Mitigation: Pin the dependency to a reviewed version.

## Reference(s):

- [go-elevenlabs setup and reference](references/setup.md)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Go integration examples, dependency installation commands, and API request guidance.]

## Skill Version(s):

0.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
