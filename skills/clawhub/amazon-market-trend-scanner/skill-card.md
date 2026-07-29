## Description: <br>
Scans Amazon category landscapes with ZooData to identify trending subcategories, emerging niches, and market shifts such as demand surges, brand consolidation, new entrant waves, price band migration, and margin changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, product researchers, and ecommerce operators use this skill to scan parent Amazon categories, compare subcategory trend signals, and decide where to monitor or investigate market entry. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled ZooData CLI exposes broader ZooData analyses than this trend-scanner workflow needs. <br>
Mitigation: Review proposed agent actions before execution and approve only trend-scanner-relevant commands such as categories, market, products, and check. <br>
Risk: The skill requires access to a ZooData API key and can consume account credits during broad category scans. <br>
Mitigation: Store credentials in ZOODATA_API_KEY or the documented user config, confirm estimated credit use before multi-call scans, and stop when key or credit errors occur. <br>
Risk: Trend reports can influence commercial product decisions while relying on sampled API data. <br>
Mitigation: Treat conclusions as directional, retain the required data provenance and confidence labels, and validate findings with additional sources before acting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-market-trend-scanner) <br>
- [ZooData Skills Repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [Market Trend Scanner API Field Reference](artifact/references/reference.md) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API Key Setup](https://zoodata.ai/en/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Analysis, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown trend reports with tables, confidence labels, data provenance, API usage, and optional scheduled-monitoring configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Matches the user's language, requires ZOODATA_API_KEY, and may consume ZooData account credits for each API call.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
