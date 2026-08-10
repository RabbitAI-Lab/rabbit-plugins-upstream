## Description:

rankrat lets an agent query SEO, search analytics, indexing, performance, audit, backlink, Cloudflare, and monitor data for controlled sites through a self-hosted MCP server and FastAPI JSON API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, site operators, and SEO engineers use rankrat to let an agent inspect and improve sites they control across Search Console, Bing Webmaster Tools, GA4, PageSpeed, CrUX, Cloudflare, backlink providers, Lighthouse, and bounded site audits. It is suited to diagnosing traffic drops, indexing issues, internal links, browser scores, provider readiness, and finite remediation within configured account and site boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server can access sensitive provider accounts and site analytics.

Mitigation: Install it only for sites and provider accounts the operator controls, and keep the default read-only mode unless writes are intentionally required.

Risk: Writable or unbounded deployments can submit indexing changes, verify ownership, change limited Cloudflare cache settings, or manage monitors.

Mitigation: Use writable or unbounded mode only as a trusted-caller deployment, keep HTTP on loopback or behind a bearer token, and return to bounded mode after onboarding or remediation.

Risk: The optional Lighthouse worker opens requested pages and may encounter hostile content.

Mitigation: Use the Lighthouse worker only on operator-controlled pages, and add a stronger outer sandbox before using it on hostile pages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/rankrat)
- [setup.md](references/setup.md)
- [rankrat.sh](references/rankrat.sh)
- [Rankrat documentation](https://github.com/psyb0t/rankrat/tree/main/docs)
- [Getting started](https://github.com/psyb0t/rankrat/blob/main/docs/getting-started.md)
- [Providers and credentials](https://github.com/psyb0t/rankrat/blob/main/docs/providers.md)
- [Troubleshooting](https://github.com/psyb0t/rankrat/blob/main/docs/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands, configuration guidance, and MCP tool-use recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to run Docker-based MCP server commands, inspect provider readiness, and interpret API or audit results without returning provider credentials.]

## Skill Version(s):

0.9.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
