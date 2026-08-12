## Description:

servicepack helps developers build Go service and daemon projects from the psyb0t/servicepack clone-and-own template, including service scaffolding, dependency-ordered startup, retries, readiness gating, CLI commands, logging, configuration, and graceful shutdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when starting or extending Go service or daemon projects that need concurrent long-running workers, dependency and readiness semantics, retry behavior, service-specific CLI commands, and graceful shutdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can rewrite module files and reset git history when running make own.

Mitigation: Use the skill only in a fresh clone or disposable project workspace, and review the upstream Makefile before running make own.

Risk: Generated or updated service code may change project behavior or introduce incorrect service logic.

Mitigation: Review proposed code changes and run the relevant Go build, test, vet, or make targets before deployment.

## Reference(s):

- [Setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/servicepack)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose service scaffold code, lifecycle hook changes, CLI command additions, and build or test commands.]

## Skill Version(s):

1.2.23 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
