## Description:

Provides a typed Go client for Runway's API, including methods for generation tasks, task polling, and account endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use the skill to integrate Runway generation and account APIs into Go projects, then poll or cancel tasks through typed methods. Requests send supplied prompts or media to Runway, and generation endpoints spend organization credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if hardcoded, committed, or logged.

Mitigation: Read the API key from RUNWAYML_API_SECRET; do not commit it or print request headers.

Risk: Prompts and media sent through the client leave the machine for Runway, and generation requests spend organization credits.

Mitigation: Send only inputs intended for Runway and confirm generation calls are authorized and budgeted.

Risk: The client is unofficial and generated methods or types may need review before production use.

Mitigation: Review and pin the dependency version, then check generated methods against current Runway documentation.

## Reference(s):

- [Setup and API usage](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-runway)
- [Source repository](https://github.com/psyb0t/go-runway)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-runway)

## Skill Output:

**Output Type(s):** [Go code, API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
