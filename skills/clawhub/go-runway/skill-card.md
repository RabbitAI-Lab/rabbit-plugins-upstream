## Description:

Unofficial Go client for the Runway API, generated with oapi-codegen from Runway's OpenAPI document, with typed methods for generation, account, and task operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add the go-runway client to a Go project and call Runway generation or account APIs with typed request and response handling. It also helps developers poll tasks and interpret API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, and other inputs sent through the client leave the local machine for Runway, and generation endpoints can spend organization credits.

Mitigation: Send only data approved for Runway and confirm the credit impact before starting a generation.

Risk: An API key could be exposed if it is hardcoded, committed, or logged.

Mitigation: Read the key from RUNWAYML_API_SECRET, keep it out of source control and logs, and do not print request headers.

Risk: The security scan was partial because two references could not be resolved, so some context was unavailable to scanners.

Mitigation: Review the unresolved references and repeat the security review when complete scanner context is needed.

## Reference(s):

- [Setup and API usage reference](references/setup.md)
- [go-runway package documentation](https://pkg.go.dev/github.com/psyb0t/go-runway)
- [Project homepage](https://github.com/psyb0t/go-runway)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-runway)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the typed Runway client; task polling is performed by the caller.]

## Skill Version(s):

0.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
