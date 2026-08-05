## Description: <br>
Scans Amazon category landscapes with ZooData to identify trending subcategories, emerging niches, demand shifts, brand consolidation, new entrant waves, price band migration, and margin changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, sellers, marketplace analysts, and agent operators use this skill to scan Amazon parent categories, rank rising subcategories, monitor trend signals, and prepare market-entry timing reports from ZooData API results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key and sends category, keyword, ASIN, marketplace, date, and numeric filter data to ZooData API endpoints. <br>
Mitigation: Install only when this data sharing is acceptable, use a scoped API key where possible, and avoid sending sensitive or unnecessary category inputs. <br>
Risk: The bundled ZooData command tool is broader than this skill's allowed trend-scanning workflow. <br>
Mitigation: Review the tool before deployment and restrict use to the documented categories, market, products, and check commands for this skill. <br>
Risk: Bundled scan-data includes preloaded monitoring state that may not match the installing user's intended categories. <br>
Mitigation: Inspect or clear the scan-data directory before first use and enable scheduled monitoring only for intentionally selected categories. <br>
Risk: ZooData API calls consume account credits, especially broad full scans. <br>
Mitigation: Estimate credit cost and confirm with the user before running multi-call scans or scheduled monitoring. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-market-trend-scanner) <br>
- [ZooData API Key Setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData API](https://api.zoodata.ai) <br>
- [ZooData Pricing](https://zoodata.ai/en/pricing) <br>
- [Market Trend Scanner API Field Reference](artifact/references/reference.md) <br>
- [ZooData CLI Contract](artifact/references/cli-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, endpoint provenance, API usage summaries, and optional scheduler configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports match the user's language and include confidence labels, sampling disclaimers, and credit usage when API results are available.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
