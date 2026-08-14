## Description:

servicepack guides agents through using the psyb0t/servicepack Go template to create and maintain multi-service daemons with lifecycle hooks, dependency ordering, retries, readiness gates, service scaffolding, testing, and build commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to scaffold, update, test, and reason about Go services built from the servicepack template. It is most useful for projects that need multiple long-running workers with graceful shutdown, dependency ordering, readiness signaling, retry handling, and service-specific CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: `make own` rewrites the cloned template, removes that clone's Git history, and reinitializes the repository.

Mitigation: Run it only in a fresh or disposable clone and keep separate backups of any work you care about.

Risk: Framework-owned files can be overwritten by servicepack update workflows.

Mitigation: Customize through service files and documented lifecycle hooks rather than editing framework-owned paths.

## Reference(s):

- [Setup](references/setup.md)
- [servicepack GitHub homepage](https://github.com/psyb0t/servicepack)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with Go code examples, shell command blocks, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal build, test, lint, audit, and generation workflows require Docker.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
