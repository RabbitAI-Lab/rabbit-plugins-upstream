## Description: <br>
Amazon category trend scanner that uses ZooData to scan category landscapes for trending subcategories, emerging niches, demand surges, brand consolidation, price-band migration, and margin changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and marketplace operators use this skill to scan Amazon parent categories, compare subcategory trend signals, identify hot niches, and generate monitoring guidance backed by ZooData API sampling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The published skill is labeled as a trend scanner, but security evidence says it includes broader ZooData research commands and a mismatched market-entry reference file. <br>
Mitigation: Review the bundled command surface before use and constrain agent runs to the trend-scanning workflow unless the broader research commands are explicitly intended. <br>
Risk: Using the skill requires a ZooData-compatible API key and sends category, keyword, ASIN, and other commercial research queries to ZooData. <br>
Mitigation: Install only when that data sharing is acceptable, manage the ZOODATA_API_KEY as a secret, and avoid entering sensitive or proprietary research terms unless approved. <br>
Risk: Trend reports rely on sampled marketplace data and may include directional recommendations that are not sufficient for business decisions by themselves. <br>
Mitigation: Preserve the skill's required confidence labels and data-provenance tables, then validate important decisions with additional sources before acting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-market-trend-scanner) <br>
- [ZooData Skills Homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API Key Setup](https://zoodata.ai/en/api-keys) <br>
- [Market Trend Scanner Reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports with tables, CLI command suggestions, and optional monitoring configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include data provenance, API usage, confidence labels, and ZooData credit consumption when available.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
