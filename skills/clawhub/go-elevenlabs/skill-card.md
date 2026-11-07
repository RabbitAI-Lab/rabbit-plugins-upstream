## Description:

Unofficial Go client for the ElevenLabs REST API, generated with oapi-codegen. `elevenlabs.NewClientWithResponses("https://api.elevenlabs.io", opts...)` from `github.com/psyb0t/go-elevenlabs` returns a `*elevenlabs.ClientWithResponses` with one typed `...WithResponse` method per endpoint (voices, text to speech, speech to text, sound effects, dubbing, user info and more). Auth is the `xi-api-key` header set through `elevenlabs.WithRequestEditorFn`; JSON replies decode into `JSON200`, and audio replies come back as raw bytes in `Body`. Use when Go code needs to call ElevenLabs or already imports go-elevenlabs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed calls to ElevenLabs REST API operations, including speech generation, transcription, and voice management, in a Go project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The clean scan had medium confidence because reference resolution was incomplete.

Mitigation: Review the referenced setup material and any unresolved references before installation; the scan verdict does not establish that the skill is risk-free.

Risk: Requests send text, audio, or voice samples to ElevenLabs; generation can use account credits, and voice cloning or deletion can change the account.

Mitigation: Send only content intended for the service, keep the API key in an environment variable, and use credit-consuming or account-changing operations only when requested.

## Reference(s):

- [Setup and API usage](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Go client source repository](https://github.com/psyb0t/go-elevenlabs)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.10.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
