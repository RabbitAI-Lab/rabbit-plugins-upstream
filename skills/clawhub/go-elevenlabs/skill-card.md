## Description:

Guides Go developers in integrating the ElevenLabs REST API with the go-elevenlabs client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and use a typed client for ElevenLabs REST API operations, including speech generation, transcription, and voice management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API key exposure

Mitigation: Read the key from an environment variable; never hardcode, commit, or log it.

Risk: Text, audio, or voice samples may be sent to ElevenLabs for processing.

Mitigation: Send only content the user intends ElevenLabs to process.

Risk: Generation may use account credits, while cloning and deletion change account state.

Mitigation: Call these operations only at the user's request, and review and pin the dependency version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-elevenlabs)
- [Setup and reference](references/setup.md)
- [Project homepage listed in skill frontmatter](https://github.com/psyb0t/go-elevenlabs)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance; the skill does not generate project files.]

## Skill Version(s):

0.4.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
