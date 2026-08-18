## Description:

调用 Sorftime 按自然语言名称搜索 Walmart 美国站商品，或查询商品详情、商品趋势与按日销量。用户提到 Walmart 商品名称搜索、按名称找产品、相关产品、ProductId、商品详情、价格、评分、类目排名、商品趋势、历史变化、销量趋势、变体销量、按日销量、昨日销量、竞品发现或竞品跟踪时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, analysts, and agents use this skill to search Walmart US products by natural-language name or inspect a known ProductId for details, historical trends, and daily or variant sales rows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill suspicious because product queries are combined with onboarding, payment, automatic feedback, and local persistence behavior.

Mitigation: Review the LinkFox account, billing, feedback, and storage flows before use; use a dedicated API key and avoid sending sensitive product research unless those flows are acceptable.

Risk: API calls consume LinkFox credits, and additional pages, operations, or date ranges can create extra paid requests.

Mitigation: Confirm before making paid calls beyond the requested operation, reuse the documented 24-hour cache for identical requests, and do not automatically retry with changed parameters.

Risk: Onboarding can involve phone verification, SMS codes, payment QR flows, and API-key configuration.

Mitigation: Share phone or SMS codes only when intentionally registering through LinkFox, confirm payment QR flows before proceeding, and store API keys only in appropriate local environment variables.

Risk: The skill saves full API responses locally and may submit feedback when behavior or results mismatch intent.

Mitigation: Inspect saved session data for sensitive content, avoid syncing generated response files unintentionally, and disable or avoid automatic feedback submission when prompts or results are sensitive.

## Reference(s):

- [Walmart 产品分析 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sorftime-walmart-product-analysis)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Files, Configuration]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses to a session-scoped JSON file; small responses may also be printed inline, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
