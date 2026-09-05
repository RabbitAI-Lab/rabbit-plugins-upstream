## Description:

从 Amazon 评论中的重复疑问和商品字段中提炼商品页 FAQ 主题与回答证据，需要 ARI API key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operations teams use this skill to turn review questions and product fields into product-page FAQ suggestions. The artifact also exposes broader ARI review analysis, monitoring, export, and account workflow commands that should be reviewed before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The FAQ-focused label understates broad ARI review-operations capabilities.

Mitigation: Review the release as a broad ARI client, and constrain use to the intended FAQ/listing workflow unless broader review operations are explicitly needed.

Risk: Paid analysis, collection, monitoring, exports, and auto-confirm settings can consume credits or change account workflow state.

Mitigation: Verify quoted costs, balances, recurring collection settings, and confirmation behavior before enabling paid, recurring, or auto-confirmed actions.

Risk: The skill requires an ARI API key for external service access.

Mitigation: Grant an API key only after accepting the ARI trust boundary, avoid exposing the key in reports or screenshots, and keep requests on the official ARI base URL unless a custom endpoint is intentionally configured.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/faq-generator)
- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [Amazon 商品 FAQ 建议 专属运营工作流](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export reports as Markdown or HTML and reviews as CSV through the bundled CLI; requires an ARI API key.]

## Skill Version(s):

1.4.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
