## Description:

Helps agents manage and analyze authorized Shopee store videos through LinkFox scripts that call Shopee Video APIs for listing, publishing, editing, deletion, cover selection, and performance reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, developers, and agents use this skill to publish, edit, delete, list, and inspect performance for videos on authorized Shopee stores. It is most useful when a workflow already has LinkFox API credentials and a Shopee store selected through the companion authorization skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API keys and can contact LinkFox services to proxy Shopee video operations.

Mitigation: Install only for workflows that intentionally use LinkFox credentials, keep API keys in environment variables, and review any configured network endpoint overrides before running scripts.

Risk: Phone/SMS login recovery, API-key generation, billing orders, and payment QR-code flows can affect account access or spending.

Mitigation: Use onboarding and payment paths only after explicit user approval, verify plan IDs and payment methods, and avoid automatic payment-status polling.

Risk: Publishing, editing, or deleting Shopee videos can change live store content.

Mitigation: Confirm the target shop, video ID, request body, and intended operation before calling publish, edit, or delete scripts.

Risk: Full Shopee and LinkFox API responses may be saved locally, including operational or account-related data.

Mitigation: Review the saved JSON directory, limit sharing of generated response files, and apply local retention or cleanup practices appropriate for the data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-video)
- [LinkFox Shopee video API reference](references/api.md)
- [LinkFox onboarding and billing recovery reference](references/onboarding.md)
- [Shopee Open Platform video module reference](https://open.shopee.com/documents/v2/v2.video.get_cover_list?module=129&type=1)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses; large or full responses are saved as JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may write full LinkFox and Shopee API responses under a local linkfox session directory and print summaries for large responses.]

## Skill Version(s):

1.0.4 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
