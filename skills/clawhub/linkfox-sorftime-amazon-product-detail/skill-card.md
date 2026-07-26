## Description: <br>
Queries Sorftime data by ASIN to retrieve Amazon product details and historical trends for sales, pricing, BSR rankings, profit, FBA fees, and promotions across supported marketplaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and agent users use this skill to inspect known ASINs, compare product-level performance, and summarize Sorftime product detail or trend data. It is intended for ASIN-based analysis, not broad product discovery or advertising strategy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ASIN query parameters and product research requests are sent to LinkFox/Sorftime services. <br>
Mitigation: Use the skill only for data that may be shared with those services, and avoid submitting confidential product research without approval. <br>
Risk: The skill reads a LinkFox API key from environment variables. <br>
Mitigation: Provide scoped credentials where available, rotate keys regularly, and avoid exposing environment variables in logs or shared shells. <br>
Risk: Product research results may be saved locally as JSON files. <br>
Mitigation: Run the skill in an approved workspace, review saved files before sharing the workspace, and delete cached or session data when retention is not needed. <br>
Risk: The skill may report feedback to a separate LinkFox endpoint and includes troubleshooting guidance to install another skill. <br>
Mitigation: Review or disable feedback and onboarding-install behavior before deployment in environments that require strict outbound-data or installed-skill controls. <br>


## Reference(s): <br>
- [Sorftime Product Detail API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sorftime-amazon-product-detail) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell commands, and JSON API responses or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script may save full API responses as local JSON files and print either full JSON or a concise summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
