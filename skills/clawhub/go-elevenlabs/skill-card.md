## Description:

Provides Go integration guidance for the unofficial go-elevenlabs client, including authentication and typed calls to ElevenLabs REST endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate the unofficial go-elevenlabs client into a project and call ElevenLabs REST endpoints for text-to-speech, transcription, and other voice services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration uses a third-party Go dependency.

Mitigation: Review and pin the dependency before production use.

Risk: The API key authenticates requests to ElevenLabs.

Mitigation: Keep the key private and avoid exposing it in source code or logs.

Risk: Text, audio, and voice samples sent in requests are processed by ElevenLabs.

Mitigation: Send only content intended for ElevenLabs to process.

Risk: Generation uses account credits, while voice cloning and deletion change account state.

Mitigation: Run generation only with awareness of credit use, and clone or delete only when explicitly requested; clone only voices the user has rights to.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-elevenlabs source repository](https://github.com/psyb0t/go-elevenlabs)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples configure the API key and make typed REST calls; responses may contain JSON or audio bytes.]

## Skill Version(s):

0.6.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
