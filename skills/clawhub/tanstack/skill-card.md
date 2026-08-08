## Description:

Builds type-safe React apps with TanStack Query (data fetching, caching, mutations), Router (file-based routing, search params, loaders), and Start (SSR, server functions, middleware). Use when working with react-query, server state, file-based routing, typed search params, route loaders, SSR, or server functions in a full-stack React app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for guidance, examples, and configuration patterns when building React applications with TanStack Query, TanStack Router, and TanStack Start. It covers server state, routing, loaders, SSR, server functions, middleware, and related TypeScript patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples may generate or recommend code that is incorrect, incomplete, or outdated for the current TanStack API.

Mitigation: Review generated code before applying it and verify TanStack Query v5, Router, and Start API details against the linked official documentation.

Risk: CDN purge examples describe privileged cache invalidation behavior that can be unsafe if copied directly.

Mitigation: Use stronger authentication, path allowlisting, rate limiting, and audit logging before adapting CDN purge endpoints.

Risk: Examples involving URL search params or client-visible runtime configuration can expose sensitive data if applied carelessly.

Mitigation: Treat URL search params as public, return only allowlisted non-sensitive runtime config to clients, and keep secrets in server-only functions or routes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/tanstack)
- [ClawHub metadata homepage](https://github.com/tenequm/skills/tree/main/skills/tanstack)
- [TanStack Query docs](https://tanstack.com/query/latest/docs/framework/react/overview)
- [TanStack Router docs](https://tanstack.com/router/latest/docs/framework/react/overview)
- [TanStack Start docs](https://tanstack.com/start/latest/docs/framework/react/overview)
- [TanStack Query GitHub](https://github.com/TanStack/query)
- [TanStack Router GitHub](https://github.com/TanStack/router)
- [TanStack Query (React Query) v5](references/query-guide.md)
- [TanStack Router v1](references/router-guide.md)
- [TanStack Start](references/start-guide.md)
- [Server Functions](references/server-functions.md)
- [SSR Modes and Rendering Strategies](references/ssr-modes.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with TypeScript, TSX, and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only output; examples should be reviewed before use in an application.]

## Skill Version(s):

0.4.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
