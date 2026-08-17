## Description:

Backlink profile analysis for referring domains, anchor text distribution, toxic link detection, and competitor gap analysis using Common Crawl, optional Moz and Bing Webmaster data, and the optional DataForSEO extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, marketers, and developers use this skill to audit backlink profiles, identify toxic or lost links, compare competitor link gaps, and plan link-building actions with source-labeled confidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analyzed domains and backlink data may be sent to third-party SEO services or crawlers when optional data sources are used.

Mitigation: Configure Moz, Bing Webmaster, and DataForSEO credentials only in intended environments and review data-sharing expectations before running audits.

Risk: Toxic-link and disavow recommendations can be incorrect or incomplete if source data is sparse or stale.

Mitigation: Treat recommendations as review inputs, require source-labeled evidence, and manually verify suspicious links before taking disavow or outreach actions.

Risk: A numeric backlink health score can be misleading when too few scoring factors have data.

Mitigation: Follow the skill's data sufficiency gate and report insufficient data instead of a numeric score when fewer than four of seven factors are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/seo-backlinks)
- [Bing Webmaster Tools](https://www.bing.com/webmasters)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance, Analysis]

**Output Format:** [Markdown report with tables, status sections, source labels, and inline command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should label data sources and confidence; numeric health scores are withheld when fewer than four of seven scoring factors have data.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact frontmatter metadata version 2.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
