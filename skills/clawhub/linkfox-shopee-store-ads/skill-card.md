## Description: <br>
Helps agents work with Shopee in-store advertising for authorized shops, including ad balance checks, CPC and campaign performance reports, manual product ads, GMS campaigns, keyword recommendations, and campaign edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Shopee sellers, e-commerce operators, and developers use this skill to inspect ad account balances, retrieve advertising performance reports, and create or edit product ad campaigns for stores they have authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or edit live Shopee advertising campaigns for authorized accounts. <br>
Mitigation: Require explicit user approval before campaign create or edit calls and use only Shopee ad accounts the user intends the agent to manage. <br>
Risk: Full Shopee Ads API responses are persistently stored in local linkfox response folders. <br>
Mitigation: Review before installing in workspaces with sensitive business data and periodically delete retained response folders when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-ads) <br>
- [Shopee Ads API reference](references/api.md) <br>
- [Shopee Open Platform Ads documentation](https://open.shopee.com/documents/v2/v2.ads.get_total_balance?module=117&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, JSON files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and saved JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save full API responses under a local linkfox response folder and may print either full JSON or summaries depending on response size.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
