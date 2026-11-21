## Description:

Provides Go developers with a typed client for calling the ElevenLabs REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to integrate Go applications with ElevenLabs REST endpoints for voice, speech, dubbing, and account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests can send text, audio, or voice samples to ElevenLabs for processing.

Mitigation: Send only content that is approved for external processing and use the documented ElevenLabs base URL.

Risk: The API key could be exposed if placed in source code, committed, or logged.

Mitigation: Read the key from an environment variable, keep it out of source control, and do not log request headers.

Risk: Generation calls consume account credits, while voice cloning and deletion calls can change the account.

Mitigation: Make these calls only when requested, and clone only voices the user has rights to use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-elevenlabs)
- [Project homepage](https://github.com/psyb0t/go-elevenlabs)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for installing and using the typed REST client, including authentication and response handling.]

## Skill Version(s):

0.20.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
