## Description:

Guides agents using Canonry MCP tools or the cnry CLI to inspect visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators and developers use this skill to navigate Canonry, evaluate stored AI-visibility evidence, and prepare scoped measurements, integration reviews, and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider tokens or other credentials could be exposed while configuring integrations.

Mitigation: Enter secrets only through private terminal or local configuration and use narrowly scoped credentials where possible.

Risk: Live reads can consume provider quota, and writes, deployments, or schedules can change external accounts.

Mitigation: Start with stored evidence and obtain approval for the exact target and bounded action before live calls or changes.

Risk: Retrying an operation with an uncertain outcome could duplicate an external change.

Mitigation: Inspect saved state or the operation receipt before retrying; stop when the outcome remains ambiguous.

## Reference(s):

- [Canonry CLI commands and return shapes](artifact/references/canonry-cli.md)
- [AEO evidence analysis](artifact/references/aeo-analysis.md)
- [Indexing workflows](artifact/references/indexing.md)
- [WordPress integration](artifact/references/wordpress-integration.md)
- [Server-side traffic](artifact/references/server-side-traffic.md)
- [Google Business Profile](artifact/references/google-business-profile.md)
- [Google Ads and Tag Manager](artifact/references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the available project evidence and authorized tools.]

## Skill Version(s):

6.3.0+a0351a3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
