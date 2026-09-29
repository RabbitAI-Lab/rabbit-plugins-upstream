## Description:

Guides agents using Canonry's connected tools or CLI to inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this guide to review saved Canonry evidence, investigate AI visibility changes, plan approved measurement or integration work, and prepare scoped reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live provider calls or research may spend quota or create new evidence even when described as reads.

Mitigation: Start with stored evidence and obtain approval for the exact target and bounded live work.

Risk: Writes, ads operations, schedules, or public content changes can have externally visible effects.

Mitigation: Require explicit approval for each scoped change, review previews where available, and inspect saved state before retrying uncertain writes.

Risk: Credentials used for connected integrations could be exposed in conversations or reports.

Mitigation: Use read-only or project-scoped credentials where possible and keep API keys in the operator's secure setup flow.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](references/canonry-cli.md)
- [Interpreting Canonry results](references/aeo-analysis.md)
- [Indexing workflows](references/indexing.md)
- [WordPress integration](references/wordpress-integration.md)
- [Server-side traffic](references/server-side-traffic.md)
- [Google Business Profile integration](references/google-business-profile.md)
- [Google Ads and Tag Manager](references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should state scope, dates, sample sizes, and missing or stale evidence.]

## Skill Version(s):

5.30.0+927559d (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
