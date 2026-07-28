## Description: <br>
Amazon Competitor Intelligence Monitor produces competitor intelligence reports and monitoring alerts for a defined Amazon competitor set using ZooData API scans and baseline diffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, ecommerce operators, and analysts use this skill to run focused Amazon competitor teardowns or recurring checks for ASINs, brands, or keywords, then turn ZooData results into market, pricing, review, inventory, listing, and alert guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs ZooData API calls that can consume paid account credits. <br>
Mitigation: Confirm estimated credit use before broad or multi-call scans, and use granular commands or Quick Check when operating under a credit cap. <br>
Risk: Bundled monitor-data sample files include an active baseline and config for a sample competitor watch list. <br>
Mitigation: Delete or replace the sample monitor-data files before using Quick Check so alerts are based on the user's own tracked ASINs. <br>
Risk: The skill reads ZooData credentials and supports a configurable API base URL. <br>
Mitigation: Set ZOODATA_API_KEY via environment variable, avoid shared credential config files, and only set ZOODATA_BASE_URL to a trusted host you control. <br>
Risk: Reports combine sampled marketplace data with inferred or directional business recommendations. <br>
Mitigation: Keep the required disclaimer and confidence labels, and validate important decisions with additional sources before acting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-competitor-intelligence-monitor) <br>
- [Project Homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API Key Setup](https://zoodata.ai/en/api-keys) <br>
- [Skill API Field Reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance, API Calls] <br>
**Output Format:** [Markdown reports with tables, alerts, inline shell commands, and data provenance/API usage sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; full scans use about 28-35 credits and quick checks use about 5-10 credits.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
