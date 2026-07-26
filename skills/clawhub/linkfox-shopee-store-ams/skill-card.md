## Description: <br>
Provides agent guidance and Python wrappers for authorized Shopee store Affiliate Marketing Solutions workflows, including campaign, affiliate, commission, and performance operations through LinkFox. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and ecommerce teams use this skill to inspect and manage Shopee Affiliate Marketing Solutions campaigns for authorized stores, including Open Campaign, Targeted Campaign, affiliate lists, commission settings, and performance reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Shopee shop campaign settings through AMS operations. <br>
Mitigation: Confirm each mutating action before execution and review request bodies for the intended shop, campaign, products, affiliates, and commission settings. <br>
Risk: Full API responses may include sensitive shop, campaign, affiliate, or performance data and are saved persistently. <br>
Mitigation: Use trusted workspaces, keep API keys in environment variables, avoid sharing real tokens, and delete generated linkfox response files when no longer needed. <br>
Risk: The skill depends on authorized Shopee credentials and LinkFox proxy access. <br>
Mitigation: Verify the required authorization skill before use and restrict API keys to trusted agents and environments. <br>


## Reference(s): <br>
- [Shopee AMS API reference](references/api.md) <br>
- [Shopee Open Platform AMS documentation](https://open.shopee.com/documents/v2/v2.ams.get_open_campaign_added_product?module=127&type=1) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-ams) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with Python shell commands and JSON request/response data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save full API responses under a linkfox session data directory and print small responses or summaries to stdout.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
