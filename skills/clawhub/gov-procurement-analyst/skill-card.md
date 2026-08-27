## Description:

A government procurement analysis assistant for opportunity discovery, bid decisions, document drafting, supplier due diligence, compliance checks, policy guidance, competitor profiling, scoring prediction, and local knowledge-base workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Bidders, procurement teams, and purchasing or agency users use this skill to discover public procurement opportunities, evaluate bid fit, draft and review bid materials, analyze supplier and competitor risk, and track government procurement outcomes. The skill is oriented to Chinese government procurement platforms and uses public data together with locally stored business context.

### Deployment Geography for Use:

China, for workflows involving Chinese government procurement data and platforms.

## Known Risks and Mitigations:

Risk: The skill may store business profiles, bid data, reports, and SQLite databases locally.

Mitigation: Use it only with approved business data, review local storage locations before production use, and define retention and deletion procedures.

Risk: The skill can crawl public procurement websites and may encounter rate limits, anti-scraping controls, or source-specific usage restrictions.

Mitigation: Limit collection to permitted public sources, respect rate limits and robots guidance, and disable collection against sources that require login or prohibit automated access.

Risk: Scheduled competitor monitoring and webhook pushes may expose procurement or business-sensitive information.

Mitigation: Disable scheduled pushes by default, review webhook destinations, and send notifications only to approved internal channels.

Risk: A PowerShell hot-update path can introduce unreviewed code if the update source is not verified.

Mitigation: Avoid hot updates unless the source is verified, pin reviewed releases, and rescan the skill after updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/gov-procurement-analyst)
- [Data Source Platforms and Compliance Guide](references/procurement-platforms.md)
- [Enterprise Profiling and Matching Algorithm Reference](references/enterprise-profiling.md)
- [Anti-Scraping Strategy and Data Collection Best Practices](references/anti-scraping-best-practices.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports with optional JSON data files, inline SVG charts, and generated Word or PDF documents when dependencies are available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local reports, procurement datasets, profiles, and SQLite knowledge bases during use.]

## Skill Version(s):

5.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
