## Description:

Screens product image URLs with Ruiguan visual similarity search to identify potential matches against known policy-violating products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, e-commerce teams, and agents use this skill to pre-screen product images for potential policy-compliance risks before listing or review. It returns similarity-based matches, scores, and matched product metadata for human verification against applicable platform policies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product image URLs and uploaded local images are sent to LinkFox services, and local image uploads create public URLs.

Mitigation: Use only images approved for external processing, avoid confidential or personal content, and prefer already-public product image URLs when possible.

Risk: The artifact includes account login, SMS-code, API-key, billing, and order flows in addition to the image compliance check.

Mitigation: Create or retrieve API keys directly on the official LinkFox site when possible, verify LinkFox gateway environment variables before use, and review any billing action before confirming payment.

Risk: Full API responses and cache files may be stored under a local linkfox directory.

Mitigation: Delete local LinkFox response and cache files when no longer needed, especially when results include sensitive product images, identifiers, or account-related data.

Risk: Similarity matches do not provide definitive legal or platform-policy determinations.

Mitigation: Treat high-similarity matches as review signals and verify final decisions against the relevant marketplace or platform policies.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-gun-parts-search)
- [睿观-图片合规检测 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consumes 59 credits per check; full responses are saved locally, small responses may print in full, and large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
