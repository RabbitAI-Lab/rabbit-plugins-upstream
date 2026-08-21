## Description:

Guides developers in building Go services with the psyb0t/servicepack clone-and-own framework, including service scaffolding, lifecycle hooks, dependency ordering, retries, readiness gating, logging, configuration, build, test, and lint workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when starting or maintaining Go services built from the servicepack template, especially services that need concurrent workers, graceful shutdown, dependency-aware startup, retries, readiness gates, and per-service CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The `make own MODNAME=...` workflow rewrites the module, removes the clone's Git history, and reinitializes the repository.

Mitigation: Run it only once, at the start of a fresh intended servicepack clone, after confirming there is no local history or work in that clone that must be preserved.

Risk: Framework-owned files can be overwritten by servicepack update workflows.

Mitigation: Customize through service files, `cmd/init.go`, `cmd/commands.go`, and lifecycle hooks instead of editing framework-owned paths.

## Reference(s):

- [Setup](references/setup.md)
- [servicepack GitHub repository](https://github.com/psyb0t/servicepack)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/servicepack)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with Go code examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose changes under service-owned files and commands for Docker-backed build, test, lint, formatting, and service registration workflows.]

## Skill Version(s):

1.9.2 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
