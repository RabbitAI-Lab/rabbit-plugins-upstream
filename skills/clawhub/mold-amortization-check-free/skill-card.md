## Description:

模具与工装摊销台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Cost accountants and finance managers use this skill before monthly costing and close to check mold and tooling amortization ledgers for arithmetic mismatches, total-line inconsistencies, duplicate rows, missing placeholders, and negative values. The free release performs the documented local checks and does not claim the paid-only checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation and default output steer users toward an external paid install and purchase workflow.

Mitigation: Use the free local checker only unless the package, merchant, product, permissions, and payment steps are separately verified by the user.

Risk: The free release withholds several checks that may matter for amortization review.

Mitigation: Treat the result as limited to the six documented free checks and do not infer coverage for paid-only or out-of-scope accounting judgments.

Risk: Insufficient or malformed ledger input can otherwise lead to overconfident conclusions.

Mitigation: Require a ledger with recognizable headers; when material is insufficient, preserve the skill behavior of returning no conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/mold-amortization-check-free)
- [SkillPay shelf for optional full version](https://skillpay.alipay.com/public/tokendidi)
- [Publisher purchase instructions for optional full version](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; findings cite source lines when checks can run, and insufficient input produces no conclusion.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
