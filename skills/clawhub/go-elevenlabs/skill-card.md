## Description:

Guides Go developers in using an unofficial typed client for the ElevenLabs REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the Go client to a project and write code for ElevenLabs REST operations such as voice listing, text-to-speech, and transcription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial Go dependency requires trust before installation.

Mitigation: Review the dependency before adding it to a project.

Risk: Exposing the ElevenLabs API key could compromise the account.

Mitigation: Keep the key in an environment variable; do not commit or log it.

Risk: Generation can spend credits, while cloning and deletion change the account.

Mitigation: Run these operations only when intended, and clone only voices you have rights to.

Risk: Text, audio, and voice samples sent through the client go to ElevenLabs.

Mitigation: Review what data is sent before making API calls.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go ElevenLabs project](https://github.com/psyb0t/go-elevenlabs)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers REST calls; an ElevenLabs API key is required.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
