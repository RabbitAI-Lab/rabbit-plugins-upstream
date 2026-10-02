## Description:

Guides agents using Canonry MCP tools or the cnry CLI to inspect AI visibility evidence, diagnose changes, plan measurements, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to review Canonry project evidence, investigate visibility changes, prepare measurements, and report results without conflating stored evidence with new measurements or approved actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Integrations and write actions can change WordPress, ads, webhooks, or deployment settings.

Mitigation: Get operator approval before changes; use read-only access until writes are needed.

Risk: New measurements can spend provider quota and persist evidence.

Mitigation: Agree on scope and obtain approval before running measurements.

Risk: Provider setup can involve sensitive credentials.

Mitigation: Keep keys in the operator's secure setup flow, not agent chat or reports.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](references/canonry-cli.md)
- [AEO analysis](references/aeo-analysis.md)
- [Indexing workflow](references/indexing.md)
- [WordPress integration](references/wordpress-integration.md)
- [Server-side traffic](references/server-side-traffic.md)
- [Google Business Profile](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [Google Marketing setup guide](https://github.com/Canonry/canonry/blob/main/docs/google-marketing.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text and Markdown with optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports preserve evidence scope, dates, and sample sizes.]

## Skill Version(s):

6.1.2+3a39895 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
