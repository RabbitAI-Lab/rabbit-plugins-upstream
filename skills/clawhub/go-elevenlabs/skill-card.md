## Description:

Provides Go developers with typed methods for calling the ElevenLabs REST API, including voice, speech, dubbing, and account endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add and call the go-elevenlabs client in a Go project. It guides installation, authentication, endpoint selection, and handling JSON or audio responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial because three local path-like references could not be resolved.

Mitigation: Review the unresolved references and treat the clean verdict as limited to the two Markdown files inspected.

Risk: API keys, text, audio, and voice samples may be exposed through requests; generation uses account credits, while voice cloning and deletion change the account.

Mitigation: Keep API keys in environment variables and out of source or logs, send only content you are authorized to share, and make credit-consuming or account-changing calls only when requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-elevenlabs)
- [Project homepage](https://github.com/psyb0t/go-elevenlabs)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover client setup, API requests, authentication, and response handling.]

## Skill Version(s):

0.13.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
