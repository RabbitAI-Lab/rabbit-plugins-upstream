## Description:

从 Amazon 评论和商品详情中识别可能导致退货的体验与期望落差线索，并给出改进方向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, product operators, and product teams use this skill to review Amazon customer feedback for return-risk clues and improvement opportunities before taking product or listing action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can override the advertised fixed return-risk workflow and run other paid product-operation flows.

Mitigation: Allow only the documented return-risk flow unless a broader ARI product-operation workflow is intentionally approved.

Risk: The skill requires an ARI account and a locally saved ARI API key.

Mitigation: Install only in environments approved for ARI access and protect the local API key.

Risk: Paid collection or analysis can consume ARI credits.

Mitigation: Use profile and quote first, then run paid commands only after explicit confirmation with the same requestId.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/return-risk)
- [Amazon 退货风险线索 专属运营工作流](references/operation-workflow.md)
- [Amazon 退货风险线索 API 参考](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown analysis and CLI command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid actions should follow quote and explicit confirmation.]

## Skill Version(s):

1.4.13 (source: server release evidence, _meta.json, CHANGELOG, script constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
