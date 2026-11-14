## Description:

Unofficial Go client for the ElevenLabs REST API, generated with oapi-codegen. `elevenlabs.NewClientWithResponses("https://api.elevenlabs.io", opts...)` from `github.com/psyb0t/go-elevenlabs` returns a `*elevenlabs.ClientWithResponses` with one typed `...WithResponse` method per endpoint (voices, text to speech, speech to text, sound effects, dubbing, user info and more). Auth is the `xi-api-key` header set through `elevenlabs.WithRequestEditorFn`; JSON replies decode into `JSON200`, and audio replies come back as raw bytes in `Body`. Use when Go code needs to call ElevenLabs or already imports go-elevenlabs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to add typed Go calls to the ElevenLabs REST API, including voice listing, speech generation, transcription, and other documented endpoints. It guides installation, authentication, request construction, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was incomplete because some references could not be resolved; a benign verdict does not guarantee zero risk.

Mitigation: Review the setup instructions and referenced materials before installing or using the skill.

Risk: Requests can send text, audio, or voice samples to ElevenLabs, consume account credits, or change an account through cloning and deletion operations.

Mitigation: Use only the intended ElevenLabs endpoint, confirm credit use and account changes before calling those operations, and clone only voices the user has rights to.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Project repository](https://github.com/psyb0t/go-elevenlabs)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown setup guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover typed REST requests and JSON or raw audio responses.]

## Skill Version(s):

0.15.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
