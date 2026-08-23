## Description:

Python patterns for CLI tools, async concurrency, and backend services for work on Python code, CLI apps, FastAPI services, asyncio, background jobs, and uv, ruff, ty, pytest, or pyproject.toml configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for practical Python service and CLI implementation guidance, including project structure, dependency tooling, async concurrency, FastAPI patterns, background jobs, resilience, observability, testing, migrations, and API design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to run development commands or suggest dependency, migration, or production configuration changes.

Mitigation: Review project-specific changes before applying them, especially dependency updates, migrations, and production configuration.

Risk: Backend service guidance can affect security-sensitive behavior such as authorization fallbacks, external response handling, and secret-dependent configuration.

Mitigation: Validate security decisions at boundaries, fail closed for authorization and trust checks, and confirm configuration during startup before serving traffic.

## Reference(s):

- [Python CLI Tools](references/cli-tools.md)
- [FastAPI Services](references/fastapi.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project-specific code, dependency, migration, and production configuration changes for human review.]

## Skill Version(s):

4.4.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
