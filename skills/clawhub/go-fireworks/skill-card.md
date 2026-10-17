## Description:

Guides developers in using an unofficial typed Go client for Fireworks AI inference and resource-management APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add authenticated Fireworks AI API calls for inference, model discovery, and management of deployments, datasets, and jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials may be exposed in code, logs, or commits.

Mitigation: Keep FIREWORKS_API_KEY in the environment; never print, hardcode, or commit the key or request headers.

Risk: API calls can upload data, incur charges, change API keys, or delete resources.

Mitigation: Require explicit approval before uploads, paid jobs, key management, or deletions; limit actions to resources owned by the task.

## Reference(s):

- [go-fireworks ClawHub release](https://clawhub.ai/psyb0t/skills/go-fireworks)
- [go-fireworks project homepage](https://github.com/psyb0t/go-fireworks)
- [Setup and usage reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for authentication, base URLs, and response handling.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
