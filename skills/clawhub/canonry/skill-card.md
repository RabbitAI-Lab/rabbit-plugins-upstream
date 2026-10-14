## Description:

Guides agents using Canonry MCP tools or the optional CLI to inspect AI visibility evidence, diagnose changes, plan measurements, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, site operators, and their agents use Canonry to assess stored AI visibility and site evidence, investigate changes, plan approved measurements, and report findings without confusing unmeasured results with zero visibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider keys, integration credentials, or local configuration may be exposed during setup or reporting.

Mitigation: Keep secrets and ~/.canonry/config.yaml private; enter credentials through the operator's secure setup flow, not chat or reports.

Risk: Live reads and operational actions may consume quota or change external systems.

Mitigation: Prefer stored-only reads; obtain explicit approval for bounded writes, syncs, schedules, traffic capture, ad operations, and live provider work.

## Reference(s):

- [Canonry skill on ClawHub](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](references/canonry-cli.md)
- [Interpreting Canonry evidence](references/aeo-analysis.md)
- [Indexing workflow](references/indexing.md)
- [WordPress integration](references/wordpress-integration.md)
- [Server-side traffic](references/server-side-traffic.md)
- [Google Business Profile integration](references/google-business-profile.md)
- [Google Ads and Tag Manager](references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with optional CLI commands and evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves measurement scope, dates, sample sizes, and separate mention and citation signals.]

## Skill Version(s):

7.45.0+1c90811 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
