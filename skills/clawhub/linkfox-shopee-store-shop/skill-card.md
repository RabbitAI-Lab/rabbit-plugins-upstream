## Description: <br>
Helps agents work with authorised Shopee stores by querying shop information, profile details, warehouse data, seller notifications, authorised reseller brands, Brazil onboarding status, and holiday-mode settings, and by updating supported shop profile or holiday-mode fields. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace operators, developers, and ecommerce support agents use this skill to inspect and manage authorised Shopee shop metadata and selected settings from an agent workflow. It is most useful for checking profile, warehouse, notification, reseller brand, Brazil KYC, and holiday-mode state before making store-management changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform live store-changing actions such as profile edits and holiday-mode changes. <br>
Mitigation: Manually confirm the exact target shop and requested write parameters before running update_profile or set_shop_holiday_mode. <br>
Risk: Full Shopee shop API responses may contain sensitive business information and are saved persistently on disk. <br>
Mitigation: Store outputs only in an appropriate workspace and periodically delete linkfox session data that is no longer needed. <br>
Risk: Use requires access to the LinkFox/Shopee store API flow and related credentials. <br>
Mitigation: Install and use only when the operator is comfortable granting that access, and keep API keys in environment variables rather than command text or committed files. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-shop) <br>
- [Skill API reference](references/api.md) <br>
- [Shopee Open Platform Shop API index](https://open.shopee.com/documents/v2/v2.shop.get_shop_info?module=92&type=1) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python or shell command examples and JSON API results saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Small responses may be printed inline; larger responses are summarized while full JSON is saved under a linkfox session directory.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
