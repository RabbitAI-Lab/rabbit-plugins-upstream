## Description:

Guides Go developers in using a typed client for the ElevenLabs REST API to work with voices, speech, and other supported endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate ElevenLabs REST operations, including listing voices, generating speech, and transcribing audio, into their applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An ElevenLabs API key could be exposed through source code, logs, or request headers.

Mitigation: Read the key from an environment variable; do not commit, log, or print it or request headers.

Risk: Generation may use account credits, while voice cloning and deletion can change the account.

Mitigation: Confirm the user's intent before these operations and clone only voices they have rights to use.

Risk: Text, audio, and voice samples sent to the API are processed by ElevenLabs.

Mitigation: Check that the user authorizes sending the content before making API requests.

## Reference(s):

- [Skill setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Go client homepage](https://github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for typed REST requests and response handling; does not support realtime WebSocket APIs.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
