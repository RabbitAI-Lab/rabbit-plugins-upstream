## Description: <br>
辅助APQP项目管理全流程；支持项目阶段定义、文档生成（FMEA/PPAP/控制计划）、甘特图可视化、风险分析与知识库查询；适用于制造业产品质量规划全流程 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Manufacturing quality, project management, and APQP teams use this skill to plan APQP phases, generate FMEA, control-plan, PPAP, Gantt, and risk-analysis outputs, and consult APQP/IATF 16949 reference material. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated APQP, FMEA, PPAP, control-plan, or risk-analysis content can be incomplete or incorrect when project inputs are missing, stale, or too generic. <br>
Mitigation: Review outputs with qualified APQP, quality, engineering, and customer-facing team members before using them for decisions or submissions. <br>
Risk: The skill produces user-directed local files and may use project files as inputs for APQP outputs. <br>
Mitigation: Run it in a dedicated project folder, choose output paths deliberately, and provide only files intended for the APQP workflow. <br>
Risk: PPAP and quality-planning requirements vary by customer, product, and applicable standard. <br>
Mitigation: Validate generated checklists and documents against customer-specific requirements, current standards, and internal quality procedures. <br>


## Reference(s): <br>
- [APQP阶段详细指南](references/apqp_phases.md) <br>
- [APQP最佳实践](references/best_practices.md) <br>
- [IATF 16949 标准要点](references/iatf16949_knowledge.md) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-apqp-project-manager) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-apqp-project-manager) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell command examples; generated Markdown, JSON, and HTML project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated local files may include FMEA reports, control plans, PPAP checklists, Gantt charts, and risk-analysis reports.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
