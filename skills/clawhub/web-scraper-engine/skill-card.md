## Description:

Web Scraper Engine helps agents plan and generate web-scraping workflows with Firecrawl, Playwright, Crawl4AI, and related tooling for search, extraction, browser interaction, batch crawling, and data export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and automation teams use this skill to design scraping jobs for authorized websites, including competitor analysis, price monitoring, content collection, lead generation, market research, and structured extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide authenticated browser automation and handling of cookies, tokens, or login sessions.

Mitigation: Require explicit user confirmation before using credentials or session material, and avoid logging or exporting secrets.

Risk: The skill can propose scraping workflows that use proxies, stealth settings, form submission, or high-volume crawling.

Mitigation: Use it only on targets the user is authorized to access, confirm robots.txt and terms of service, and apply conservative rate limits.

Risk: The skill can generate exports or database writes that may contain sensitive scraped data.

Mitigation: Review fields before export or upload, minimize collected data, and redact sensitive values from files and reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/web-scraper-engine)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Markdown, JSON, Files]

**Output Format:** [Markdown guidance with generated code examples, shell commands, configuration notes, and structured data exports such as JSON, CSV, and Parquet.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose browser automation, API usage, schema-based extraction, file exports, and database writes depending on user input and available tools.]

## Skill Version(s):

1.0.1 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
