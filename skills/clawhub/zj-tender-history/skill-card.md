## Description:

浙江工程招投标合同公示的供应商视角整理，按公司查中标项目、时间、金额与同类报价区间。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up Zhejiang public-works bid-history records for a supplier, including won projects, contract dates, amounts, and peer amount ranges for similar project types. It is intended for Zhejiang engineering tender history research, not national procurement coverage, non-engineering procurement, or company credit evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier queries are sent to the skill's remote service.

Mitigation: Use only appropriate supplier or project queries for remote lookup and disclose the remote service behavior before use.

Risk: The skill may store this product's cookies, install ID, or API key under ~/.odf.

Mitigation: Protect the local credential file, rotate or remove it when access changes, and avoid sharing it across users or machines.

Risk: Unexpected login or payment links could be untrusted.

Mitigation: Follow login or payment links only when they match the intended provider and treat unexpected links as untrusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/zj-tender-history)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text or Markdown summary generated from the packaged command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a supplier or project-type query; may store this product's cookies, install ID, or API key under ~/.odf/zj-tender-history.json.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
