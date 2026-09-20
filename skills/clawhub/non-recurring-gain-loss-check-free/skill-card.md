## Description:

对非经常性损益明细表执行逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

上市公司、拟上市公司、集团合并报表相关的财务、审计与证券事务人员可在报告期底稿编制、年报或半年报披露、审计和券商核查前，用它核对非经常性损益明细表的机械勾稽关系。它不替代会计判断、税务判断、审计程序或鉴证意见。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a local Node.js script against financial table text supplied by the user.

Mitigation: Run it only in a trusted local workspace and provide only the table text needed for the check.

Risk: Runner help text mentions an anonymous statistics call, while the inspected code does not send network requests.

Mitigation: Review the installed artifact before use and monitor or block network access if anonymous telemetry would be unacceptable.

Risk: The checks cover a free subset and do not make accounting, tax, audit, or disclosure judgments.

Mitigation: Use the output as a deterministic consistency check and route material conclusions through normal finance, tax, audit, and disclosure review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/non-recurring-gain-loss-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown-facing usage guidance with shell commands; runtime output is human-readable text or JSON findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, line number, category, message, and source evidence when checks run successfully.]

## Skill Version(s):

1.0.13 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
