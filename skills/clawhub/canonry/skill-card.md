## Description:

Canonry helps agents use connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, marketers, SEO/AEO analysts, and developers use this skill to guide Canonry workflows for status checks, diagnostics, measurement planning, integrations, and reporting while preserving evidence boundaries and approval requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers workflows that may handle SEO, ads, analytics, traffic, website integrations, credentials, and visitor metadata.

Mitigation: Use read-only or project-scoped keys where possible, keep secrets out of chats and command lines, pin third-party tooling, and review the Cloudflare traffic path before sending visitor metadata to a public Canonry receiver.

Risk: Visitor-traffic collection can expose more data than necessary if sources or routes are too broad.

Mitigation: Limit traffic collection to the specific project and source needed, review data paths before deployment, and prefer the least-privileged integration mode that satisfies the task.

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

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be bounded by stored evidence, exact project scope, and operator approval for live reads, writes, syncs, or externally visible actions.]

## Skill Version(s):

4.192.3+cd66f63 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
