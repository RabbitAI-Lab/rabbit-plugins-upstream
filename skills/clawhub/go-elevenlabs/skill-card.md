## Description:

Unofficial Go client for the ElevenLabs REST API, generated with oapi-codegen. `elevenlabs.NewClientWithResponses("https://api.elevenlabs.io", opts...)` from `github.com/psyb0t/go-elevenlabs` returns a `*elevenlabs.ClientWithResponses` with one typed `...WithResponse` method per endpoint (voices, text to speech, speech to text, sound effects, dubbing, user info and more). Auth is the `xi-api-key` header set through `elevenlabs.WithRequestEditorFn`; JSON replies decode into `JSON200`, and audio replies come back as raw bytes in `Body`. Use when Go code needs to call ElevenLabs or already imports go-elevenlabs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add or work with the typed go-elevenlabs Go client for ElevenLabs REST APIs, including voice listing, speech generation, transcription, and other supported operations. It guides installation, API-key configuration, request construction, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An ElevenLabs API key could be exposed in source code, logs, or request headers.

Mitigation: Read the key from an environment variable; do not hardcode, commit, log, or print request headers.

Risk: Text, audio, and voice samples sent in API requests are processed by ElevenLabs.

Mitigation: Send only content intended for that service and use the documented ElevenLabs API base URL.

Risk: Generation requests use account credits, while voice cloning and deletion can change the account.

Mitigation: Call generation or account-changing operations only when explicitly requested; clone only voices the user has rights to use.

Risk: The unofficial third-party dependency may require review before production use.

Mitigation: Review and pin the dependency before adopting it in production.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Project homepage](https://github.com/psyb0t/go-elevenlabs)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration instructions, Technical guidance]

**Output Format:** [Markdown guidance with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover client setup, authenticated REST calls, and response handling; API responses may contain JSON or audio bytes.]

## Skill Version(s):

0.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
