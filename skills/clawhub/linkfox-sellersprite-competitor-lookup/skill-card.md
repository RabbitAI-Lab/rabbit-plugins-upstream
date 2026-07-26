## Description: <br>
Uses SellerSprite data to help Amazon sellers find and analyze competing products across 12 marketplaces, including sales, BSR, pricing, rating, and growth metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and ecommerce analysts use this skill to query SellerSprite competitor data by ASIN, keyword, seller, brand, or category and compare product performance metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon research terms, ASINs, seller, brand, category inputs, session metadata, and the LinkFox API key are sent to LinkFox-controlled endpoints. <br>
Mitigation: Use the skill only when those inputs are acceptable to share with LinkFox-controlled services, and avoid confidential product strategy unless that data handling is approved. <br>
Risk: The helper script persists full API responses locally, which may include sensitive competitor research data. <br>
Mitigation: Review the generated local JSON files, manage retention, and avoid running the skill in shared workspaces that should not store these results. <br>
Risk: Authentication or credit issues may lead the agent toward installing a separate onboarding skill from a remote ZIP. <br>
Mitigation: Confirm the source and need for any onboarding skill before installation, and prefer existing trusted authentication guidance when available. <br>
Risk: The service consumes paid LinkFox credits and repeated queries can increase cost. <br>
Mitigation: Confirm additional searches, pagination, or query changes with the user before making repeated calls. <br>


## Reference(s): <br>
- [卖家精灵-查竞品 API 参考](references/api.md) <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-competitor-lookup) <br>
- [LinkFox publisher profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell command examples, and saved JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script writes full API responses to local JSON files and prints either full JSON or a compact summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
