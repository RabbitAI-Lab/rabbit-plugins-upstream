## Description:

从主 ASIN 与已授权竞品的商品字段、图片和评论证据提炼可验证的差异化方向与待验证问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators use this skill to compare a primary ASIN with authorized competitor product fields, images, and review evidence, then identify verifiable product differentiation opportunities and follow-up questions. It is not intended for market-size, sales, profit, inventory, advertising, order, or real-time operational decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store and use an ARI API key and send product or review requests to ARI.

Mitigation: Use it only with an intended ARI account, keep API keys out of reports and screenshots, and rely on the documented setup/configuration flow.

Risk: The skill can spend ARI credits or make billing-affecting changes such as analysis runs, monitoring schedules, or competitor bindings.

Mitigation: Review quotes, confirmation prompts, autoconfirm settings, schedules, and competitor bindings before allowing paid or future collection activity.

Risk: The skill is broader than its differentiation label and includes export, monitoring, account-setting, and other ARI workflows.

Mitigation: Constrain use to the fixed page_compare/differentiation workflow unless the user explicitly requests another documented ARI workflow.

Risk: Outputs may be unsuitable for sales, profit, inventory, advertising, order, or market-sizing decisions.

Mitigation: Treat results as evidence-backed discussion inputs and validate them with additional business data before operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/differentiation)
- [Operation workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI API key setup](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise text guidance with CLI command invocations; some CLI responses may be JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses fixed page_compare/differentiation defaults for this release.]

## Skill Version(s):

1.4.5 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
