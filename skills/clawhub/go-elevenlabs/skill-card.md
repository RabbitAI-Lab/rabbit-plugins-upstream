## Description:

Provides guidance for using an unofficial typed Go client to call the ElevenLabs REST API from Go projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

External developers use the skill to install and integrate the typed Go client in projects that need ElevenLabs REST API features such as text to speech, transcription, or voice operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review is incomplete because three path-like references did not resolve to bundled files.

Mitigation: Review those references against the release contents before installing or relying on them.

Risk: Requests can send text, audio, or voice samples to ElevenLabs; generation can consume account credits, and voice cloning or deletion can change the account.

Mitigation: Protect the API key, send only approved content, and use credit-consuming or account-changing operations only when explicitly requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-elevenlabs source repository](https://github.com/psyb0t/go-elevenlabs)
- [go-elevenlabs on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Usage guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover Go client setup, authentication, requests, and response handling.]

## Skill Version(s):

0.20.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
