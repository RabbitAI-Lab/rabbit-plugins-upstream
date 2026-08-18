## Description:

servicepack guides agents through creating and maintaining Go services on the psyb0t/servicepack clone-and-own framework, including service scaffolding, dependency ordering, readiness gates, retries, logging, configuration, lifecycle hooks, and graceful shutdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to start or maintain Go servicepack-based projects that run related workers locally and can later be built as one binary or split into microservices. It is most relevant when projects need dependency-aware startup, readiness gating, retries, per-service commands, and graceful shutdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ownership step rewrites module paths, removes the clone's Git history, reinitializes Git, and creates an initial commit.

Mitigation: Run the ownership step once at the start in a fresh clone, not inside an existing project or repository with work to preserve.

Risk: Docker-backed make targets and generated service registration can modify local project files.

Mitigation: Review generated code and pending file changes before building, testing, or committing.

Risk: Framework-owned files may be overwritten by servicepack update workflows.

Mitigation: Customize through documented service directories, command files, and lifecycle hooks instead of editing framework-owned paths.

## Reference(s):

- [servicepack setup reference](artifact/references/setup.md)
- [servicepack project homepage](https://github.com/psyb0t/servicepack)
- [ClawHub servicepack skill page](https://clawhub.ai/psyb0t/skills/servicepack)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file edits under service and command paths and may suggest make targets for build, test, lint, formatting, audit, service registration, and Docker-backed development.]

## Skill Version(s):

1.6.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
