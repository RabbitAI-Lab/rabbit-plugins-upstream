## Description:

协助用户按预算与风险需求调研产品或服务，核验规格、质量和价格信息，并给出有依据的选购建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhashushu](https://clawhub.ai/user/zhashushu)

### License/Terms of Use:

MIT

## Use Case:

面向寻求购买建议的消费者，用于对产品及部分服务进行预算分级的调研、证据核验、横向比较和风险说明。

### Deployment Geography for Use:

Global; purchase and pricing research focuses on Mainland China.

## Known Risks and Mitigations:

Risk: The installer package version is not pinned.

Mitigation: Check the installer source and pin a trusted package version before installation.

Risk: Repair-cost estimates may be affected by a reported calculation issue.

Mitigation: Verify repair-cost assumptions and calculations against independent sources before relying on the estimates.

Risk: Some referenced materials were unresolved during scanning, leaving the review incomplete.

Mitigation: Inspect unresolved references before relying on conclusions that depend on them.

Risk: The security summary notes a possible tool-scope gap.

Mitigation: Review the requested tool access against the skill's intended tasks before enabling it.

## Reference(s):

- [Server-resolved source repository (commit d5c0d779d50a729b6c5eb0a9dcc529ac87d12775)](https://github.com/zhashushu/bilei-team-skill/tree/d5c0d779d50a729b6c5eb0a9dcc529ac87d12775)
- [ClawHub release page](https://clawhub.ai/zhashushu/skills/bilei-team-skill)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with a plain-language recommendation, evidence-based comparisons, pricing analysis, and risk notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices and availability can change; the report should identify unknowns and support claims with current sources.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; embedded skill documentation identifies its workflow as 6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
