## Description:

Operate Canonry (the `cnry` / `canonry` CLI) for AEO. Load this BEFORE any canonry operator task: creating or configuring a project, connecting GSC, GA4, Bing, Google Business Profile or a Cloudflare traffic source, running or scheduling a sweep, reading mention and citation coverage, running a technical audit, submitting sitemaps, or diagnosing why a number moved. Covers anything touching cnry, canonry doctor, ~/.canonry, @canonry/canonry, the canonry_* MCP tools, mention share, or direct-push / queue-pull traffic. Load it before acting, not after something fails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing engineers use this skill to manage Canonry AEO workflows: configuring projects, connecting analytics and provider accounts, running approved sweeps and audits, interpreting mention and citation coverage, and applying documented indexing or content fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad Canonry operations that touch site integrations, provider accounts, schedules, sweeps, and write-capable project settings.

Mitigation: Require explicit operator approval for writes, schedules, quota-consuming sweeps, and live provider reads; prefer stored reads and dry-run previews when available.

Risk: Canonry configuration can contain sensitive WordPress, Google, Cloudflare, Vercel, OpenAI Ads, and other tokens.

Mitigation: Keep ~/.canonry/config.yaml private with restrictive permissions, never paste credentials into chat, and rotate affected tokens if the file is exposed.

Risk: A full-instance or write-capable key can exercise broad access through the available Canonry tools.

Mitigation: Use the narrowest project-scoped or read-only keys that fit the task, and do not work around missing tools or 403 responses by switching credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry website](https://canonry.ai)
- [Canonry documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [AEO Analysis](references/aeo-analysis.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [Google Business Profile](references/google-business-profile.md)
- [Google Marketing](references/google-marketing.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [Server-side traffic](references/server-side-traffic.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 22.14+, the globally installed @canonry/canonry package, and canonry-mcp on PATH.]

## Skill Version(s):

4.177.1+9308d51 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
