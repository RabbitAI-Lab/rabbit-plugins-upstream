## Description:

Provides setup and usage guidance for an unofficial typed Go client to the ElevenLabs REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with the ElevenLabs REST API for voice listing, text to speech, transcription, and related operations through typed client methods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner review is partial because three path-like references could not be matched to bundled artifacts.

Mitigation: Review the release contents and referenced paths before relying on the assessment.

Risk: ElevenLabs requests use an account API key; generation can consume credits, and voice cloning or deletion can change the account.

Mitigation: Load the key from an environment variable, never log or commit it, and perform credit-consuming or account-changing operations only when requested.

Risk: Text, audio, and voice samples sent in requests are processed by ElevenLabs.

Mitigation: Send only content the user has asked to process and is permitted to share.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Project homepage](https://github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text guidance and code examples; API response content depends on the requested operation.]

## Skill Version(s):

0.12.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
