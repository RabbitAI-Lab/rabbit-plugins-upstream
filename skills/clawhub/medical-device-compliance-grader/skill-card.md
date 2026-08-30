## Description:

医疗器械合规度量化评分工具，按注册路径、技术文件、风险管理、临床评价、标签 IFU、软件网络安全、上市后监管和质量体系 8 个维度进行 0-5 分自评，并生成包含雷达图、明细表和改进建议的自包含 HTML 评分卡。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Regulatory, quality, and product teams use this skill to structure medical-device compliance self-assessments, compare evidence across eight dimensions, and produce HTML and JSON scorecard artifacts for planning remediation before formal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat self-assessment scores as a formal regulatory or notified-body decision.

Mitigation: Present outputs as planning and gap-analysis aids only, and require qualified regulatory affairs review before submission or compliance decisions.

Risk: Generated HTML can include fields derived from scoring input.

Mitigation: Run the tool only on scoring JSON the user intends to process, and avoid opening generated HTML from untrusted third-party input.

Risk: Scores can be misleading when supporting evidence is incomplete or stale.

Mitigation: Attach evidence notes for each dimension, recheck cited regulatory sources, and treat missing evidence as a low score or not applicable only when justified.

## Reference(s):

- [合规评分维度与标准](references/合规评分维度与标准.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON scoring input, shell commands, self-contained HTML report output, and optional JSON result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The scoring script uses local standard-library Python and produces dependency-free SVG charts inside the HTML report.]

## Skill Version(s):

1.0.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
