## Description: <br>
Extracts consumer insights from Amazon reviews using ZooData, including pain points, buying factors, user profiles, usage patterns, competitor sentiment comparisons, and listing copy suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, ecommerce analysts, marketplace operators, and product teams use this skill to turn Amazon ASIN, category, keyword, marketplace, date, and filter inputs into review intelligence reports for product improvement, competitive analysis, and listing optimization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon research inputs and a ZooData API key are used with ZooData network calls. <br>
Mitigation: Install and run the skill only when that data sharing is acceptable, keep ZOODATA_API_KEY scoped appropriately, and use the documented ZooData endpoints for this workflow. <br>
Risk: Broad review, category, or competitor scans can consume ZooData credits. <br>
Mitigation: Estimate credit usage before multi-call scans and confirm broad or ambiguous requests before execution. <br>
Risk: The bundled shared CLI exposes additional ZooData research commands beyond the review-intelligence workflow. <br>
Mitigation: Limit agent usage to the commands and endpoints documented for this skill's Amazon review-intelligence tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-review-intelligence-extractor) <br>
- [Publisher profile](https://clawhub.ai/user/apiclaw) <br>
- [ZooData-Skills repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API base](https://api.zoodata.ai/openapi/v2) <br>
- [API field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands and structured API usage tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should disclose ZooData sampling, credit usage, credential requirements, and confidence labels for review-derived conclusions.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
