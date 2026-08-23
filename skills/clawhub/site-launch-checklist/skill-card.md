## Description:

Pre-launch checklist for shipping a new website, covering analytics, legal compliance, security headers, SEO/GEO setup, copy review, social previews, favicon and manifest assets, quality gates, and optional weekly SEO maintenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, site owners, and launch teams use this skill to run an interactive production-readiness audit before a website goes live. It helps verify infrastructure, analytics, legal/compliance pages, security headers, SEO files, copy quality, social metadata, icons, accessibility, performance, and optional weekly SEO monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional weekly SEO agent can create recurring automation that uses local credentials or MCP access.

Mitigation: Review the weekly SEO agent before enabling it, prefer scoped MCP credentials, and avoid unattended runs with broad write or shell permissions.

Risk: Weekly SEO reports may be posted to Slack when a webhook is configured.

Mitigation: Configure Slack only when report contents are safe to share in that channel, and omit the webhook for sensitive sites.

Risk: Companion skills and MCP servers can expand the active toolchain and permission surface.

Mitigation: Inspect companion skills before installing them, install only confirmed sub-skills, and require explicit user confirmation for each install.

Risk: The security evidence classifies the release as Review because of the optional weekly SEO automation behavior.

Mitigation: Follow the security guidance before deployment: review the agent, use scoped credentials, avoid broad unattended permissions, and confirm reporting destinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/site-launch-checklist)
- [Project homepage](https://github.com/samber/cc-skills)
- [Weekly SEO maintenance sub-agent](references/weekly-seo-agent.md)
- [Launch templates](references/templates.md)
- [Decisions and matrices](references/decisions.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, file templates, and optional agent configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce launch readiness reports, checklist status summaries, TONE.md guidance, robots.txt and manifest templates, security header snippets, and weekly SEO agent configuration.]

## Skill Version(s):

1.2.0 (source: evidence release.version, SKILL.md frontmatter, target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
