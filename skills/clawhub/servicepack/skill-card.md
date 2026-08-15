## Description:

Build a Go service on psyb0t/servicepack, a clone-and-own framework for creating related Go services that can run together locally and later deploy as one binary or separate microservices with retry, dependency, readiness, CLI, logging, and graceful-shutdown patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold and extend Go service projects on the servicepack template, including service registration, lifecycle hooks, dependency ordering, readiness gating, retry behavior, and build/test commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ownership/setup workflow rewrites module identity and resets git history for the clone.

Mitigation: Run ownership/setup commands only in a fresh clone intended to become a servicepack-based project.

Risk: Generated or edited services may connect to infrastructure or expose application-specific runtime surfaces.

Mitigation: Review generated service code, configuration, and environment variables before running service binaries against real infrastructure.

Risk: Framework-owned files can be overwritten by servicepack update commands.

Mitigation: Customize through supported service directories and lifecycle hooks instead of hand-editing framework-owned files.

## Reference(s):

- [servicepack ClawHub release](https://clawhub.ai/psyb0t/skills/servicepack)
- [servicepack repository](https://github.com/psyb0t/servicepack)
- [Setup reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file edits under service directories and project command files, and may suggest Docker-backed make targets.]

## Skill Version(s):

1.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
