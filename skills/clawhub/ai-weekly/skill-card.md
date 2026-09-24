## Description:

AI Weekly Report helps agents collect AI industry news from RSS feeds and generate a searchable, filterable, dark-mode single-file HTML report with source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agent users use this skill to produce sourced AI news briefings, lightweight Markdown summaries, static HTML reports, and optional deployment or Feishu delivery guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment and scheduling paths may use broad or persistent credentials.

Mitigation: Use short-lived or tightly scoped credentials, avoid storing GitHub personal access tokens in .github_token where possible, and run dry-run modes before publishing.

Risk: A maintenance script can make published reports vulnerable to injected JavaScript.

Mitigation: Do not publish reports modified by backfill_translations.py until the NEWS_DATA serialization issue is fixed and reviewed.

Risk: The skill fetches public news and can optionally post to Feishu, deploy to hosting providers, or create an OS scheduler task.

Mitigation: Enable delivery, deployment, and scheduling features only when the operator has reviewed the destination, credentials, and recurrence settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/elisabeth15501/skills/ai-weekly)
- [Publisher profile](https://clawhub.ai/user/elisabeth15501)
- [Project homepage](https://github.com/Elisabeth15501/ai-weekly)
- [Live report demo](https://elisabeth15501.github.io/ai-weekly/AI_News_2026-09-07.html)
- [FAQ](references/FAQ.md)
- [Data sources](references/data_sources.md)
- [Report structure](references/report_structure.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses, JSON data, shell commands, configuration snippets, and single-file HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports are intended to include source links and should label missing or fallback data instead of presenting it as real-time.]

## Skill Version(s):

3.6.1 (source: SKILL.md frontmatter, CHANGELOG, release notes, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
