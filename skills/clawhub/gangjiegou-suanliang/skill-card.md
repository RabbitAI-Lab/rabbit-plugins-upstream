## Description:

钢结构算量：消费 cad-file-reader 的 *.steel.json，按截面标注、米重公式及显式或图面长度生成吨位估算带，并提供牌号分档、构件归并、连接计数、节点板、涂装面积和复核清单；不做识图，也不替代深化、翻样、下料、结算或报价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

钢结构工程师和估算人员可将已有的钢结构识图契约或手工整理的契约汇总为吨位区间、构件台账及复核清单，用于方案阶段估算和数据复核。输出是估算草稿，不用于正式结算或报价。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented end-to-end workflow starts an external drawing-recognition tool, while this skill describes its own role as calculating from an existing contract.

Mitigation: Review the external recognition tool and resulting contract before calculation; use an existing verified contract when appropriate.

Risk: The scanner could not verify some referenced external scripts, so evidence about the complete workflow is incomplete.

Mitigation: Review referenced dependency scripts from trusted sources before enabling the full workflow.

Risk: The documented workflow uses shell commands and reads and writes local contract and report files.

Mitigation: Run it with trusted inputs and in a directory where the expected files can be reviewed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/gangjiegou-suanliang)
- [lis-skill-bus contract](references/bus-contract.md)
- [Manual input contract example](examples/README.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, CSV, Guidance]

**Output Format:** [JSON, Markdown, and CSV files with estimate bands, section summaries, member and connection ledgers, and review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tonnage is a ±15% estimate band with final_quantity=false; missing or ambiguous evidence remains marked for review.]

## Skill Version(s):

0.3.1 (source: frontmatter, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
