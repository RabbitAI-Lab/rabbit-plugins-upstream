## Description:

Provides Go developers with a typed client for calling the ElevenLabs REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate ElevenLabs REST API operations into Go projects, including voice, speech, transcription, and account requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security analysis is partial, with three SKILL.md references unresolved, so some behavior was not assessed.

Mitigation: Review the unresolved references and skill contents before installation, as advised by the security guidance.

Risk: Generation endpoints use account credits, while voice cloning and delete endpoints can change the account.

Mitigation: Call these endpoints only when the user requested the action, and clone only voices the user has rights to use.

Risk: Text, audio, and voice samples sent in requests are processed by ElevenLabs.

Mitigation: Send only content that is appropriate to share with ElevenLabs.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-elevenlabs repository](https://github.com/psyb0t/go-elevenlabs)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover API requests, authentication setup, and response handling.]

## Skill Version(s):

0.20.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
