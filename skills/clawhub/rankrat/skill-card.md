## Description:

Rankrat lets agents query SEO and search analytics providers, run bounded site audits, manage monitors, and perform finite remediation for sites the operator controls through a self-hosted MCP and HTTP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and SEO operators use rankrat to inspect search performance, indexing, analytics, PageSpeed, backlinks, internal links, and controlled remediation for sites they own or administer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured provider credentials can grant broad account authority within supported SEO, analytics, DNS, cache, and indexing operations.

Mitigation: Install only for sites and provider accounts the operator controls, keep provider secrets mounted read-only, and review provider scopes before use.

Risk: Writable mode can mutate provider resources and local Rankrat state through onboarding, indexing notifications, monitor lifecycle operations, cache purges, and related write tools.

Mitigation: Run with RANKRAT_READ_ONLY=true for autonomous or untrusted callers so write tools and write routes are not exposed.

Risk: HTTP mode can expose the MCP and REST interfaces beyond the intended operator if bound too widely or left without authentication.

Mitigation: Bind HTTP to loopback or a private network and configure a bearer token whenever anything else can reach the service.

Risk: Local Lighthouse browser audits execute Chromium against requested pages and are not appropriate for hostile content without stronger isolation.

Mitigation: Use the browser worker only for operator-controlled sites, and add an outer sandbox such as gVisor or Kata before auditing untrusted pages.

## Reference(s):

- [ClawHub rankrat release page](https://clawhub.ai/psyb0t/skills/rankrat)
- [Rankrat setup reference](references/setup.md)
- [Rankrat launcher](references/rankrat.sh)
- [Rankrat public documentation](https://github.com/psyb0t/rankrat/tree/main/docs)
- [Rankrat repository homepage](https://github.com/psyb0t/rankrat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and API-backed findings from configured providers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are bounded by configured provider accounts, site ownership, read-only mode, and available credentials.]

## Skill Version(s):

0.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
