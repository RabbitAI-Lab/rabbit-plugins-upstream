## Description:

Guides Go developers in using an unofficial typed client for the ElevenLabs REST API to work with voices, speech, audio, and account endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and integrate a typed ElevenLabs REST client for voice listing, speech generation, transcription, and related API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted third-party Go module could introduce unwanted code.

Mitigation: Confirm you trust the module before adding it to your project.

Risk: API keys and submitted text or audio may be exposed to unintended recipients.

Mitigation: Keep the API key in an environment variable, avoid logging headers, and send only content intended for ElevenLabs.

Risk: Generation may consume account credits; cloning and deletion may change account data.

Mitigation: Use these endpoints only when explicitly requested, and clone only voices you have rights to use.

## Reference(s):

- [go-elevenlabs setup and reference](references/setup.md)
- [go-elevenlabs package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Go client homepage](https://github.com/psyb0t/go-elevenlabs)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [REST API guidance only; requires Go and an ElevenLabs API key.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
