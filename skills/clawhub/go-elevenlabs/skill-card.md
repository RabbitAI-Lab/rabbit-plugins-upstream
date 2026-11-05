## Description:

Provides setup and usage guidance for calling the ElevenLabs REST API from Go with the unofficial go-elevenlabs client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with ElevenLabs REST endpoints, including voice listing, text-to-speech, and speech-to-text operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An ElevenLabs API key could be exposed through source control or logs.

Mitigation: Read a restricted API key from an environment variable, and do not hardcode it, commit it, log it, or print request headers.

Risk: Text, audio, and voice samples sent in requests are processed by ElevenLabs.

Mitigation: Send only content the user intends to submit to ElevenLabs and ensure the user understands where it is processed.

Risk: Generation endpoints can consume account credits, while cloning and deletion endpoints change the account.

Mitigation: Call chargeable or account-changing operations only when the user requested them; clone only voices the user has rights to use.

Risk: The unofficial Go dependency is downloaded separately and is outside the bundled-file security review.

Mitigation: Review and pin the dependency version before using it.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-elevenlabs source repository](https://github.com/psyb0t/go-elevenlabs)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover Go client setup, REST requests, authentication, and response handling.]

## Skill Version(s):

0.8.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
