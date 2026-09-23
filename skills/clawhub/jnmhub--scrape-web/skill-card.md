## Description:

Fetches web page content with Python and Scrapling, with support for simple CSS selectors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jnmhub](https://clawhub.ai/user/jnmhub)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to retrieve page text, extract simple CSS selector results, or save scraped output for downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch any URL reachable from the host, including sensitive internal or metadata endpoints.

Mitigation: Use it only where outbound scraping is acceptable and avoid internal, administrative, or cloud-metadata URLs.

Risk: The optional output path can overwrite local data.

Mitigation: Review the output path before execution and write only to intended working directories.

Risk: The skill depends on mutable third-party scraping components.

Mitigation: Pin or review dependencies before use in sensitive or production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jnmhub/skills/scrape-web)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text or saved text file, with command guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write scraped content to a local output file when requested.]

## Skill Version(s):

1.0.0 (source: release metadata; artifact frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
