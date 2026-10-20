## Description:

Guides Go developers in using an unofficial typed client for Together AI APIs, including authentication, requests, and response handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Together AI into Go applications, find generated client methods, authenticate requests, and handle API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing a Together AI API key through source code, logs, or request headers.

Mitigation: Read the key from an environment variable and do not commit or log it.

Risk: Prompts and uploaded files leave the local environment for Together AI processing.

Mitigation: Review sensitive content before sending requests to Together AI.

Risk: Fine-tuning, endpoints, and clusters may incur charges; deletion can remove remote data.

Mitigation: Review such operations and require user authorization before running them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-togetherai)
- [Go client documentation](https://pkg.go.dev/github.com/psyb0t/go-togetherai)
- [Setup and usage reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover client setup, API requests, and response handling.]

## Skill Version(s):

0.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
