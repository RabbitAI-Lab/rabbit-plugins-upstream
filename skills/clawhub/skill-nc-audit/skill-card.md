## Description: <br>
管理体系内审不符合项判定与验证工具，帮助内审员录入不符合项、依据 ISO 条款辅助判定性质、跟踪验证状态并生成审核结论报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
内审员和质量管理人员使用此技能管理内审不符合项的生命周期，包括记录创建、分类、规则辅助判定、验证跟踪和审核汇总报告生成。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit evidence and verification details are stored in a local plaintext JSON file. <br>
Mitigation: Use the skill only in access-controlled workspaces, avoid entering confidential personnel or operational details, and clear or replace bundled audit records when they are not needed. <br>
Risk: Rule-based category suggestions may not reflect the final audit judgment for a specific organization or ISO context. <br>
Mitigation: Have a qualified auditor review suggested categories, cited clauses, and report conclusions before using them in formal audit records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-nc-audit) <br>
- [Server-resolved GitHub repository](https://github.com/duding-engicool/skill-nc-audit) <br>
- [ISO clause reference](artifact/references/iso_clauses.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON or text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local scripts read and write audit records in assets/nc_data.json; generated reports include statistics and improvement suggestions.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
