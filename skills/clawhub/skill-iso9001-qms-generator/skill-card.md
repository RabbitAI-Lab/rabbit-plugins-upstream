## Description: <br>
基于过程和风险思维生成符合ISO9001标准的质量管理体系文件，支持四级文件结构和乌龟图；覆盖质量手册、程序文件、作业文件、记录表单等全套体系文件。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality managers, consultants, auditors, and operations teams use this skill to collect enterprise and process information, analyze ISO9001:2015 process requirements, and generate draft quality management system documents for review and adaptation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores enterprise profile details such as company name, scope, organization structure, responsibilities, and business process details in enterprise-info.json for reuse. <br>
Mitigation: Remove enterprise-info.json when it is no longer needed or before switching organizations, and avoid placing sensitive business details in shared workspaces. <br>
Risk: Generated ISO9001 quality management documents may contain generic language or待补充 placeholders when enterprise or process details are incomplete. <br>
Mitigation: Review generated manuals, procedures, work instructions, and forms with qualified quality management staff before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-iso9001-qms-generator) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-iso9001-qms-generator) <br>
- [ISO9001:2015 标准条款参考](references/iso9001-standards.md) <br>
- [过程分析指南](references/process-analysis-guide.md) <br>
- [质量手册模板（基于过程和风险方法）](references/quality-manual-template.md) <br>
- [ISO9001 文件选择模板](references/file-selection-template.md) <br>
- [过程乌龟图绘制指南](references/turtle-diagram-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Files, Shell commands] <br>
**Output Format:** [Conversational guidance, Markdown document drafts, and Word .docx files generated from Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses enterprise and process inputs to draft quality manuals, procedures, work instructions, and form templates; may reuse the latest local enterprise profile.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter and release changelog; release metadata version is 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
