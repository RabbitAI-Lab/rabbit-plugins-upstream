## Description:

Provides guidance for using a typed Go client to call the ElevenLabs REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add or work with Go code that calls ElevenLabs REST endpoints, including text-to-speech and transcription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests may send text, audio, or voice samples to ElevenLabs and generation calls consume account credits.

Mitigation: Confirm the content is appropriate to share, monitor usage, and store a restricted API key in an environment variable.

Risk: Voice cloning and deletion operations change account resources.

Mitigation: Make these calls only on explicit user request, and clone only voices the user has rights to use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Project repository](https://github.com/psyb0t/go-elevenlabs)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and instructions for integrating the Go client into the current project.]

## Skill Version(s):

0.6.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
