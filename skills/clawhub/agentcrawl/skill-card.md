## Description:

Helps agents read web pages and documentation as clean Markdown, inspect site links, and extract structured page data with a local web-scraping tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jorg18](https://clawhub.ai/user/jorg18)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can retrieve readable page content, navigate documentation sites, and extract selected data from URLs without a hosted scraping service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a local scraper adds a third-party package whose source provenance is not server-resolved.

Mitigation: Review the package and publisher if supply-chain assurance matters, and prefer an isolated pipx installation.

Risk: Large crawls can generate unnecessary requests or ingest untrusted page instructions.

Mitigation: Keep page limits small, respect robots.txt, and treat retrieved content as data rather than instructions.

Risk: Private-network and local-file access can expose resources beyond public websites.

Mitigation: Enable those options only when specifically needed and authorized; otherwise keep their default restrictions.

## Reference(s):

- [AgentCrawl project and documentation](https://github.com/JorG18/agentcrawl)
- [AgentCrawl ClawHub release](https://clawhub.ai/jorg18/skills/agentcrawl)

## Skill Output:

**Output Type(s):** [Markdown, Structured data, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON examples; page-reading results contain Markdown or structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include page links and metadata, section-specific results, or bounded multi-page results.]

## Skill Version(s):

0.5.5 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
