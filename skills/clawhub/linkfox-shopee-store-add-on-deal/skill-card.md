## Description:

Helps agents manage Shopee Add-On Deal promotions for authorized stores through the LinkFox gateway, including create, list, update, end, delete, and item-management actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee store operators, commerce teams, and developers use this skill to create, inspect, update, end, and delete Add-On Deal promotions after store authorization is available. It is most useful when an agent needs scripted access to the Shopee Add-On Deal API surface while preserving full JSON responses for later review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive Shopee store-management data, account onboarding details, API keys, and payment flows.

Mitigation: Install and run it only in environments where LinkFox is trusted with those records and secrets.

Risk: Store-changing operations can update, end, or delete active Add-On Deal promotions.

Mitigation: Require explicit user confirmation and verify the shop ID, merchant ID, and deal or item IDs before running destructive or mutating actions.

Risk: Custom gateway endpoint environment variables can redirect requests away from the default LinkFox service.

Mitigation: Avoid setting custom LinkFox endpoint variables unless the destination is controlled and approved.

Risk: Saved LinkFox response files may contain sensitive business records.

Mitigation: Store response files in a trusted workspace, restrict access, and review contents before sharing logs or artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-add-on-deal)
- [Shopee Add-On Deal API index](https://open.shopee.com/documents/v2/v2.add_on_deal.add_add_on_deal?module=111&type=1)
- [Add-On Deal module reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response summaries; full script responses are saved as JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses up to 8 KB are printed in full; larger responses are summarized while the full response remains available in a session data file.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
