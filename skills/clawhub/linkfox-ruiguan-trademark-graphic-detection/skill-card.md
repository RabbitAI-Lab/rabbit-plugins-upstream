## Description:

Detects graphic trademarks and visually similar registered marks in product images to help assess potential logo or design trademark risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, brand owners, and agents use this skill to compare product images or logos against supported trademark databases before listing or reviewing products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product image URLs or uploaded local images may be sent to LinkFox services and can contain business-sensitive product data.

Mitigation: Use the skill only when the user is comfortable sharing those images with LinkFox, and avoid uploading confidential or unreleased product images unless that sharing is approved.

Risk: Account phone numbers, SMS codes, API keys, feedback content, and billing or order data may be handled during onboarding or error recovery.

Mitigation: Keep SMS codes and raw API keys out of untrusted transcripts, use official LinkFox endpoint environment variables, and confirm any paid order before displaying a payment QR.

Risk: Local LinkFox response and cache files may retain trademark results or other business-sensitive data after use.

Mitigation: Review and periodically delete local LinkFox response/cache files when they contain sensitive business information.

## Reference(s):

- [睿观-图形商标检测 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-trademark-graphic-detection)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown summaries and tables, JSON API responses, local JSON files, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses may be written to local LinkFox response/cache files; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
