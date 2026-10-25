## Description:

Guides Go developers using an unofficial client to integrate Mem0's hosted memory API, including typed operations, authentication, and response handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and work with the unofficial go-mem0 client for Mem0's hosted API, including memory search and management and related platform operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed in source code or logs.

Mitigation: Use a least-privilege key from the environment; never hardcode, commit, or log it.

Risk: Memory content and metadata are sent to an external hosted API.

Mitigation: Send only necessary data and scope filters to the intended user, agent, app, or run.

Risk: Delete and organization, project, or member changes can alter hosted resources.

Mitigation: Require explicit human review before these calls and limit them to authorized resources.

## Reference(s):

- [go-mem0 setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-mem0)
- [Library homepage listed in the skill](https://github.com/psyb0t/go-mem0)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-mem0)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for a Go integration; runtime API calls can change hosted resources.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
