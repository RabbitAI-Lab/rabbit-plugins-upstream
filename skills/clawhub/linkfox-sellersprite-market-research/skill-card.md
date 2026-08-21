## Description:

使用卖家精灵选市场列表能力，基于类目维度筛选亚马逊细分市场，支持市场规模、竞争度、头部集中度、卖家结构、新品占比、价格/评分/毛利区间等大量条件，用于发现可进入市场与评估选品方向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace researchers, Amazon sellers, and ecommerce operators use this skill to screen category-level SellerSprite market data, compare market size and competition signals, and identify product or category opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends research queries, session metadata, and a LinkFox API key to LinkFox endpoints.

Mitigation: Install only for intended LinkFox/SellerSprite market research, review gateway environment variables before use, and avoid sending sensitive or unnecessary query data.

Risk: The skill can guide phone login, reusable API-key generation, billing checkout, and feedback submission.

Mitigation: Prefer self-service account setup and require explicit user confirmation before phone login, API-key generation, purchase, order query, or feedback actions.

Risk: The skill consumes paid credits and may save complete API responses locally.

Mitigation: Warn users before additional paid calls, use the 24-hour cache where appropriate, and review or delete saved response files when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-market-research)
- [卖家精灵-选市场列表 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and locally saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses may be summarized in stdout when large while complete JSON responses are saved under a linkfox session data directory.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
