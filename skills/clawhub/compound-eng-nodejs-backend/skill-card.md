## Description:

Node.js backend patterns: layered architecture, TypeScript, validation, error handling, security, observability, logging, metrics, deployment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement or review Node.js and server-side TypeScript backends with layered architecture, API validation, error handling, security, observability, database, and production-readiness patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Backend coding guidance may influence generated authentication, dependency, or production configuration without itself guaranteeing security.

Mitigation: Review generated auth, dependency, and production changes, and run the project's normal tests and security checks before deployment.

Risk: Ad hoc package execution or dependency updates can introduce supply-chain risk in Node.js projects.

Mitigation: Prefer pinned project dependencies, frozen installs, reviewed package scripts, and local package commands over unreviewed npx execution.

## Reference(s):

- [API boundaries](references/api-boundaries.md)
- [API Design Patterns](references/api-design.md)
- [Async operations and production](references/async-and-production.md)
- [Database & Production](references/database-production.md)
- [Observability: tracing, sampling, and telemetry governance](references/observability-tracing.md)
- [Authentication & Security](references/security.md)
- [TypeScript Configuration & Patterns](references/typescript-config.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code, shell command, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes the agent to bundled references for API design, security, production, observability, database, and TypeScript decisions.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
