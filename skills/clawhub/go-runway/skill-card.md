## Description:

Provides Go developers with a typed client for calling Runway's generation and account APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and call the go-runway client for Runway generation, task, and organization APIs. It helps them configure authentication and interpret typed request and response values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review coverage is partial because two references in SKILL.md could not be matched to bundled files.

Mitigation: Review the unresolved references and the skill before installing.

Risk: Runway requests send prompts and other inputs to Runway, while generation and deletion operations can affect credits or account resources.

Mitigation: Protect the API key, use only approved inputs, and run chargeable or destructive operations only when requested and on the intended resources.

## Reference(s):

- [go-runway setup and reference](artifact/references/setup.md)
- [go-runway source repository](https://github.com/psyb0t/go-runway)
- [go-runway package documentation](https://pkg.go.dev/github.com/psyb0t/go-runway)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use a Go project and Runway API key.]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
