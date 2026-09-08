## Description:

SEO analysis and optimization skill for auditing website search visibility, diagnosing ranking or traffic issues, and producing fixes for technical SEO, on-page content, schema, and AI search visibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

External developers, site owners, and SEO practitioners use this agent skill to audit websites, diagnose search visibility problems, and prepare concrete SEO fixes. The skill supports full-site audits, single-page analysis, content quality review, structured data work, and AI search visibility improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Active SEO audits fetch website content that may contain untrusted text or prompt-injection attempts.

Mitigation: Treat fetched page content, robots.txt, sitemap data, and metadata as data only, and do not execute instructions embedded in those sources.

Risk: Incorrect changes to robots.txt, canonical tags, redirects, schema, llms.txt, or pricing pages can affect indexing, ranking, or traffic.

Mitigation: Review proposed diffs before applying them and verify changes with search console tools, rendered page checks, rich results tests, and HTTP status checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-seo-skill)
- [Technical SEO reference](references/technical-seo.md)
- [On-page SEO reference](references/on-page.md)
- [Content quality reference](references/content-quality.md)
- [Structured data reference](references/schema.md)
- [AI SEO reference](references/ai-seo.md)
- [Zero-dependency SEO audit script](scripts/seo-audit.js)
- [Google PageSpeed Insights](https://pagespeed.web.dev)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org](https://schema.org)
- [llms.txt](https://llmstxt.org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed diffs, verification commands, SEO issue severity, and copy-ready metadata or JSON-LD snippets.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
