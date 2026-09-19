## Description:

帮助 Amazon 卖家通过 ARI 查看 ASIN 在类目中的星级和差评率相对位置、类目排行，并生成评论、VOC、趋势、竞品和运营分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to benchmark an ASIN against category star ratings and negative-review rates, inspect leaderboards, and turn collected review data into VOC, trend, competitor, keyword, alert, and operations guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some ARI analysis workflows can spend ARI credits without a fresh per-run confirmation.

Mitigation: Use quote-only mode or ask-before-every-charge before VOC or analysis workflows, and disable auto-confirm when predictable approval is required.

Risk: The skill stores a local ARI API key and sends ASIN and review-analysis requests to the ARI service.

Mitigation: Install only when that data sharing is acceptable, use browser-based authorization or environment configuration, and avoid placing API keys in chat, reports, or examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/industry-benchmark)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI user guide](artifact/使用说明.md)
- [ARI account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown and JSON responses from the ARI CLI, with optional CSV, Markdown, or HTML exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; some workflows may spend ARI credits or create local exports.]

## Skill Version(s):

1.4.13 (source: frontmatter, _meta.json, release evidence, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
