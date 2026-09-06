## Description:

核对 Amazon 商品页承诺与真实评论体验之间的差距，并生成基于 ARI 评论数据的 promise-audit 报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT

## Use Case:

External Amazon sellers and e-commerce operators use this skill to compare listing promises with customer review evidence, identify expectation gaps, and decide what to improve in product pages or operations. It is not intended for Amazon policy review, legal compliance review, or unsupported marketing claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release label is narrow, but the skill can use an ARI account key and access broader ARI operations such as paid analysis, monitoring, export, and account or workbench state changes.

Mitigation: Install only when that broader ARI operations access is intended, keep the API key local, and review requested actions before allowing the agent to run them.

Risk: Paid ARI workflows and auto-confirm settings can spend account credits.

Mitigation: Keep auto-confirm disabled or capped when appropriate, require quotes before paid workflows, and verify completion status before retrying interrupted paid operations.

## Reference(s):

- [Amazon 消费者预期差距 workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/customer-gap)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with concise command guidance and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid operations are quoted before execution and should use explicit user confirmation unless account auto-confirm rules apply.]

## Skill Version(s):

1.4.5 (source: frontmatter, _meta.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
