## Description:

Guides Go developers in using the unofficial go-elevenlabs client to call ElevenLabs REST API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to install and integrate the go-elevenlabs client, then call ElevenLabs REST endpoints such as voice listing, speech generation, and transcription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed or sent to an untrusted destination.

Mitigation: Use an appropriately restricted API key, keep it out of source and logs, and send requests only to a trusted API destination.

Risk: Text, audio, and voice samples sent in requests are processed by ElevenLabs, and generation uses account credits.

Mitigation: Review the data being sent and expected credit use before making API calls.

Risk: Voice cloning and delete operations can change the account.

Mitigation: Perform account-changing actions only when explicitly requested, and clone only voices the user has rights to use.

Risk: The external Go dependency was outside the bundled artifacts.

Mitigation: Review and pin the dependency before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Project homepage](https://github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover Go client setup, API calls, and response handling.]

## Skill Version(s):

0.9.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
