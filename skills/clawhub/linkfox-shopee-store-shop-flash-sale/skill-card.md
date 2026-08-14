## Description:

Enables agents to manage authorized Shopee Shop Flash Sale campaigns through LinkFox wrappers for all 11 Shopee Open Platform Shop Flash Sale APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, operators, and developers use this skill to manage authorized store flash-sale campaigns, including finding time slots, creating promotions, adding or updating items, deleting promotions or items, and inspecting campaign details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create, update, and delete operations can affect live Shopee flash-sale promotions.

Mitigation: Confirm the exact shop, merchant, flash-sale, item, and request-body values before executing mutating actions.

Risk: The skill handles LinkFox API keys, account onboarding, billing flows, and payment QR artifacts.

Mitigation: Use the skill only with trusted LinkFox accounts, keep credentials and payment artifacts private, and avoid sharing stdout logs that may contain sensitive values.

Risk: Full API responses are saved locally and may include operational store data.

Mitigation: Treat the local linkfox session data directory as sensitive and delete or protect saved responses according to the user's data-handling requirements.

Risk: Environment overrides can redirect gateway or login traffic.

Mitigation: Use default LinkFox hosts unless the user controls and trusts the configured override endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-shop-flash-sale)
- [Shopee Shop Flash Sale API index](https://open.shopee.com/documents/v2/v2.shop_flash_sale.get_time_slot_id?module=123&type=1)
- [Artifact API overview](artifact/references/api.md)
- [Artifact onboarding guidance](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [API calls, JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses saved to local files with stdout JSON or summaries, plus Markdown-style operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
