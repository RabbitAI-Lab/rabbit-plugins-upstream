## Description:

蓝海扫描专家 helps Amazon sellers evaluate a category keyword or ASIN with multi-source market insight, keyword validation, trend analysis, competitive scanning, Top ASIN breakdowns, profit estimates, and HTML category reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to decide whether a category, search term, or ASIN-related market is worth entering or revisiting. It gathers and cross-checks marketplace, search trend, competitive, supplier, and margin signals, then returns an HTML market report path plus a concise summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox credentials and calls LinkFox services.

Mitigation: Install only when a LinkFox API key can be provided intentionally, keep API keys private, and do not point gateway or onboarding override variables at untrusted hosts.

Risk: The skill may write full raw market-analysis results to a local linkfox directory.

Mitigation: Review local output directories before sharing the workspace and avoid entering sensitive product or account details unless they are needed for the analysis.

Risk: Some flows can create scheduled tasks, public upload URLs, onboarding actions, or billing-related steps.

Mitigation: Confirm user intent before enabling scheduling, public uploads, SMS-code entry, or payment steps, and prefer self-service account setup where possible.

Risk: Reports depend on third-party market data sources that can fail, return partial data, or use different measurement definitions.

Mitigation: Treat the report as decision support, review sections marked as missing or degraded, and verify key commercial assumptions before acting on the results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-blue-ocean-market-scanner)
- [LinkFox Skills](https://skill.linkfox.com/)
- [Output contract](artifact/skills/amazon-niche-radar/references/output-schema.md)
- [Amazon niche radar workflow](artifact/skills/amazon-niche-radar/SKILL.md)
- [Data fields](artifact/skills/amazon-niche-radar/references/data-fields.md)
- [Report layout extensions](artifact/skills/amazon-niche-radar/references/layout-extensions.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [HTML report file with a text summary and local report path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intermediate JSON data may be written under a local linkfox data directory; long reports are generated through the bundled report generator.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
