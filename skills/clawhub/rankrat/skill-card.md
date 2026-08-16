## Description:

Rankrat is a self-hosted MCP server that lets agents inspect and, when explicitly trusted, manage SEO, indexing, analytics, tags, redirects, backlinks, performance, and site-audit workflows for configured sites the operator controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and SEO or analytics teams use Rankrat to connect an agent to their own provider accounts for search analytics, indexing diagnostics, site audits, performance reports, ownership workflows, and bounded remediation. It is intended for sites and provider accounts the operator controls, with read-only mode for reporting or autonomous-agent use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured provider credentials can authorize account-level changes across supported Google, Bing, Cloudflare, Microsoft Clarity, and related provider resources.

Mitigation: Install Rankrat only for provider accounts and sites the operator controls, and use provider credentials with the narrowest practical account scope.

Risk: Writable mode is the default and can expose mutating actions such as Tag Manager publication, DNS verification, redirects, cache purges, indexing submissions, and monitor changes.

Mitigation: Set RANKRAT_READ_ONLY=true for reporting workflows or autonomous agents, and reserve writable mode for deliberate operator-approved changes.

Risk: HTTP mode can expose powerful provider-backed operations if reachable by untrusted clients.

Mitigation: Bind HTTP to loopback or a private network and configure bearer-token protection whenever anything else can reach the service.

Risk: Local Lighthouse audits run browser work against requested bounded pages and are not a substitute for a browser renderer sandbox when content may be hostile.

Mitigation: Use the Lighthouse worker for operator-controlled sites and add an outer sandbox such as gVisor or Kata Containers before auditing hostile content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/rankrat)
- [Rankrat setup reference](references/setup.md)
- [Rankrat repository](https://github.com/psyb0t/rankrat)
- [Rankrat documentation](https://github.com/psyb0t/rankrat/tree/main/docs)
- [Getting started](https://github.com/psyb0t/rankrat/blob/main/docs/getting-started.md)
- [Providers and credentials](https://github.com/psyb0t/rankrat/blob/main/docs/providers.md)
- [Troubleshooting](https://github.com/psyb0t/rankrat/blob/main/docs/troubleshooting.md)
- [Merged OpenAPI document](https://github.com/psyb0t/rankrat/blob/main/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, configuration values, and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include provider-specific reports, API results, and remediation instructions bounded to configured sites.]

## Skill Version(s):

0.15.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
