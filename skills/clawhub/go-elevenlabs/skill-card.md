## Description:

Guides Go developers in using a typed client to call the ElevenLabs REST API for voice, speech, transcription, dubbing, and related operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add or update Go code that calls ElevenLabs REST endpoints, handles JSON or audio responses, and configures API authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because three path-like references in the skill could not be matched to bundled artifacts.

Mitigation: Review the unresolved references before relying on guidance that depends on them.

Risk: API keys and submitted text, audio, or voice samples are sent to ElevenLabs when requests are made.

Mitigation: Read the API key from an environment variable, do not commit or log it, and send only content intended for processing by ElevenLabs.

Risk: Generation can use account credits, and voice cloning or deletion can change the account.

Mitigation: Make these calls only when requested, confirm the expected credit use, and clone only voices the user has rights to use.

## Reference(s):

- [Setup and API usage](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Project homepage](https://github.com/psyb0t/go-elevenlabs)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go source code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Code may call the ElevenLabs REST API; response data can be JSON or audio bytes.]

## Skill Version(s):

0.19.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
