## Description: <br>
标书查重与围串标风险初筛助手。当用户上传多份投标或招标文件需要检测文本雷同、关键信息（公司/电话/项目经理/造价师等）碰撞、文档属性一致、表格相似或两份文档差异比对时使用。基于大模型语义比对，输出含风险等级与定位的结构化检测报告，并支持导出 Word。适用于投标人自检与招标人初步筛查，不适用于评标委员会正式判定。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, bid teams, and procurement reviewers use this skill to perform an initial duplicate-check and collusion-risk screen across 2-10 Chinese bid or tender documents. It helps identify text similarity, key-field collisions, document metadata warnings, table similarity, and two-document diffs, then produces a structured report for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bid documents may contain personal data, bank details, commercial secrets, or document metadata. <br>
Mitigation: Confirm the processing environment is permitted for these files and redact unnecessary sensitive fields before use. <br>
Risk: Generated reports may contain extracted sensitive fields, document metadata, and a fixed author/feedback footer. <br>
Mitigation: Review each report before sharing it formally or using it in procurement decisions. <br>
Risk: The skill is an initial screening aid and may miss issues or produce false positives, especially for scanned documents or documents without tender-baseline removal. <br>
Mitigation: Use human review and, for high-stakes decisions, specialist duplicate-checking or legal review before acting on findings. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chesaram/skills/bid-dup-check) <br>
- [README](artifact/README.md) <br>
- [Detection Rules Reference](artifact/references/detection_rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown and JSON guidance with shell commands; generated reports may be Markdown and DOCX files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include risk levels, finding locations, limitations, conclusions, and a fixed author/feedback footer.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata); artifact frontmatter and manifest state 1.1.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
