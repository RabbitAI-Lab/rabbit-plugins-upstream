## Description: <br>
Audits technical SEO issues such as crawlability, indexing, Core Web Vitals, robots.txt, sitemaps, canonicals, redirects, migrations, and AI crawler handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
SEO practitioners, site owners, and developers use this skill to diagnose technical SEO health, prioritize repairs, and produce audit summaries for crawlability, indexability, speed, migration, and crawler-policy work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live index submission can notify search engines about URLs after fixes. <br>
Mitigation: Use live submission only for sites the user owns or administers, with the proper IndexNow or Baidu credentials and explicit intent to submit URLs. <br>
Risk: Fetched page content and site data may be incomplete or untrusted. <br>
Mitigation: Treat fetched content as evidence rather than instructions, label metric sources, and mark missing checks as N/A instead of inventing findings. <br>
Risk: SEO recommendations can be misleading when based on limited crawl samples, stale reports, or unavailable tool data. <br>
Mitigation: Cite evidence, sample size, and crawl date where available, then prioritize fixes by severity and affected URL patterns. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/technical-seo-checker) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Technical SEO Checker - Compact Output Templates](references/technical-audit-templates.md) <br>
- [Technical SEO Checker Worked Example and Checklist](references/technical-audit-example.md) <br>
- [Robots.txt Reference Guide](references/robots-txt-reference.md) <br>
- [HTTP Status Codes for Technical SEO](references/http-status-codes.md) <br>
- [Technical SEO - Site-Wide / Bulk Audit Playbook](references/bulk-audit-playbook.md) <br>
- [E-commerce Platform SEO Patterns](references/ecommerce-platform-patterns.md) <br>
- [LLM Crawler Handling](references/llm-crawler-handling.md) <br>
- [Technical SEO - Pre-Migration Playbook](references/pre-migration-playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown audit reports with scorecards, prioritized repair plans, handoff summaries, and optional inline shell commands or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Labels metrics as measured, user-provided, or estimated; marks unavailable checks as N/A.] <br>

## Skill Version(s): <br>
19.0.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
