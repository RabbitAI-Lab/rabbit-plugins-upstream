## Description:

Helps agents configure and inspect Shopee Open Platform Push callbacks, retrieve lost push messages, and confirm consumed lost push messages through LinkFox's Shopee gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and e-commerce operators use this skill to manage Shopee store Push configuration, replay missed Push messages, and troubleshoot authentication or balance issues needed to complete those workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a LinkFox API key and calls LinkFox/Shopee gateway services.

Mitigation: Install only when the operator accepts those external service calls, keep API keys out of shared logs or transcripts, and rotate exposed credentials.

Risk: The skill can save complete API responses locally, which may include operational or account data.

Mitigation: Review the generated linkfox output directory, limit access to saved response files, and remove files that are no longer needed.

Risk: The artifact includes onboarding, SMS login, API-token generation, and billing/payment recovery flows beyond core Push operations.

Mitigation: Run those flows only when authentication or balance errors require them, and review payment-order details before sharing or acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-push)
- [Shopee Push API reference](artifact/references/api.md)
- [set_app_push_config](artifact/references/apis/set-app-push-config.md)
- [get_app_push_config](artifact/references/apis/get-app-push-config.md)
- [get_lost_push_message](artifact/references/apis/get-lost-push-message.md)
- [confirm_consumed_lost_push_message](artifact/references/apis/confirm-consumed-lost-push-message.md)
- [Shopee Open Platform Push documentation](https://open.shopee.com/documents/v2/v2.push.set_app_push_config?module=105&type=1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses or response summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may save full API responses in a local linkfox session directory and print either full JSON or a concise summary to stdout.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
