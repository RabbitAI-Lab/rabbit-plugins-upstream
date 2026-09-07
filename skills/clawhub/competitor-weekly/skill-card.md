## Description:

经明确确认并完成报价后，生成主 ASIN 与已授权竞品的 Amazon 商品详情、快照和评论证据对照周报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to request a confirmed weekly competitor report comparing a main ASIN with authorized competitor ASINs using ARI-collected product, snapshot, and review evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags broader ARI account, monitoring, billing, export, and persistent-confirmation controls than the narrow weekly competitor report description suggests.

Mitigation: Review before installing, trust only the ARI service, and keep auto-confirm, monitoring changes, and export actions disabled or closely supervised unless explicitly needed.

Risk: Paid ARI actions can spend credits under account confirmation or auto-confirm rules.

Mitigation: Use quote-only behavior until the user gives explicit approval, and verify credit cost, balance, and request ID before confirmed report generation.

Risk: The skill requires an ARI API key.

Mitigation: Use the browser authorization flow or environment variable support, and do not place the API key in reports, command examples, or chat transcripts.

## Reference(s):

- [Amazon 竞品周报 workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI Amazon review assistant user guide](artifact/使用说明.md)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-weekly)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise conversational summaries, with shell commands for setup or troubleshooting when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may return report URLs, report IDs, credit usage, and data coverage notes.]

## Skill Version(s):

1.4.7 (source: server release evidence, frontmatter, changelog, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
