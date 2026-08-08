## Description:

servicepack helps agents guide developers through building Go service daemons from the psyb0t/servicepack clone-and-own template, including service scaffolding, concurrent workers, dependency ordering, readiness gating, retry behavior, CLI commands, logging, configuration, and graceful shutdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when starting a new Go service or extending an existing servicepack-based repository with long-running workers, dependency-aware startup, readiness gates, retry handling, service commands, and generated service registration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The one-time ownership command rewrites module files and recreates Git history in the clone.

Mitigation: Run it only inside a fresh disposable clone of the template after confirming the working directory.

Risk: Framework-owned files can be overwritten by servicepack update flows.

Mitigation: Put custom behavior in service directories, cmd/init.go, cmd/commands.go, and other documented customization points.

Risk: Generated guidance may include build, test, lint, or Make commands that modify local project files.

Mitigation: Review commands, target paths, and the current working directory before execution.

## Reference(s):

- [servicepack ClawHub page](https://clawhub.ai/psyb0t/skills/servicepack)
- [servicepack GitHub repository](https://github.com/psyb0t/servicepack)
- [Setup reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Go code examples, configuration notes, and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include proposed Go service files, lifecycle hook edits, Make targets, build/test commands, and setup guidance.]

## Skill Version(s):

1.2.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
