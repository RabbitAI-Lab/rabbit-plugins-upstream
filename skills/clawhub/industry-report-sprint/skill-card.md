## Description:

Write a cited industry report with market analysis, product comparisons, barriers, and evidence gaps; retain research in JishuDB. / 撰写有引用的行业报告，覆盖市场、产品对比、壁垒与证据缺口，研究记录保存在JishuDB。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external analysts, and developers use this skill to turn a sector name into a cited industry report with market structure, demand, barriers, representative product comparisons, evidence gaps, and retained JishuDB research records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow writes local report files and approved JishuDB records, which may retain source material or research notes beyond the immediate session.

Mitigation: Confirm the selected knowledge base, retention scope, output directory, and permitted source representations before the agent starts work.

Risk: Public browsing or search could expose private documents or confidential facts if they are included in queries.

Mitigation: Keep private material out of public queries and use only public or explicitly authorized acquisition routes.

Risk: Industry reports may rely on incomplete, inaccessible, truncated, or conflicting evidence.

Mitigation: Label evidence coverage, access limits, contradictions, and unresolved gaps in the report instead of presenting unsupported conclusions.

Risk: JishuDB writes require explicit approval and suitable privileges.

Mitigation: Verify the live host capabilities, approved write profile, selected KB ID, saved record IDs, and readback before marking the workflow complete.

## Reference(s):

- [Evidence contract](references/evidence-contract.md)
- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/industry-report-sprint)
- [Project homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/industry-report-sprint)
- [199IT report category](https://www.199it.com/archives/category/report)
- [199IT RSS feed](https://www.199it.com/feed)

## Skill Output:

**Output Type(s):** [text, markdown, CSV, guidance]

**Output Format:** [Markdown report files, CSV evidence table, source notes, revision manifest, and JishuDB records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local report artifacts and saves approved research records to a selected JishuDB knowledge base.]

## Skill Version(s):

0.1.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
