## Description:

Guides agents using Canonry MCP tools or the cnry CLI to inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and developers use this skill to examine stored Canonry evidence, investigate AI search visibility, and plan or review authorized measurement and integration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes or live integrations may change the wrong project, account, site, advertising setup, or traffic route.

Mitigation: Confirm the exact project, account, credential, action, and bounded scope before allowing writes, syncs, schedules, webhooks, ads changes, WordPress updates, or Cloudflare edits.

Risk: API keys, OAuth secrets, application passwords, and local tokens can be exposed during setup or troubleshooting.

Mitigation: Keep secrets out of chat and reports, and protect ~/.canonry/config.yaml with appropriate local permissions.

Risk: Provider reads and measurement runs may consume quota or create misleading comparisons if evidence is incomplete.

Mitigation: Get approval for bounded live work; check dates, sample sizes, and missing or stale evidence before interpreting results.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](artifact/references/canonry-cli.md)
- [Interpreting Canonry results](artifact/references/aeo-analysis.md)
- [Indexing workflows](artifact/references/indexing.md)
- [Server-side traffic setup](artifact/references/server-side-traffic.md)
- [Google Business Profile integration](artifact/references/google-business-profile.md)
- [Google Ads and Tag Manager guidance](artifact/references/google-marketing.md)
- [WordPress integration](artifact/references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Text and Markdown, with CLI commands when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advice and actions depend on connected tools, available project evidence, and approval scope.]

## Skill Version(s):

7.4.0+ecdc505 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
