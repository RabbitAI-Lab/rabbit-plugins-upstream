## Description:

Provides agent-facing access to Shopee Shop APIs for reading shop information, profile, warehouse, notification, reseller-brand, Brazil onboarding, and holiday-mode data, and for updating shop profile and holiday-mode settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and commerce agents use this skill to inspect authorized Shopee shop state and make supported shop-setting changes through LinkFox scripts. It is suited for workflows involving shop profile checks, warehouse and notification review, reseller-brand status, Brazil onboarding data, and holiday-mode management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access LinkFox/Shopee shop data and save full API responses locally.

Mitigation: Install only for trusted workflows, treat response files as sensitive business data, and periodically delete saved LinkFox response files when they are no longer needed.

Risk: The skill can change shop profile fields and holiday-mode settings.

Mitigation: Manually confirm every profile or holiday-mode change before execution, especially changes that affect ordering or public shop presentation.

Risk: The onboarding flow may handle API keys, SMS login, billing, and payment steps.

Mitigation: Treat generated API keys like passwords, prefer existing configured keys when possible, and avoid the SMS onboarding path unless it is necessary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-shop)
- [Shopee Shop API index](https://open.shopee.com/documents/v2/v2.shop.get_shop_info?module=92&type=1)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [get_shop_info](references/apis/get-shop-info.md)
- [get_profile](references/apis/get-profile.md)
- [update_profile](references/apis/update-profile.md)
- [set_shop_holiday_mode](references/apis/set-shop-holiday-mode.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses saved to local files, with stdout containing full JSON for small responses or summaries for larger responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses LinkFox API key environment variables and requires an authorized Shopee shop selected through the related auth skill.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
