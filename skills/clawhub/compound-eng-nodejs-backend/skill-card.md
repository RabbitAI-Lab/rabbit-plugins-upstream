## Description:

Provides Node.js backend patterns for layered architecture, TypeScript, validation, error handling, security, observability, logging, metrics, and deployment when building REST APIs, REST endpoints, middleware, Express/Fastify/Hono/NestJS/Koa servers, tRPC procedures, Bun servers, or server-side TypeScript.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for Node.js backend implementation and review work, including REST APIs, middleware, server-side TypeScript, validation, security, observability, and production deployment patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional unpinned `npx tsc --extendedDiagnostics` diagnostic command may use a TypeScript compiler outside the project's pinned toolchain.

Mitigation: Prefer `./node_modules/.bin/tsc --extendedDiagnostics` or an offline/no-install package-manager mode before running diagnostics.

Risk: Backend guidance touching authorization, validation, resilience, or error handling can introduce caller-visible behavior changes if applied without project review.

Mitigation: Review generated changes against existing API contracts, preserve authorization behavior, validate boundary inputs, and test failure paths before deployment.

## Reference(s):

- [TypeScript Configuration & Patterns](references/typescript-config.md)
- [Authentication & Security](references/security.md)
- [API Design Patterns](references/api-design.md)
- [Database & Production](references/database-production.md)
- [API Boundaries](references/api-boundaries.md)
- [Async Operations and Production](references/async-and-production.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is conditional on the user's Node.js backend task and relevant reference files.]

## Skill Version(s):

4.5.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
