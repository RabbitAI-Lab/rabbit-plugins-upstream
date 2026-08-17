## Description:

servicepack helps developers build Go services from the psyb0t/servicepack clone-and-own template, with guidance for service scaffolding, concurrent service management, dependency and readiness behavior, retries, CLI commands, logging, configuration, and graceful shutdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when starting or extending a Go service template that runs related services together locally, then can be built as one binary or split into microservices. It is especially relevant when they need dependency-ordered startup, readiness gates, retries, service-specific CLI commands, structured logging, configuration, and graceful shutdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented make own initialization step rewrites the module, removes existing Git history in the clone, and reinitializes the repository.

Mitigation: Use the skill as a fresh project template, and run make own only in a fresh clone or after committing or backing up local work.

Risk: The skill guides edits around framework-owned files that can be overwritten by servicepack update workflows.

Mitigation: Keep custom behavior in service files, cmd/init.go, and cmd/commands.go, and avoid hand-editing framework-owned paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/servicepack)
- [psyb0t publisher profile](https://clawhub.ai/user/psyb0t)
- [servicepack GitHub repository](https://github.com/psyb0t/servicepack)
- [Setup reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go code examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker for the documented template workflow.]

## Skill Version(s):

1.5.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
