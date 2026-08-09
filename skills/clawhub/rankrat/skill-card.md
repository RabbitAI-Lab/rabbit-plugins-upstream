## Description:

Query Google Search Console, Bing Webmaster Tools, GA4, PageSpeed, CrUX, Cloudflare analytics, and configured backlink providers; run Lighthouse and bounded whole-site/internal-link audits; persist monitors and issue history; automate ownership and finite remediation through one self-hosted MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and SEO teams use rankrat to inspect and improve SEO, indexing, internal links, backlinks, browser scores, performance history, and search traffic for sites and provider accounts they control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server can access sensitive SEO, analytics, DNS, Cloudflare, and backlink-provider data for configured accounts.

Mitigation: Install only for sites and provider accounts you control, keep boundaries narrow, and keep provider credentials on the host.

Risk: Writable, unbounded, and agent-onboarding modes can make provider-side changes when deliberately enabled.

Mitigation: Keep read-only mode on for general use and enable write, unbounded, or onboarding modes only for trusted sessions where changes are intended.

Risk: HTTP mode may expose the MCP and REST surfaces beyond the local operator if bound or published broadly.

Mitigation: Bind HTTP to loopback or a private network and use a bearer token whenever anything else can reach the service.

Risk: The optional Lighthouse browser worker processes public pages and needs stronger isolation for hostile content.

Mitigation: Use Lighthouse only for operator-controlled sites, and add an outer sandbox such as gVisor or Kata before auditing hostile pages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/rankrat)
- [Setup reference](references/setup.md)
- [Rankrat wrapper](references/rankrat.sh)
- [Project homepage](https://github.com/psyb0t/rankrat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, structured tool responses, JSON API responses, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are bounded by configured provider accounts, sites, properties, and optional read/write modes.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
