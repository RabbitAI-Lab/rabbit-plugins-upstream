## Description: <br>
One-click market viability assessment for Amazon sellers that analyzes market size, competition intensity, brand landscape, pricing structure, and consumer pain points to deliver a GO/CAUTION/AVOID recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, marketplace operators, and commerce analysts use this skill to evaluate a named Amazon niche or category before market entry. It compares sub-markets, pulls ZooData-powered product and market signals, and returns a concise GO/CAUTION/AVOID decision with supporting rationale. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon market research inputs, ASINs, and review data are sent to ZooData under the user's ZooData account. <br>
Mitigation: Install only when this data sharing is acceptable and use a dedicated ZOODATA_API_KEY with only the needed scope. <br>
Risk: Review fallback runs can create temporary working directories containing review data. <br>
Mitigation: Delete /tmp review working directories after fallback runs when the data is sensitive. <br>
Risk: Broad or composite scans consume ZooData account credits. <br>
Mitigation: Confirm estimated credit use before multi-call scans and use granular commands when operating under a credit cap. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-market-entry-analyzer) <br>
- [ZooData-Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData pricing](https://zoodata.ai/en/pricing) <br>
- [ZooData API base URL](https://api.zoodata.ai/openapi/v2) <br>
- [CLI contract](references/cli-contract.md) <br>
- [Market Entry Analyzer API Field Reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown market-entry report with tables, confidence labels, data provenance, API usage, and GO/CAUTION/AVOID verdict] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and may consume ZooData account credits; review fallback can create temporary /tmp review working directories.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
