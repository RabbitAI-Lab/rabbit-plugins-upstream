## Description:

A typed Go client skill for calling ElevenLabs REST API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and call the typed Go client for the ElevenLabs REST API, including voice listing, speech generation, transcription, and other supported endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if hardcoded, committed, logged, or printed.

Mitigation: Read the API key from an environment variable and do not hardcode, commit, log, or print it.

Risk: Text, audio, and voice samples sent to the API are processed by ElevenLabs.

Mitigation: Send only the text, audio, or voice samples intended for that service.

Risk: Generation uses account credits, while voice cloning and deletion change the account.

Mitigation: Use generation, cloning, and deletion only when explicitly requested; clone only voices the user has rights to.

## Reference(s):

- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-elevenlabs)
- [Project homepage](https://github.com/psyb0t/go-elevenlabs)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover typed REST calls and JSON or audio response handling.]

## Skill Version(s):

0.6.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
