## Description:

申报前的涉税批量自查，一次跑完目录里所有对象，逐个跑 14 项涉税检查并每个对象输出一行结论（各项通过 / 有问题 / 材料不足未执行），每条结论都引用原文文件与行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External tax and accounting users can run local pre-filing checks over customer or entity folders to find arithmetic, consistency, and missing-material issues across 14 tax-related tables. The skill reports one result line per object and cites source files and line numbers for findings.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill reads the tax folders or files the user points it at, which may contain sensitive business or taxpayer information.

Mitigation: Run it only on intended local directories and provide the minimum materials needed for the pre-filing check.

Risk: A clean result can be mistaken for tax advice or a filing decision.

Mitigation: Treat the output as a local arithmetic and consistency check, then review results with qualified tax judgment before relying on them.

Risk: Missing materials or unexecuted sub-checks can leave parts of a filing package unchecked.

Mitigation: Review the reported not-run checks, withheld checks, and material gaps, then rerun after supplying the missing tables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tax-filing-pack-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text or JSON containing per-object check status, findings, severity counts, and source file line references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against explicitly selected input materials and normally prints results to stdout without writing output files.]

## Skill Version(s):

1.0.30 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
