## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results. Use this optional host-native skill for CLI workflows and detailed references; connected MCP users can operate through canonry_help without installing a local runtime or skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to inspect Canonry measurement evidence, diagnose visibility changes, plan analysis, review integrations, and report results. It provides optional CLI workflows and references for host-native use, while connected MCP users can work through Canonry tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed writes or recurring work may affect tracking, saved patterns, publishing, or settings.

Mitigation: Inspect the exact targets, costs, scope, and proposed changes; obtain explicit approval before executing writes or recurring work.

Risk: Integration setup and local configuration may expose credentials or grant access beyond the intended scope.

Mitigation: Enter secrets only through private setup flows, protect the local configuration file, and use project-scoped, stored-only access for analysis where possible.

Risk: Enabling server-side traffic collection transports visitor data.

Mitigation: Review the visitor data being transported before enabling collection, and revoke dedicated credentials when removing integrations.

## Reference(s):

- [Canonry Operations Guide](artifact/SKILL.md)
- [AEO Analysis: Interpreting Canonry Results](artifact/references/aeo-analysis.md)
- [Canonry CLI Reference](artifact/references/canonry-cli.md)
- [Google Business Profile Integration](artifact/references/google-business-profile.md)
- [Google Ads and GTM Evidence Boundaries](artifact/references/google-marketing.md)
- [Indexing Reference](artifact/references/indexing.md)
- [Server-Side Traffic Reference](artifact/references/server-side-traffic.md)
- [WordPress Integration](artifact/references/wordpress-integration.md)
- [Canonry on ClawHub](https://clawhub.ai/arberx/skills/canonry)
- [Google Business Profile API access prerequisites](https://developers.google.com/my-business/content/prereqs#request-access)
- [Google Business Profile API access request](https://support.google.com/business/contact/api_default)

## Skill Output:

**Output Type(s):** [text, markdown, analysis, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and reports, with shell commands and configuration examples where relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content depends on the requested Canonry workflow and available evidence.]

## Skill Version(s):

7.55.1+34bb1cc (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
