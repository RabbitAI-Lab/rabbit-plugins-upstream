## Description:

查询 Amazon ASIN 的 SellerSprite 流量关键词列表，帮助查看关键词流量来源、自然位、广告位、流量占比类型、转化类型、历史月份和排序指标。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, e-commerce analysts, and agents use this skill to inspect keyword traffic structure for a specified Amazon ASIN. It supports ASIN reverse keyword lookup, result filtering, ranking metrics, paid-credit awareness, and authentication or billing setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup requests and keyword results are sent through LinkFox/SellerSprite service endpoints.

Mitigation: Install only when sharing ASIN and keyword lookup data with LinkFox is acceptable, and use official LinkFox endpoint environment variables.

Risk: Setup can involve phone/SMS login, API-key provisioning, and paid order creation.

Mitigation: Avoid entering one-time codes in logged or shared sessions, protect generated API keys, and confirm plan details before running billing commands.

Risk: Full lookup responses and cache files are persisted locally under linkfox session directories.

Mitigation: Periodically remove local linkfox response and cache files when they contain sensitive business data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-traffic-keyword)
- [SellerSprite traffic keyword API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API results and saved local JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lookup responses are cached for 24 hours and full responses are saved under a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
