## Description:

当用户提供产品想法、目标人群或待验证的问题，需要产品需求调研、用户痛点、现有替代方案、购买顾虑或相反证据时使用。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向产品团队、创业者和研究人员，用于围绕明确的人群与问题整理有限范围的公开社交讨论证据，识别痛点、替代方案、购买顾虑和反证，并形成可追溯的简报与后续验证建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The examples run the unpinned, changeable `socialdatax-skills@latest` package through npx, creating a supply-chain risk; the security evidence reports no evidence of malicious intent.

Mitigation: Pin and review the package version, use a controlled installation, and provide only the credentials and access the task needs.

Risk: The security scan was partial because it could not resolve three local references, so the evidence is incomplete.

Mitigation: Review the unresolved references and complete the security review before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/product-demand-evidence)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown brief with source-linked evidence and follow-up validation suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bounded research scope: up to two platforms, two queries per platform, four posts for detail and primary comments, and three follow-up suggestions. Findings reflect the retrieved sample and do not establish market size or paid conversion.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
