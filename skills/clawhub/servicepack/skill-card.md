## Description:

servicepack helps agents guide developers through creating Go services from the psyb0t/servicepack clone-and-own framework, including service scaffolding, lifecycle hooks, dependency-aware startup, readiness behavior, build/test workflows, and framework boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when starting or maintaining Go services based on the servicepack template, especially services that need concurrent workers, graceful shutdown, retries, dependency ordering, readiness gating, per-service CLI commands, and Docker-backed build or test workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides agents to clone an external Go template and run Docker/Make build workflows.

Mitigation: Review proposed commands before execution and ensure Docker is available and appropriate for the target environment.

Risk: The `make own` workflow intentionally removes the cloned repository's `.git` history and reinitializes it for a new project.

Mitigation: Run `make own` only once at the start of a fresh clone, not inside an existing project or a clone with work that must be preserved.

Risk: Framework-owned files can be overwritten by servicepack update workflows.

Mitigation: Customize services, lifecycle hooks, and user-owned command files instead of editing framework-owned paths directly.

## Reference(s):

- [servicepack ClawHub release](https://clawhub.ai/psyb0t/skills/servicepack)
- [servicepack repository](https://github.com/psyb0t/servicepack)
- [Setup reference](references/setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline Go code, shell commands, configuration examples, and file path references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include Make and Docker commands plus generated Go service scaffolding patterns; command execution remains subject to agent/user approval.]

## Skill Version(s):

1.7.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
