## Description:

Helps agents query and manage authorized Shopee shop information and settings through LinkFox wrappers for the Shopee Open API Shop module.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and e-commerce operators use this skill to inspect Shopee shop status, profile, warehouse, notifications, authorized reseller brand data, Brazil onboarding status, and holiday mode, and to update profile or holiday-mode settings for an authorized store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live Shopee store settings, including profile fields and holiday mode.

Mitigation: Review the exact command and JSON parameters before execution, and get explicit confirmation before running update_profile or set_shop_holiday_mode.

Risk: Full API responses may contain sensitive shop, warehouse, notification, or Brazil onboarding data and are persisted locally.

Mitigation: Treat saved response files as sensitive, limit access to the local linkfox data directory, and delete files when they are no longer needed.

Risk: Custom LINKFOX_* gateway URLs could send shop data or API keys to an untrusted service.

Mitigation: Use the default LinkFox HTTPS gateway unless a trusted operator has approved a replacement endpoint.

Risk: The skill depends on LinkFox authentication and billing flows beyond basic shop lookup.

Mitigation: Use it only when the publisher and LinkFox account workflow are trusted for the target Shopee shop data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-shop)
- [Shopee Shop module index](https://open.shopee.com/documents/v2/v2.shop.get_shop_info?module=92&type=1)
- [Shop API reference](artifact/references/api.md)
- [Onboarding and billing guidance](artifact/references/onboarding.md)
- [get_shop_info reference](artifact/references/apis/get-shop-info.md)
- [get_profile reference](artifact/references/apis/get-profile.md)
- [update_profile reference](artifact/references/apis/update-profile.md)
- [set_shop_holiday_mode reference](artifact/references/apis/set-shop-holiday-mode.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, JSON files, guidance]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written under a local linkfox session data directory; small responses may also be printed inline, while larger responses are summarized unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
