## Description:

Unofficial Go client for the ElevenLabs REST API, generated with oapi-codegen. `elevenlabs.NewClientWithResponses("https://api.elevenlabs.io", opts...)` from `github.com/psyb0t/go-elevenlabs` returns a `*elevenlabs.ClientWithResponses` with one typed `...WithResponse` method per endpoint (voices, text to speech, speech to text, sound effects, dubbing, user info and more). Auth is the `xi-api-key` header set through `elevenlabs.WithRequestEditorFn`; JSON replies decode into `JSON200`, and audio replies come back as raw bytes in `Body`. Use when Go code needs to call ElevenLabs or already imports go-elevenlabs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go code for calling ElevenLabs REST endpoints, including voice listing, speech generation, transcription, and other account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had partial coverage because some references could not be resolved.

Mitigation: Review the unresolved referenced material before installing, as recommended by the security guidance.

Risk: API credentials, generated audio requests, and account-changing operations can expose sensitive data, consume credits, or change account state.

Mitigation: Keep the API key in an environment variable and out of logs; make credit-consuming or account-changing calls only when requested, and clone only voices the user has rights to.

## Reference(s):

- [go-elevenlabs on GitHub](https://github.com/psyb0t/go-elevenlabs)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with Go code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.17.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
