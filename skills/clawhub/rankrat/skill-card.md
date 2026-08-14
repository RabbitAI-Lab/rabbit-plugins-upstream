## Description:

Rankrat lets agents inspect and improve SEO, indexing, analytics, tags, redirects, backlinks, browser scores, performance history, and search traffic for sites the operator controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and SEO practitioners use this skill to connect an agent to their own search, analytics, tag, performance, and DNS-provider accounts for bounded analysis and remediation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writable mode delegates account-level provider authority to the agent.

Mitigation: Use RANKRAT_READ_ONLY=true for analysis-only workflows or when the caller should not mutate provider or local state.

Risk: Configured provider credentials can reach every supported resource exposed by those accounts.

Mitigation: Install only for sites and provider accounts the operator controls, and keep provider secret mounts read-only.

Risk: HTTP transport can expose the server beyond the local process boundary if bound broadly.

Mitigation: Bind HTTP to loopback or a private network and configure a bearer token whenever another process or host can reach it.

Risk: Local Lighthouse browser audits fetch operator-requested public pages and may encounter hostile content.

Mitigation: Use the browser worker only for operator-controlled sites and add an outer sandbox for higher-risk pages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/rankrat)
- [Setup reference](references/setup.md)
- [Rankrat public documentation](https://github.com/psyb0t/rankrat/tree/main/docs)
- [Getting started](https://github.com/psyb0t/rankrat/blob/main/docs/getting-started.md)
- [Providers and credentials](https://github.com/psyb0t/rankrat/blob/main/docs/providers.md)
- [Troubleshooting](https://github.com/psyb0t/rankrat/blob/main/docs/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured provider results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can emit read-only analysis or writable remediation guidance depending on Rankrat runtime mode and configured provider credentials.]

## Skill Version(s):

0.13.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
