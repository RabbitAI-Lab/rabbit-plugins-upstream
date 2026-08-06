## Description:

rankrat helps agents query owned SEO, indexing, analytics, PageSpeed, and Lighthouse data through a self-hosted MCP and HTTP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners, SEO practitioners, developers, and agents use rankrat to analyze properties they control, diagnose search traffic and indexing issues, audit page performance, and prepare bounded setup or onboarding steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to sensitive SEO, analytics, and provider account data.

Mitigation: Install it only for sites and provider accounts the operator controls, keep credentials on the host, bind HTTP to loopback or a private network, and require the bearer token for any reachable HTTP service.

Risk: Writable and unbounded modes can submit indexing changes, onboard resources, or update the configured boundary file.

Mitigation: Keep the default read-only mode for normal use, enable writable or unbounded mode only for trusted onboarding sessions, and restart in bounded mode after exact resources are recorded.

Risk: The optional Lighthouse worker opens requested public pages and documents that Chromium runs without its internal sandbox in the hardened container setup.

Mitigation: Use Lighthouse only for operator-controlled sites, keep the worker credential-free, and add an outer sandbox such as gVisor or Kata before auditing hostile content.

## Reference(s):

- [rankrat ClawHub skill page](https://clawhub.ai/psyb0t/skills/rankrat)
- [setup reference](references/setup.md)
- [rankrat wrapper script](references/rankrat.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are scoped to configured owned sites and provider accounts; provider availability depends on local credentials.]

## Skill Version(s):

0.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
