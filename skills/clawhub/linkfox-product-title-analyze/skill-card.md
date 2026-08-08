## Description:

Analyzes previously queried Amazon product titles to extract and count one requested attribute dimension, such as scene words, audience terms, materials, colors, or feature words.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce analysts use this skill to find recurring keyword and attribute patterns in product listing titles that have already been retrieved in the current conversation. It supports competitive title analysis, title keyword frequency review, and attribute-based grouping one dimension at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product titles and related product data are sent to a paid LinkFox cloud service for analysis.

Mitigation: Use the skill only when the user accepts sharing that product data with LinkFox and understands that each call may consume credits.

Risk: The artifact includes account login, API-key generation, quota purchase, and payment QR workflows that go beyond title analysis.

Mitigation: Run onboarding and payment flows only after explicit user intent, and verify plan, price, payment method, and order status before presenting next steps.

Risk: Full analysis responses are stored locally in a linkfox session data directory.

Mitigation: Treat saved response files as potentially sensitive and review or remove them according to the user's data-retention expectations.

Risk: Setup guidance can persist API keys in shell startup files.

Mitigation: Avoid modifying shell startup files unless the user intentionally wants a persistent LinkFox API key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-product-title-analyze)
- [商品标题分词分析 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown tables and concise text for the user, plus JSON API responses saved to session data files when the script is run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analyzes one title-attribute dimension per API call; full responses are saved under a linkfox session data directory, and large responses may be summarized on stdout.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
