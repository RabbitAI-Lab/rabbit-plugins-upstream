## Description:

Provides Python patterns for CLI tools, asynchronous concurrency, and backend services, including FastAPI and development tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill for guidance when building Python CLI tools, FastAPI services, asynchronous workflows, and background jobs, or configuring and testing Python projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated retry or background-job code could repeat work or lose unfinished tasks.

Mitigation: Review retry conditions, idempotency, cancellation, and task lifecycle before deployment.

Risk: Secrets configuration or production migrations could expose credentials or disrupt data.

Mitigation: Check secret handling and test migration and rollback plans in a staging environment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-python-services)
- [Python tooling and tests](references/tooling-and-tests.md)
- [Concurrency and resilience](references/concurrency-and-resilience.md)
- [Service boundaries](references/service-boundaries.md)
- [CLI tools](references/cli-tools.md)
- [FastAPI services](references/fastapi.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python, shell, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the developer's task and require review before use.]

## Skill Version(s):

5.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
