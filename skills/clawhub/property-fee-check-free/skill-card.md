## Description:

物业费计算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External property-management teams and park operators use this skill to check monthly property-fee and late-fee tables before billing or collections. It recalculates fee rows and totals, flags duplicate or incomplete rows, and cites source line numbers for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an optional paid-upgrade path that asks an agent to run an unpinned remote installer and follow another skill's instructions.

Mitigation: Treat the paid upgrade as a separate installation decision: verify the package publisher, prefer a pinned reviewed version or sandbox, and require explicit user review before installing dependencies or initiating payment steps.

Risk: Property-fee findings can be incomplete or misleading when the input table is missing required headers or source rows.

Mitigation: Provide the complete table with headers and review line-cited findings against the original billing records before using results in billing or collections.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-fee-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable text or JSON with executed checks, findings, line references, omitted checks, and insufficient-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with bundled Node.js scripts; findings depend on a supplied property-fee table with recognizable headers.]

## Skill Version(s):

1.0.3 (source: server-resolved release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
