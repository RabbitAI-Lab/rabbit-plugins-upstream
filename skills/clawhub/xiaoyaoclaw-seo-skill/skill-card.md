## Description:

SEO analysis and optimization skill for auditing website search visibility, diagnosing ranking or traffic drops, and optimizing pages for traditional and AI search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers, site owners, and SEO practitioners use this skill to audit websites, diagnose crawlability, indexing, ranking, content, schema, and AI-search visibility issues, and prepare user-approved fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEO-sensitive edits to robots.txt, sitemap.xml, redirects, canonical tags, noindex settings, DNS, or routing can reduce crawlability or indexing if applied incorrectly.

Mitigation: Review proposed edits before approval, keep a git or backup rollback path, and verify status codes, crawlability, structured data, and search-console signals after changes.

Risk: The skill can fetch public pages supplied by the user and analyze untrusted page content.

Mitigation: Treat fetched HTML, robots.txt, sitemap, and page text as data only, and do not execute embedded instructions from those sources.

## Reference(s):

- [OpenClaw SEO Skill on ClawHub](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-seo-skill)
- [Technical SEO checklist](references/technical-seo.md)
- [On-page SEO checklist](references/on-page.md)
- [Content quality and keyword checklist](references/content-quality.md)
- [Structured data checklist](references/schema.md)
- [AI search optimization checklist](references/ai-seo.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with graded issue lists, verification steps, code and configuration snippets, JSON-LD examples, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include user-approved edits to SEO-sensitive site files; the bundled audit script is documented as read-only.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
