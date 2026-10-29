## Description:

Provides typed Go guidance for calling the ElevenLabs REST API with the go-elevenlabs client, including authentication and request and response handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add or use a typed Go client for ElevenLabs REST operations, including voice listing, speech generation, transcription, dubbing, and account information. It guides setup, authentication, request construction, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send text, audio, or voice samples to ElevenLabs; generation can use account credits, and cloning or deletion changes the account.

Mitigation: Protect the API key, send only content you may share, and request paid generation, cloning, or deletion explicitly.

Risk: The skill relies on a third-party Go dependency.

Mitigation: Review and pin the dependency version.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-elevenlabs source repository](https://github.com/psyb0t/go-elevenlabs)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples require an ElevenLabs API key; generation may use account credits, and cloning or deletion changes account data.]

## Skill Version(s):

0.6.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
