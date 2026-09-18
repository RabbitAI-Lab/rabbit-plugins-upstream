## Description:

Real-time competitive intelligence and market research using Bright Data's web scraping infrastructure to analyze competitors' pricing, features, reviews, hiring patterns, content strategy, and market positioning with live web data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meirk-brd](https://clawhub.ai/user/meirk-brd)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to gather live competitive data, compare products and markets, build battlecards, and turn observed pricing, review, hiring, SEO, and positioning signals into sourced strategic recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup command pipes a remote installer directly into Bash.

Mitigation: Use a signed or package-managed Bright Data CLI install path when available, or download and verify the installer before executing it.

Risk: Competitive research queries and target URLs are sent to Bright Data through the bdata CLI.

Mitigation: Use the skill only for data that may be shared with Bright Data, and avoid including confidential strategy, customer, or unreleased product details in queries.

Risk: The skill requires bdata login credentials on the local system.

Mitigation: Confirm where credentials are stored, limit access to the account used for research, and document how to revoke or remove stored credentials.

## Reference(s):

- [Analysis Frameworks](references/analysis-frameworks.md)
- [Data Source Selection Guide](references/data-source-guide.md)
- [Industry Signal Interpretation Guide](references/industry-signals.md)
- [Output Templates](references/output-templates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown reports with sourced analysis, tables, strategic recommendations, and inline shell commands when data collection is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are expected to include source URLs, a data collection date, clear gaps when data is unavailable, and strategic recommendations.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
