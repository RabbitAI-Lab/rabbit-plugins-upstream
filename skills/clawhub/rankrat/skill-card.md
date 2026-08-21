## Description:

Rankrat helps agents inspect and improve SEO, indexing, analytics, tags, redirects, backlinks, audits, and performance history for sites the user controls through a self-hosted MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and SEO practitioners use Rankrat to inspect and improve search visibility, indexing, analytics, ownership, tags, redirects, backlinks, internal links, browser scores, and site-audit history for sites they control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured provider credentials can grant account-wide read and write authority.

Mitigation: Install only for provider accounts and sites the operator controls, and use RANKRAT_READ_ONLY=true with read-only config mounts for autonomous or less trusted agents.

Risk: An exposed HTTP endpoint could let unintended callers reach the MCP server or REST API.

Mitigation: Bind HTTP to loopback or a private network and configure a bearer token whenever anything else can reach the service.

Risk: Local Lighthouse browser audits can load public pages and their subresources.

Mitigation: Use the browser worker only for operator-controlled sites, keep URL boundaries configured, and use a stronger outer sandbox such as gVisor or Kata for hostile content.

## Reference(s):

- [Rankrat setup reference](references/setup.md)
- [Rankrat documentation](https://github.com/psyb0t/rankrat/tree/main/docs)
- [Getting started](https://github.com/psyb0t/rankrat/blob/main/docs/getting-started.md)
- [Providers and credentials](https://github.com/psyb0t/rankrat/blob/main/docs/providers.md)
- [Troubleshooting](https://github.com/psyb0t/rankrat/blob/main/docs/troubleshooting.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/rankrat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and MCP or REST tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include provider API reads, bounded audit findings, remediation guidance, and write-operation instructions when writable mode is enabled.]

## Skill Version(s):

0.20.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
