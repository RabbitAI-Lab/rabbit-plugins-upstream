## Description: <br>
Provides agent-facing guidance and Python entry points for Shopee Open Platform Push operations through LinkFox, including push callback configuration, current configuration lookup, lost push message retrieval, and consumed-message confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and ecommerce operators use this skill to configure Shopee Push webhooks, inspect app push settings, retrieve lost push messages, and confirm consumed replay messages through LinkFox-managed Shopee API access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform state-changing Shopee Push operations such as setting webhook configuration and confirming consumed lost messages. <br>
Mitigation: Confirm the target shop or merchant, request body, and intended state change before running POST operations. <br>
Risk: Full API responses are retained locally in plaintext and may contain webhook, shop, merchant, or message data. <br>
Mitigation: Store generated linkfox data files outside source control, review them for sensitive contents, and delete or protect them according to local data handling requirements. <br>
Risk: The skill requires LinkFox API credentials and Shopee merchant access. <br>
Mitigation: Use least-privilege credentials where available and avoid sharing command output or saved response files that contain merchant data. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-push) <br>
- [API reference](references/api.md) <br>
- [Shopee Push set_app_push_config documentation](https://open.shopee.com/documents/v2/v2.push.set_app_push_config?module=105&type=1) <br>
- [Shopee Push get_app_push_config documentation](https://open.shopee.com/documents/v2/v2.push.get_app_push_config?module=105&type=1) <br>
- [Shopee Push get_lost_push_message documentation](https://open.shopee.com/documents/v2/v2.push.get_lost_push_message?module=105&type=1) <br>
- [Shopee Push confirm_consumed_lost_push_message documentation](https://open.shopee.com/documents/v2/v2.push.confirm_consumed_lost_push_message?module=105&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Files] <br>
**Output Format:** [Markdown guidance with Python command examples and JSON API responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session data directory; small responses may also be printed to stdout, while larger responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
