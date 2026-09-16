## Description:

Guides SEO and AI-search visibility for Next.js, Astro, and React apps in Cursor, Claude Code, and Codex, including metadata, Open Graph, Twitter cards, Schema.org JSON-LD, sitemaps, robots.txt, optional llms.txt, keyword research, clustering, auditing, and stack-aware implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daniel-amekpoagbe](https://clawhub.ai/user/daniel-amekpoagbe)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement or audit SEO and AI-search visibility in Next.js, Astro, and React applications. It helps choose stack-appropriate patterns for metadata, structured data, sitemaps, robots.txt, optional llms.txt, keyword clustering, and validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated SEO and crawl-control changes can affect how public pages are indexed or presented by search engines and AI-search systems.

Mitigation: Review generated metadata, robots.txt, sitemap entries, llms.txt content, and placeholder domains before publishing.

Risk: Project-specific details such as production domains, social handles, locales, and target keywords may be missing or guessed.

Mitigation: Provide real site metadata and mark any remaining placeholders for developer review before deployment.

Risk: Client-rendered metadata may not be visible to crawlers or social preview fetchers that inspect only initial HTML.

Mitigation: Use prerendering or server-side rendering when indexable route content and metadata must appear in the initial response.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/daniel-amekpoagbe/react-seo-skills/tree/main/skill)
- [ClawHub skill page](https://clawhub.ai/daniel-amekpoagbe/skills/skill)
- [App Router - Metadata, Sitemap & Robots](references/app-router.md)
- [Pages Router - Metadata, Sitemap & Robots](references/pages-router.md)
- [Astro - Metadata, Sitemap, Robots, and JSON-LD](references/astro.md)
- [React & Vite - Metadata, Sitemap & Robots](references/react-vite.md)
- [react-helmet-async](references/react-helmet-async.md)
- [Structured Data - Schema.org JSON-LD](references/structured-data.md)
- [Keyword Clustering & Validation](references/keywords.md)
- [GEO - AI Visibility](references/geo.md)
- [Language Detection - JavaScript vs TypeScript](references/language.md)
- [Validation Tools](references/validation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks and file-change guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to public SEO files such as metadata components, JSON-LD helpers, sitemaps, robots.txt, and optional llms.txt.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
