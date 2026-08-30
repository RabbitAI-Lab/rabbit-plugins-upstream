## Description:

电商选品决策助手｜AI-HIVE helps merchants and ecommerce teams turn product-selection inputs into fact-grounded scoring tables, risks, content plans, runnable AI-HIVE commands, and review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, category operators, live-commerce teams, and marketing creators use this skill to evaluate candidate products, identify missing facts, plan platform-specific content, and prepare AI-HIVE image or video generation tasks after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can incur costs after prompts, routing, and models are submitted.

Mitigation: Review final parameters before execution, start with small samples, and use the skill's cost-aware routing and pricing snapshot steps.

Risk: Uploaded product images, videos, logos, or reference assets may include private or unlicensed media.

Mitigation: Confirm rights and privacy status before upload; use abstract structure guidance when source-media authorization is unclear.

Risk: Persisting an AI-HIVE API key in a local config file can expose credentials on shared systems.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable for transient use, and keep any local config file permissions restricted.

Risk: Product claims, market data, rankings, or performance promises can become misleading if not grounded in supplied evidence.

Mitigation: Use only user-provided facts or clearly sourced claims, keep gaps visible, and avoid promises of sales, ranking, review, or approval outcomes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-product-selector-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured checklists, JSON task records, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task identifiers, routing mode, model choice, pricing snapshot, status, and downloaded file locations when generation is submitted.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
