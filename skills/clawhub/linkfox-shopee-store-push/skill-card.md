## Description:

Enables agents to configure and inspect Shopee Open Platform Push settings, retrieve lost push messages, and confirm consumed lost messages through LinkFox's Shopee developer proxy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators working with Shopee stores use this skill to manage Push callback configuration and recover missed Push messages through LinkFox-mediated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Shopee store requests through LinkFox and requires LinkFox API key access.

Mitigation: Install only in environments where LinkFox is trusted, keep API keys in controlled environment variables, and avoid exposing workspace logs or saved outputs.

Risk: Onboarding and billing recovery can use or generate LinkFox API keys and may create payment orders.

Mitigation: Use onboarding only when authentication or billing recovery is needed, review any payment step before proceeding, and keep generated credentials private.

Risk: Saved response files may contain store, webhook, or Push message data.

Mitigation: Run the skill in a private workspace and delete, restrict, or encrypt saved linkfox response files after use.

Risk: Endpoint override environment variables can redirect API traffic.

Mitigation: Do not set endpoint override variables unless intentionally routing to a trusted endpoint.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-push)
- [Shopee Push set_app_push_config](https://open.shopee.com/documents/v2/v2.push.set_app_push_config?module=105&type=1)
- [Shopee Push get_app_push_config](https://open.shopee.com/documents/v2/v2.push.get_app_push_config?module=105&type=1)
- [Shopee Push get_lost_push_message](https://open.shopee.com/documents/v2/v2.push.get_lost_push_message?module=105&type=1)
- [Shopee Push confirm_consumed_lost_push_message](https://open.shopee.com/documents/v2/v2.push.confirm_consumed_lost_push_message?module=105&type=1)
- [API Reference](references/api.md)
- [Onboarding and Billing Recovery](references/onboarding.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses, saved response files, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are written to local linkfox response files; small responses may also be printed inline, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
