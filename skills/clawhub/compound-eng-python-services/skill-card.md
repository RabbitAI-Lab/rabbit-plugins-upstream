## Description:

Provides Python patterns for CLI tools, async concurrency, and backend services when working with Python code, building CLI apps, FastAPI services, asyncio, background jobs, or configuring uv, ruff, ty, pytest, or pyproject.toml.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for Python service and CLI work, including FastAPI endpoints, async concurrency, background jobs, package tooling, linting, type checking, and tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guidance for service implementation can lead an agent to propose code, configuration, or verification commands that affect a Python project.

Mitigation: Review proposed edits and commands before applying them, and run the project's normal tests, linting, and type checks.

Risk: Concurrency, retry, timeout, and background-job guidance can change runtime behavior in production services.

Mitigation: Scope changes to the requested behavior, preserve published API contracts, and validate resilience behavior in tests or staging before deployment.

## Reference(s):

- [Python CLI Tools](artifact/references/cli-tools.md)
- [Concurrency and resilience](artifact/references/concurrency-and-resilience.md)
- [FastAPI Services](artifact/references/fastapi.md)
- [Service boundaries](artifact/references/service-boundaries.md)
- [Tooling and tests](artifact/references/tooling-and-tests.md)
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-python-services)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to inspect Python project files and run normal verification commands such as pytest, ruff, and ty when asked to work on Python services.]

## Skill Version(s):

4.6.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
