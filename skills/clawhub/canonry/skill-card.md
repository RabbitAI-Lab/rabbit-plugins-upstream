## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to operate Canonry workflows for AI visibility evidence, diagnostics, measurement planning, integrations, and reporting. It provides host-native CLI guidance and reference material while preserving Canonry's server-side authority and approval boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill references powerful Canonry integrations and commands that can affect settings, schedules, ads, WordPress, Cloudflare routes, webhooks, or external syncs.

Mitigation: Use read-only or narrowly scoped credentials where possible and approve only the exact target, action, and bounded scope before running any write, sync, schedule, or externally visible operation.

Risk: Credentials or local configuration details could be exposed if copied into chat, reports, tool arguments, or public guidance.

Mitigation: Keep secrets out of chat and public outputs, use secure setup flows, and check permissions on ~/.canonry/config.yaml before using local Canonry configuration.

## Reference(s):

- [Canonry Operations Guide v1](SKILL.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [ClawHub skill page](https://clawhub.ai/arberx/skills/canonry)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline CLI commands and operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; referenced actions require Canonry credentials, permissions, and explicit approval for the exact target and scope.]

## Skill Version(s):

5.13.0+894086f (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
