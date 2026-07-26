## Description: <br>
检验抽样技能支持抽样方案设计、待检数据处理、抽样计划生成、抽样记录追踪和抽样结果分析，覆盖 GB/T2828 等标准抽样方法。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
质量、生产和数据分析人员可用该技能创建简单、分层、系统或整群抽样方案，解析 CSV、Excel 或 JSON 待检数据，并生成可追溯的抽样结果与统计分析报告。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads inspection datasets and writes parsed data, sample selections, audit records, and reports to local workspace files. <br>
Mitigation: Use it only where local storage of those files is acceptable, and avoid sensitive production datasets unless the workspace storage and retention are approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-inspection-sampling) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-inspection-sampling) <br>
- [检验抽样数据格式规范](references/format_spec.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces sampling schemes, parsed data files, sampling result JSON, audit records, and analysis reports in the local workspace.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
