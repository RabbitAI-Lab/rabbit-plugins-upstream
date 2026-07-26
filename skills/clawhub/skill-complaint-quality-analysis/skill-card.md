## Description: <br>
客诉质量复盘分析；当用户需要客诉台账分析、售后质量问题复盘、投诉统计报告生成或客诉异常清单分析时使用；覆盖数据清洗、统计分析与改善建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality, support, and operations teams use this skill to review customer complaint ledgers, confirm field mappings, calculate complaint statistics, identify repeated issues, and prepare internal quality review reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Complaint datasets may contain customer names, complaint descriptions, and other business-sensitive values that can appear in JSON analysis output or generated reports. <br>
Mitigation: Install and use the skill only for datasets approved for agent analysis, and review generated JSON and reports before sharing them. <br>
Risk: Incorrect or unconfirmed field mappings can produce misleading complaint statistics and quality conclusions. <br>
Mitigation: Confirm key fields, analysis goals, and report outline with the user before running deeper analysis or generating final reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-complaint-quality-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>
- [Server-resolved GitHub source](https://github.com/duding-engicool/skill-complaint-quality-analysis) <br>
- [Field mapping reference](references/field-mapping.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts produce JSON analysis data and HTML or Markdown reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes user-provided Excel or CSV complaint data locally; analysis output may include small raw row previews and sample field values.] <br>

## Skill Version(s): <br>
0.1.0 (source: release metadata; artifact frontmatter states 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
