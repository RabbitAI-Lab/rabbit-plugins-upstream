## Description:

Rapid development with Cloudflare Workers - build and deploy serverless applications on Cloudflare's global network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to build, configure, test, observe, and deploy Cloudflare Workers applications, including APIs, full-stack apps, edge middleware, background jobs, bindings, and CI/CD workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment, --remote, delete, restore, and CI/CD examples can affect live Cloudflare infrastructure.

Mitigation: Require explicit user approval before live operations, test in staging first, keep backups for data-affecting workflows, and use least-privilege Cloudflare tokens.

Risk: Logging and alerting examples may expose credentials, cookies, query strings, user identifiers, stack traces, or other sensitive data if copied directly.

Mitigation: Redact sensitive headers and identifiers before logging or forwarding data to external systems.

## Reference(s):

- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/cloudflare-workers)
- [Complete Bindings Guide](references/bindings-complete-guide.md)
- [Wrangler and Deployment Guide](references/wrangler-and-deployment.md)
- [Development Best Practices](references/development-patterns.md)
- [Advanced Features](references/advanced-features.md)
- [Observability](references/observability.md)
- [Cloudflare Workers documentation](https://developers.cloudflare.com/workers/)
- [Wrangler CLI documentation](https://developers.cloudflare.com/workers/wrangler/)
- [Cloudflare Workers Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)
- [Cloudflare Workers examples](https://developers.cloudflare.com/workers/examples/)
- [Cloudflare Workflows documentation](https://developers.cloudflare.com/workflows/)
- [Cloudflare Containers documentation](https://developers.cloudflare.com/containers/)
- [Cloudflare Workers quickstarts](https://developers.cloudflare.com/workers/get-started/quickstarts/)
- [Cloudflare Workers framework guides](https://developers.cloudflare.com/workers/framework-guides/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Wrangler commands, TypeScript examples, TOML configuration, deployment steps, and operational guidance.]

## Skill Version(s):

3.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
