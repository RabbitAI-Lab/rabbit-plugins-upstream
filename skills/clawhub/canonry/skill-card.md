## Description:

Operate Canonry (`cnry` / `canonry`) for Answer Engine Optimization workflows, including project setup, integrations, sweeps, technical audits, indexing, mention and citation analysis, traffic sources, and guarded ads lifecycle operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and AEO operators use this skill to configure Canonry projects, run approved sweeps and audits, connect analytics, search, traffic, and local-business integrations, and turn mention and citation evidence into fixes and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise broad, persistent access across Canonry-connected marketing, website, ads, traffic, and analytics workflows.

Mitigation: Install it only for intended Canonry operations, prefer read-only or tightly project-scoped keys, and require explicit approval for every mutation, sweep, or live provider read.

Risk: Local Canonry configuration may contain credentials or full-instance API keys.

Mitigation: Protect ~/.canonry/config.yaml like a secret store, do not print or paste credentials, and avoid switching credentials to bypass missing tools or authorization failures.

Risk: Schedules, webhooks, and Aero automation can continue operating after setup.

Mitigation: Review active schedules, webhooks, and Aero automation before enabling or changing them, and keep automation bounded to the intended project and workflow.

Risk: External AI providers and connected Google, WordPress, Cloudflare, Vercel, and analytics services may incur quota, cost, or data-exposure impact.

Mitigation: Choose providers deliberately, use stored reads and dry runs where available, and confirm quota-consuming or live-service operations before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry website](https://canonry.ai)
- [Canonry GitHub documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON-oriented reads, configuration instructions, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 22.14+ and a globally installed @canonry/canonry runtime with canonry-mcp on PATH.]

## Skill Version(s):

4.180.4+62e0b82 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
