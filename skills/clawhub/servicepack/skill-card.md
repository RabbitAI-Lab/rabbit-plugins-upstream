## Description:

servicepack guides agents in building Go service or daemon projects from the psyb0t/servicepack clone-and-own template, including service scaffolding, lifecycle hooks, dependency ordering, readiness behavior, retries, CLI commands, and build/test commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when starting or extending Go services that need concurrent long-running workers, dependency-aware startup, readiness gates, retries, graceful shutdown, and scaffolded service commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The make own workflow deliberately rewrites project files and reinitializes git in the cloned template.

Mitigation: Run it only inside a newly cloned servicepack directory before adding project work, and keep any important work outside that clone until ownership conversion is complete.

Risk: The final runtime surface comes from the user's services, including any listeners, databases, credentials, or environment variables they add.

Mitigation: Review generated and custom Go code, manage service-specific secrets separately, and run the documented build, test, vet, or lint commands before deployment.

## Reference(s):

- [Setup guide](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/servicepack)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Go code examples, shell commands, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go tooling and may propose changes to service files, command hooks, and project configuration.]

## Skill Version(s):

1.2.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
