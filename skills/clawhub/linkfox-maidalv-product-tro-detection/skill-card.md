## Description:

Checks product images and optional listing context for TRO and trademark, patent, or copyright infringement risk through LinkFox's Maidalu service, returning risk levels, matching IP and TRO details, numeric scores, and a generated legal assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers, cross-border e-commerce operators, and compliance reviewers use this skill to triage product images and listing context for possible TRO or IP infringement exposure before sourcing or publishing a product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, descriptions, account details, and feedback may be sent to LinkFox services.

Mitigation: Use approved product data only, avoid confidential or unreleased images unless that disclosure is acceptable, and verify LINKFOX_* endpoint and credential environment variables before use.

Risk: Local-image uploads can make uploaded images publicly reachable.

Mitigation: Prefer already approved public image URLs or Base64 data URIs when appropriate, and do not upload sensitive local files.

Risk: Full detection responses and cache files are stored locally under linkfox session folders.

Mitigation: Review and delete saved response or cache files when they contain sensitive product or account data.

Risk: The skill performs paid checks and can guide payment-related onboarding flows.

Mitigation: Confirm user intent before repeated checks, recharge actions, or payment-order steps.

## Reference(s):

- [Skill API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-maidalv-product-tro-detection)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and JSON responses from the LinkFox API scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written to local linkfox session files; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
