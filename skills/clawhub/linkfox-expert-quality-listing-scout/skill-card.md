## Description:

亚马逊精品铺货选品专家，帮助筛选 BSR 上升、近期上架且评分达标的高质量商品机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and e-commerce operators use this skill to find quality listing opportunities with fixed filters for strong BSR growth, recent listing age, and rating thresholds, then export Excel results or run optional ASIN scoring. It supports repeated scouting rounds, sorting changes, condition recommendations, and scheduled product selection workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a LinkFox API key and guide account or payment onboarding.

Mitigation: Install only when the publisher is trusted, and review API key, endpoint, account, and payment configuration before use.

Risk: Generated or uploaded files can become publicly accessible URLs.

Mitigation: Upload only files intended for public sharing, and review local result files before publishing them.

Risk: Scheduled task support can create persistent recurring or one-time agent work.

Mitigation: Review task content, frequency, notification settings, and cost before enabling scheduled runs.

Risk: Bundled tooling includes paths that can modify other agent instructions or extend workflows.

Mitigation: Avoid patching or self-extension paths unless explicitly intended, and review changes before continuing.

Risk: Product scoring is based on available SellerSprite fields and does not fully cover brand concentration, price history, traffic structure, or patent risk.

Mitigation: Use the scoring output as an initial shortlist and run deeper product, competition, and compliance checks before business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-quality-listing-scout)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Root skill workflow](artifact/SKILL.md)
- [Amazon Product Scout Agent](artifact/skills/amazon-product-scout-agent/SKILL.md)
- [Product scout API parameter catalog](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [SellerSprite product search API](artifact/skills/linkfox-sellersprite-product-search/references/api.md)
- [ASIN dynamic scoring expectations example](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [Task scheduler API](artifact/skills/linkfox-task-scheduler/references/api.md)
- [File upload API](artifact/skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands plus Excel, CSV, and JSON file outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversations show Top 10 previews, file paths, sorting prompts, pagination status, and optional scoring summaries.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
