## Description:

调用 Sorftime 研究 Walmart 美国站关键词市场、名称反查词、搜索结果商品、关键词详情、商品关联词与扩展词，并管理收藏关键词目录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, analysts, and agent operators use this skill to research Walmart US keyword demand, inspect keyword metrics, find products or related terms for a keyword, reverse-search product keywords, and manage saved keyword folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The onboarding flow can handle phone verification, API keys, paid order creation, and payment QR generation.

Mitigation: Require clear user consent before collecting verification details, showing API-key setup steps, creating paid orders, or presenting payment QR codes.

Risk: The keyword API can consume paid credits, especially for high-cost searches, related-keyword expansion, or additional pages.

Mitigation: Disclose expected credit use before high-cost calls or continued pagination, and avoid automatic retry, variant, or multi-step discovery chains.

Risk: Saved-keyword operations can mutate external account data.

Mitigation: Run add, delete, or move operations only after explicit authorization and confirm the folder or delete scope when ambiguity could affect multiple saved entries.

Risk: Full API responses are stored locally and may contain sensitive business research data.

Mitigation: Tell users where responses are saved, avoid including secrets in requests, and review stored files before sharing or committing them.

Risk: Automatic feedback reporting may send context about mismatched behavior or user sentiment to the feedback endpoint.

Mitigation: Avoid sending sensitive user or account details in feedback and obtain consent when feedback content could reveal private information.

## Reference(s):

- [Walmart keyword research API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sorftime-walmart-keyword-research)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API responses, concise summaries, and saved JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are written under a linkfox session directory; large responses print a summary unless inline output is requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
