## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results. Use this optional host-native skill for CLI workflows and detailed references; connected MCP users can operate through canonry_help without installing a local runtime or skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use canonry to inspect AI visibility evidence, diagnose measurement changes, plan bounded measurement work, review integrations, and produce reports through Canonry MCP tools or the `cnry` CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive credentials may be involved when configuring analytics and integration providers.

Mitigation: Use read-only or narrowly scoped credentials where possible, avoid pasting real secrets into chat or shell commands, and prefer file, stdin, or dashboard OAuth flows for credential handling.

Risk: Broad agent or write authority could affect project-scoped analytics, integrations, or settings.

Mitigation: Restrict the agent scope to read-only unless a specific write is approved, and require approval for the exact target, action, and bounded work before live provider reads, syncs, sweeps, or mutations.

Risk: Server-side traffic workflows can route raw visitor data through Cloudflare direct-push paths.

Mitigation: Review the Cloudflare direct-push privacy tradeoff before routing visitor traffic through it, and use the documented bounded retention and source controls.

## Reference(s):

- [Canonry Operations Guide v1](SKILL.md)
- [CLI commands and JSON return shapes](references/canonry-cli.md)
- [Interpreting stored evidence and regressions](references/aeo-analysis.md)
- [Indexing workflow after inspection and approval](references/indexing.md)
- [Approved WordPress workflow](references/wordpress-integration.md)
- [Server-side traffic setup and diagnosis](references/server-side-traffic.md)
- [Google Business Profile prerequisites](references/google-business-profile.md)
- [Google Ads and GTM evidence boundaries](references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline CLI commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance; live reads, writes, provider calls, syncs, and externally visible actions require appropriate Canonry credentials and explicit approvals.]

## Skill Version(s):

5.1.3+1f10658 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
