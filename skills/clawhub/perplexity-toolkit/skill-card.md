## Description:

Automate Perplexity AI search for batch searches, citation extraction, source aggregation, and result verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mfang0126](https://clawhub.ai/user/mfang0126)

### License/Terms of Use:

MIT

## Use Case:

Developers and researchers use this skill to run Perplexity searches through browser automation, process batches of queries, extract cited sources, and generate aggregate research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control a logged-in Perplexity browser session.

Mitigation: Use a dedicated browser profile or account, avoid sensitive account data, and review browser actions before running long batches.

Risk: Browser automation and anti-detection behavior may create account or terms-of-service risk.

Mitigation: Confirm that the intended use complies with Perplexity's terms, keep batch rates conservative, and avoid unattended high-volume runs.

Risk: The history command can delete Perplexity conversations.

Mitigation: Use dry-run mode first, back up important conversations, and target deletions with explicit query, URL, and limit settings.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mfang0126/skills/perplexity-toolkit)
- [Perplexity AI](https://www.perplexity.ai)
- [Perplexity Web Automation Skill](docs/SKILL.md)
- [Perplexity Intelligent Search Skill](docs/perplexity-search-skill.md)
- [Perplexity Pro Practical Guide](docs/reference-pro-guide.md)
- [Perplexity AI Browser Automation Mapping](docs/research/perplexity-browser-mapping.md)
- [Perplexity AI Capability Gap Analysis](docs/research/perplexity-capability-analysis.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text, JSON, and Markdown reports with CLI commands and Python API examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include answers, source URLs, follow-up questions, quality checks, batch result files, and aggregated source reports.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
