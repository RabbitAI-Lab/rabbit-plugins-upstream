## Description: <br>
Rapid development with Cloudflare Workers for building and deploying serverless APIs, full-stack web apps, edge functions, background jobs, and real-time applications on Cloudflare's global network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to create, configure, test, and deploy Cloudflare Workers applications, including APIs, full-stack apps, edge middleware, scheduled jobs, queues, storage bindings, and observability workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Examples may affect live Cloudflare production resources when deployment, remote binding, or resource deletion commands are used without review. <br>
Mitigation: Review Wrangler commands before execution, prefer staging or local development first, and avoid running examples against production by default. <br>
Risk: Cloudflare API tokens and account identifiers may be exposed or over-scoped during non-interactive authentication and CI deployment workflows. <br>
Mitigation: Use narrowly scoped Cloudflare tokens, store credentials in CI secrets or Wrangler secrets, and avoid placing sensitive values in configuration files. <br>
Risk: Telemetry, logs, headers, URLs, cookies, tokens, stack traces, raw emails, and third-party logging payloads may contain sensitive data. <br>
Mitigation: Add redaction and data minimization before logging, tailing, exporting, or forwarding runtime and observability data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/cloudflare-workers) <br>
- [Skill Homepage](https://github.com/tenequm/skills/tree/main/skills/cloudflare-workers) <br>
- [Cloudflare Workers Documentation](https://developers.cloudflare.com/workers/) <br>
- [Wrangler CLI Documentation](https://developers.cloudflare.com/workers/wrangler/) <br>
- [Cloudflare Workers Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/) <br>
- [Complete Bindings Guide](references/bindings-complete-guide.md) <br>
- [Wrangler and Deployment](references/wrangler-and-deployment.md) <br>
- [Development Best Practices](references/development-patterns.md) <br>
- [Advanced Features](references/advanced-features.md) <br>
- [Observability](references/observability.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Wrangler commands, TypeScript examples, TOML configuration, CI/CD snippets, and security guidance for Cloudflare credentials and telemetry.] <br>

## Skill Version(s): <br>
3.1.2 (source: SKILL.md frontmatter metadata.version and evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
