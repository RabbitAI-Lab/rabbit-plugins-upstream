## Description:

Guides agents using Canonry MCP tools or the cnry CLI to inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, developers, and agents use this guide to interpret Canonry evidence, investigate AI visibility, review connected marketing services, and prepare measurement plans and reports. Live operations and changes require explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad operations can change public websites, scheduled work, provider data, or ads.

Mitigation: Require explicit human approval for each bounded write, sync, schedule change, public website change, or ad activation.

Risk: Connected site and marketing account credentials may be exposed during setup or reporting.

Mitigation: Use read-only or project-scoped keys when possible, keep ~/.canonry/config.yaml private, and perform secret-bearing setup in a private terminal.

Risk: Live provider reads, probes, and research can consume quotas or persist evidence.

Mitigation: Start from stored evidence and obtain approval for the exact target and bounded live work before calling providers.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](references/canonry-cli.md)
- [AEO analysis](references/aeo-analysis.md)
- [Indexing workflow](references/indexing.md)
- [WordPress integration](references/wordpress-integration.md)
- [Server-side traffic](references/server-side-traffic.md)
- [Google Business Profile integration](references/google-business-profile.md)
- [Google Ads and Tag Manager](references/google-marketing.md)
- [Google Marketing setup guide](https://github.com/Canonry/canonry/blob/main/docs/google-marketing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish measured evidence from hypotheses and identify missing or stale inputs.]

## Skill Version(s):

5.34.0+728d007 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
