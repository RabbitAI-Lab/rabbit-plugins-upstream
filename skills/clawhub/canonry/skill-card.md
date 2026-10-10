## Description:

Guides agents using Canonry MCP tools or the cnry CLI to inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this guide to interpret stored Canonry evidence, troubleshoot visibility changes, plan approved measurement, review connected services, and prepare scoped reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials or local configuration may be exposed during provider or integration setup.

Mitigation: Keep secrets out of chat and reports; use the operator's secure setup flow, limit credential scopes, and protect local Canonry configuration.

Risk: Live provider reads and measurement actions may consume quota, while syncs or writes may change connected services.

Mitigation: Inspect stored evidence first and confirm the exact target, action, and bounded work before any live read, write, or sync.

Risk: Ambiguous write results or incomplete evidence may lead to duplicate changes or misleading conclusions.

Mitigation: Check saved state or operation receipts before retrying, and disclose stale or missing evidence in reports.

## Reference(s):

- [Canonry ClawHub release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](artifact/references/canonry-cli.md)
- [Interpreting AI visibility evidence](artifact/references/aeo-analysis.md)
- [Indexing workflow](artifact/references/indexing.md)
- [WordPress integration](artifact/references/wordpress-integration.md)
- [Server-side traffic](artifact/references/server-side-traffic.md)
- [Google Business Profile integration](artifact/references/google-business-profile.md)
- [Google Ads and Tag Manager](artifact/references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown reports, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves evidence scope, time windows, sample sizes, and uncertainty in reports.]

## Skill Version(s):

7.23.0+8c7755d (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
