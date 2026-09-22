## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing teams use this skill to guide Canonry MCP or CLI workflows for AI visibility evidence, diagnostics, measurement planning, integrations, and reporting. It helps agents start from stored evidence, preserve measurement context, and request approval before externally visible or quota-consuming actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could propose writes, schedule changes, deployments, live syncs, sweeps, key creation, or provider configuration beyond the intended task.

Mitigation: Review commands before execution and require explicit approval for the exact target, action, and bounded work.

Risk: API keys, OAuth secrets, WordPress application passwords, or local Canonry configuration could be exposed through chat, tool arguments, reports, or public guidance.

Mitigation: Keep credentials in secure setup flows or permission-restricted local configuration, and do not include secrets in agent-visible content.

Risk: Reports or diagnoses can mislead users if stale, missing, or incomparable evidence is treated as zero, current, or causal.

Mitigation: Use server-returned metrics, preserve project, time window, provider, model, location, sample size, and query class, and state missing or stale inputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry Operations Guide v1](artifact/SKILL.md)
- [Canonry CLI Reference](artifact/references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](artifact/references/aeo-analysis.md)
- [Indexing Workflows for AEO](artifact/references/indexing.md)
- [WordPress Integration](artifact/references/wordpress-integration.md)
- [Server-side traffic (AI Visibility - Server-Side)](artifact/references/server-side-traffic.md)
- [Google Business Profile Integration](artifact/references/google-business-profile.md)
- [Google Ads and Google Tag Manager](artifact/references/google-marketing.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-directed operational guidance; review commands before approving writes, schedule changes, Cloudflare Worker deployments, live syncs or sweeps, key creation, or provider configuration.]

## Skill Version(s):

5.7.0+1697bee (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
