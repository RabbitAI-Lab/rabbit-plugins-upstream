## Description: <br>
Build type-safe React apps with TanStack Query (data fetching, caching, mutations), Router (file-based routing, search params, loaders), and Start (SSR, server functions, middleware). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to build React applications with TanStack Query, Router, and Start, including data fetching, cache management, type-safe routing, SSR, server functions, middleware, and deployment patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated app code may add server functions, API routes, or authentication flows that handle sessions or private data. <br>
Mitigation: Review generated handlers and middleware so authorization is enforced at the server function, server route, or API endpoint that reads or writes private data. <br>
Risk: Generated loaders or client code may accidentally expose secrets because TanStack loaders can run on both server and client. <br>
Mitigation: Keep secrets in server-only functions or server routes, and inspect generated bundles and environment variable usage before deployment. <br>
Risk: Cache persistence or public cache headers can retain credential-bearing or per-user data in inappropriate storage or shared caches. <br>
Mitigation: Exclude identity-specific queries from persistence and use private, no-store, or Vary-aware cache headers for authenticated responses. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/tanstack) <br>
- [Publisher Profile](https://clawhub.ai/user/tenequm) <br>
- [ClawHub Homepage Metadata](https://github.com/tenequm/skills/tree/main/skills/tanstack) <br>
- [TanStack Query Docs](https://tanstack.com/query/latest/docs/framework/react/overview) <br>
- [TanStack Router Docs](https://tanstack.com/router/latest/docs/framework/react/overview) <br>
- [TanStack Start Docs](https://tanstack.com/start/latest/docs/framework/react/overview) <br>
- [TanStack Query GitHub](https://github.com/TanStack/query) <br>
- [TanStack Router GitHub](https://github.com/TanStack/router) <br>
- [Query Guide](references/query-guide.md) <br>
- [Router Guide](references/router-guide.md) <br>
- [Start Guide](references/start-guide.md) <br>
- [Data Loading](references/data-loading.md) <br>
- [Server Functions](references/server-functions.md) <br>
- [Middleware](references/middleware.md) <br>
- [SSR Modes](references/ssr-modes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with TypeScript, TSX, shell, and configuration code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; generated application changes should be reviewed before execution or deployment.] <br>

## Skill Version(s): <br>
0.4.2 (source: frontmatter and evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
