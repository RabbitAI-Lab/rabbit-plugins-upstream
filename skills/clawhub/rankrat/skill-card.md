## Description:

Query Google Search Console, Google Tag Manager, Bing Webmaster Tools, GA4, Microsoft Clarity, PageSpeed, CrUX, Cloudflare analytics, and Bing backlink intelligence; manage typed tags and safe edge redirects; run Lighthouse and bounded whole-site/internal-link audits; persist monitors and issue history; automate ownership and finite remediation through one self-hosted MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and SEO operators use this skill to inspect and improve search visibility, indexing, analytics, tags, redirects, backlinks, performance, and audit history for sites they control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured provider credentials can authorize broad read and write access across supported SEO, analytics, tag, DNS, cache, redirect, and monitoring resources.

Mitigation: Install only for provider accounts and sites the operator controls, and run agents that should not mutate provider or local state with RANKRAT_READ_ONLY=true.

Risk: HTTP mode can expose the MCP and REST surfaces beyond the local process if bound or published too broadly.

Mitigation: Keep HTTP bound to loopback or a private network and require a bearer token whenever any other process can reach it.

Risk: Local Lighthouse audits execute a browser against requested pages and may need stronger containment for hostile content.

Mitigation: Use Lighthouse only for operator-controlled sites, keep the browser worker credential-free, and add an outer sandbox such as gVisor or Kata for untrusted pages.

## Reference(s):

- [Setup reference](references/setup.md)
- [Rankrat documentation](https://github.com/psyb0t/rankrat/tree/main/docs)
- [Getting started](https://github.com/psyb0t/rankrat/blob/main/docs/getting-started.md)
- [Providers and credentials](https://github.com/psyb0t/rankrat/blob/main/docs/providers.md)
- [Troubleshooting](https://github.com/psyb0t/rankrat/blob/main/docs/troubleshooting.md)
- [Merged OpenAPI document](https://github.com/psyb0t/rankrat/blob/main/openapi.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with command examples and MCP or REST tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on configured provider accounts, writable versus read-only mode, and whether optional Lighthouse support is enabled.]

## Skill Version(s):

0.14.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
