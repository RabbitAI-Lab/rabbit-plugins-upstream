## Description:

Canonry guides agents through connected MCP tools or the `cnry` CLI to inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, marketers, and developers use this skill to route Canonry MCP and CLI workflows for AI visibility status, diagnosis, measurement planning, integration checks, and reporting while preserving evidence and approval boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected marketing, site, traffic, and reporting integrations can expose sensitive account permissions or credentials if handled in chat or shell history.

Mitigation: Keep secrets out of chat and shell history, prefer file-based or interactive secret entry, and review Cloudflare, WordPress, ads, and analytics permissions before use.

Risk: Live provider reads, sweeps, probes, syncs, schedules, webhooks, and write actions can consume quota or affect connected accounts.

Mitigation: Enable those actions only for exact approved projects and accounts, and require bounded approval before externally visible or quota-consuming work.

Risk: Reports or diagnosis can become misleading when evidence is missing, stale, or merged across incompatible providers, time windows, locations, or query classes.

Mitigation: Use server-returned metrics, preserve project and measurement context, keep mention and citation signals separate, and state missing or stale inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI examples and structured JSON references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational guidance depends on the connected Canonry MCP or CLI permissions and explicit approval for bounded live actions.]

## Skill Version(s):

5.0.1+92ebeea (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
