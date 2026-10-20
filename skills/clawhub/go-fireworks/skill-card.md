## Description:

Guides Go developers in using an unofficial typed client for Fireworks AI inference and account-management APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the Fireworks AI client, find typed API methods, and handle inference or account-management responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Fireworks AI API key could be exposed in code, logs, or request headers.

Mitigation: Load the key from a secret environment variable; do not commit or log it or print request headers.

Risk: Management calls can delete resources or incur charges.

Mitigation: Review generated calls and run create, delete, fine-tuning, deployment, or batch operations only when the user requests them for authorized resources.

Risk: Prompts, datasets, or model files sent through the client reach Fireworks AI.

Mitigation: Check the destination base URL and confirm the data is appropriate to send before making requests.

## Reference(s):

- [go-fireworks on ClawHub](https://clawhub.ai/psyb0t/skills/go-fireworks)
- [Setup and API reference](references/setup.md)
- [go-fireworks package documentation](https://pkg.go.dev/github.com/psyb0t/go-fireworks)
- [go-fireworks project homepage](https://github.com/psyb0t/go-fireworks)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover authentication, separate API base URLs, and response handling.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
