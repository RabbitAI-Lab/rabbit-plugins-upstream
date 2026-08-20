## Description:

Generates SEO-oriented, multilingual ecommerce listing copy for Amazon, Shopify, and TikTok Shop through the Yufluent cloud listing service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[metahuan](https://clawhub.ai/user/metahuan)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and their agents use this skill to gather product details and produce platform-specific listing copy, including titles, bullet points, descriptions, SEO keywords, and platform metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and listing inputs are sent to the Yufluent service.

Mitigation: Use the skill only when those inputs are appropriate to share with Yufluent, and remove sensitive or confidential product data before submission.

Risk: The skill requires TOKENAPI_KEY and allows TOKENAPI_BASE_URL configuration.

Mitigation: Protect the API key, review the configured base URL before use, and avoid sending requests to untrusted endpoints.

Risk: Generated listing copy may include inaccurate claims or platform-noncompliant wording.

Mitigation: Manually review generated titles, bullet points, descriptions, and keywords against the relevant marketplace rules before publishing.

Risk: The security guidance flags dependency and packaging hygiene considerations.

Mitigation: Prefer a pinned or constrained requests dependency and verify the packaged cloud client in controlled deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/metahuan/skills/yufluentcn-ecommerce-listing)
- [Yufluent Listing homepage](https://www.changzhiai.com/skills/listing)
- [OpenClaw and Yufluent setup](https://claw.changzhiai.com/app/openclaw)
- [Amazon Listing reference](artifact/references/amazon-style-guide.md)
- [Amazon platform rules](artifact/references/platform-rules-amazon.md)
- [Shopify best practices](artifact/references/shopify-best-practices.md)
- [TikTok Shop tips](artifact/references/tiktok-shop-tips.md)
- [Pricing table](artifact/references/pricing-table.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON listing output, optionally saved as a text file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes run metadata; the generated fields vary by Amazon, Shopify, or TikTok Shop format.]

## Skill Version(s):

1.3.3 (source: server release metadata; artifact frontmatter reports 1.3.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
