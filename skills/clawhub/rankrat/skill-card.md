## Description:

rankrat lets agents query owned Search Console, Bing Webmaster Tools, GA4, PageSpeed Insights, and optional Lighthouse data through a self-hosted MCP and HTTP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and SEO analysts use this skill to let an agent inspect search analytics, indexing status, GA4 traffic, PageSpeed results, and bounded Lighthouse audits for sites they already own.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writable, onboarding, or unbounded deployments can let a trusted caller modify provider state or expand the configured boundary.

Mitigation: Install in the default read-only bounded mode unless writes are intentional; when writes are enabled, keep the boundary file tightly scoped and restart without unbounded mode after onboarding.

Risk: An HTTP deployment reachable beyond the intended operator environment could expose access to configured SEO and analytics providers.

Mitigation: Bind HTTP to loopback or a private network and require the configured bearer token whenever anything else can reach the service.

Risk: Provider credentials and OAuth records grant access to site analytics and webmaster data.

Mitigation: Keep provider secrets read-only, store OAuth records only on the host running rankrat, and mount only the credentials needed for the configured accounts and sites.

## Reference(s):

- [setup.md](references/setup.md)
- [rankrat.sh](references/rankrat.sh)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/rankrat)
- [rankrat homepage](https://github.com/psyb0t/rankrat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides use of a self-hosted server and returns provider-derived SEO, analytics, indexing, PageSpeed, and Lighthouse information through the configured agent client.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
