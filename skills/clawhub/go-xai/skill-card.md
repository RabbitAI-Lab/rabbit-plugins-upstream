## Description:

Guides Go developers in using the unofficial go-xai client to call the xAI API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the go-xai client to Go projects and implement xAI API calls for chat, embeddings, media generation, and other supported endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed in code or logs.

Mitigation: Read the API key from an environment variable and avoid logging request headers.

Risk: Requests send data to xAI and may incur charges.

Mitigation: Review the data and intended API calls before sending requests.

Risk: Uploads, deletes, and public file URLs can change account state or expose content.

Mitigation: Run account-changing calls only when requested and only for specified resources.

## Reference(s):

- [go-xai on ClawHub](https://clawhub.ai/psyb0t/skills/go-xai)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-xai)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
