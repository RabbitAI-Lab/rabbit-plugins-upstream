## Description:

Type-safe React with TanStack Query (fetching, caching, mutations), Router (file-based routing, search params, loaders), and Start (SSR, server functions). Use for react-query, server state, typed search params, route loaders, or SSR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill as framework reference material for building type-safe React applications with TanStack Query, Router, and Start. It helps agents propose data fetching, routing, SSR, server function, middleware, and deployment guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copyable examples can expose secrets through URLs, client-returned data, or isomorphic loaders.

Mitigation: Validate data boundaries, keep secrets on the server, and avoid returning sensitive values to client-visible loaders or responses.

Risk: Examples involving file paths or file serving can be adapted unsafely.

Mitigation: Validate filesystem paths, restrict served directories, and review generated file-serving code before use.

Risk: Cache purge endpoints and tokens can be under-protected.

Mitigation: Protect purge endpoints with authorization, avoid long-lived tokens in localStorage, and scope or rotate credentials.

Risk: Scaffold commands may change over time or install unexpected code.

Mitigation: Pin package versions or run scaffold commands in a sandbox before applying them to sensitive repositories.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/tanstack)
- [OpenClaw Homepage](https://github.com/tenequm/skills/tree/main/skills/tanstack)
- [TanStack Query Docs](https://tanstack.com/query/latest/docs/framework/react/overview)
- [TanStack Router Docs](https://tanstack.com/router/latest/docs/framework/react/overview)
- [TanStack Start Docs](https://tanstack.com/start/latest/docs/framework/react/overview)
- [TanStack Query GitHub](https://github.com/TanStack/query)
- [TanStack Router GitHub](https://github.com/TanStack/router)
- [TanStack Query Reference](references/query-guide.md)
- [TanStack Router Reference](references/router-guide.md)
- [TanStack Start Reference](references/start-guide.md)
- [Data Loading](references/data-loading.md)
- [Server Functions](references/server-functions.md)
- [Middleware](references/middleware.md)
- [SSR Modes and Rendering Strategies](references/ssr-modes.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript, TSX, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces framework guidance and examples for agent use; it does not execute code by itself.]

## Skill Version(s):

0.4.5 (source: server release metadata, frontmatter, and changelog released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
