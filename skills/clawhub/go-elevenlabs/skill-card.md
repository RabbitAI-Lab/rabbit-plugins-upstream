## Description:

Helps Go developers call ElevenLabs REST endpoints through typed client methods and handle JSON and audio responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the go-elevenlabs client to Go projects and call ElevenLabs REST APIs for voice listing, speech generation, transcription, dubbing, and account operations. It applies to Go projects and does not cover realtime WebSocket APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because three references in SKILL.md were unresolved.

Mitigation: Review the unresolved references and verify their targets before installation.

Risk: Requests send text, audio, or voice samples to ElevenLabs; generation uses account credits, and voice cloning or deletion changes the account.

Mitigation: Protect the API key, use the intended base URL, perform credit-using or account-changing operations only when requested, and clone only voices the user has rights to.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-elevenlabs on GitHub](https://github.com/psyb0t/go-elevenlabs)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples; API responses may be JSON or audio bytes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Response content depends on the requested endpoint; audio is returned as bytes.]

## Skill Version(s):

0.11.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
