## Description:

Amazon 评论转行动结合商品详情和评论证据，把 Amazon 评论问题整理成产品、包装、说明和供应商任务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operations teams use this skill to analyze review data for a specified ASIN and convert recurring issues into actionable product improvement tasks. The skill is designed for evidence-driven product action, not buyer outreach, direct listing changes, or purchasing execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses an ARI API key locally to access Amazon review analysis services.

Mitigation: Install only if the publisher and ARI service are trusted with the relevant Amazon review data; keep the key out of reports, prompts, and shared command examples.

Risk: Some ARI analyses can consume account credits or run under service-defined auto-confirmation settings without a fresh per-action approval.

Mitigation: Turn autoconfirm off when every charge needs explicit approval, and review quoted costs before paid operations.

Risk: Schedule, watch, competitor, export, and workbench actions can change future account behavior or create local files.

Mitigation: Use these actions only after confirming the requested account behavior, target ASIN or watch ID, and destination file expectations.

## Reference(s):

- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-action)
- [ARI API Key Account Page](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Product Management](https://ari.funewa.com/zh/products)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with concise recommendations, data caveats, quoted costs, and occasional inline shell commands for advanced use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should separate observed API data, inferred analysis, and strategy suggestions, and should include report links when returned by the ARI service.]

## Skill Version(s):

1.4.8 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
