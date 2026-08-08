## Description:

rankrat lets agents query Google Search Console, Bing Webmaster Tools, Google Analytics 4, PageSpeed Insights, local Lighthouse, DNS ownership automation, site audits, and Bing backlink evidence for sites the operator controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and SEO engineers use rankrat to let an agent inspect and improve search analytics, indexing, site audit findings, ownership status, backlinks, browser scores, and search traffic for sites they control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive provider data for configured sites and accounts.

Mitigation: Install it only for sites and provider accounts the operator controls, and keep the boundary file limited to the intended accounts, sites, and properties.

Risk: HTTP mode can expose the MCP and REST surfaces if bound too broadly or left unauthenticated.

Mitigation: Bind HTTP to loopback or a private network and configure the bearer secret whenever any other process or host can reach the port.

Risk: Write, agent onboarding, or unbounded modes can submit URLs, change search-console or Bing resources, publish DNS verification records, or update the boundary file.

Mitigation: Keep the default read-only mode for reporting and enable write-capable modes only for trusted sessions.

Risk: Local Lighthouse audits execute browser work against operator-selected pages.

Mitigation: Use the browser worker only for operator-controlled sites and add a stronger outer sandbox before auditing hostile content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/rankrat)
- [Publisher profile](https://clawhub.ai/user/psyb0t)
- [Setup reference](references/setup.md)
- [rankrat wrapper](references/rankrat.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration values, and provider report summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing results may include SEO reports, analytics summaries, audit findings, remediation guidance, and Docker run commands.]

## Skill Version(s):

0.8.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
