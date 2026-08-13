## Description:

Searches previously synchronized Etsy category data by keyword and returns category names, IDs, levels, and parent IDs for product or shop filtering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, sellers, and agent workflows use this skill to find Etsy category IDs from LinkFox-synchronized category data for product and shop search filters. It also provides guidance for LinkFox authentication and billing recovery when lookup access fails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, phone numbers, SMS codes, account tokens, and payment-order data during onboarding.

Mitigation: Use it only in trusted workspaces, avoid sharing logs that contain secrets or account data, and rotate credentials if they are exposed.

Risk: The release includes account login, API-key issuance, and billing/payment flows beyond Etsy category lookup.

Mitigation: Install only when LinkFox authentication and billing management are expected, and manually confirm any selected plan or payment action before proceeding.

Risk: The helper script can write full lookup responses and cache files under local LinkFox output directories.

Mitigation: Run it in an appropriate workspace and remove local output or cache files when category results should not persist.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-category-search)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON lookup results and Markdown-style guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lookup output includes category fields such as id, name, categoryLevel, parentId, and parentIds; large responses may be summarized while full JSON is saved locally by the helper script.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
