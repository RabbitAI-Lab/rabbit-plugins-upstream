## Description:

An unofficial typed Go client for the Runway API, covering generation, task polling, and account resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate Runway generation and account operations into an existing Go project, including creating tasks and checking their status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, and other inputs sent through the client leave the local environment for Runway servers.

Mitigation: Send only data approved for Runway processing, and keep the API key in RUNWAYML_API_SECRET rather than hardcoding or logging it.

Risk: Generation calls spend organization credits, and cancellation or deletion calls can change Runway resources.

Mitigation: Start, cancel, or delete only when requested, and only for resources the user created or named.

Risk: Security review coverage is partial because two local path-like references in SKILL.md were not matched to bundled files.

Mitigation: Check whether the missing referenced files are required and review them before relying on the skill.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-runway)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
