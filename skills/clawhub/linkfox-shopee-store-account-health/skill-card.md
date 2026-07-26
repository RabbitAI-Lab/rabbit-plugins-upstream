## Description: <br>
Shopee-店铺健康 helps agents query authorized Shopee store account-health metrics, penalty points, punishments, late orders, and listings with issues through LinkFox's Shopee developer proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Shopee sellers, operators, and support agents use this skill to inspect account-health status for authorized stores and investigate performance metrics, penalty history, punishments, late orders, and listings with issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can save full Shopee account-health responses locally, which may include sensitive store and operational data. <br>
Mitigation: Run it only in workspaces intended for this data, protect generated linkfox session files, and delete them when no longer needed. <br>
Risk: The skill depends on LinkFox and Shopee credentials to access authorized store data. <br>
Mitigation: Use it only for stores the user is allowed to inspect, keep API keys in environment variables, and avoid sharing generated outputs unnecessarily. <br>
Risk: Security evidence reports unclear cost and storage behavior for API calls and saved results. <br>
Mitigation: Confirm expected API credit use before additional calls and avoid repeated probing unless the user explicitly approves. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-account-health) <br>
- [Artifact API reference](artifact/references/api.md) <br>
- [Shopee Account Health API reference](https://open.shopee.com/documents/v2/v2.account_health.get_shop_performance?module=103&type=1) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with Python command examples; scripts emit JSON or summarized text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials and the linkfox-shopee-store-auth dependency; full API responses are saved locally under a linkfox session directory.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
