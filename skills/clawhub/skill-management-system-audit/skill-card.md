## Description: <br>
分析管理体系文件的逻辑完整性与合规性，识别差异点和风险，提供结构化改进建议；适用于内审、供应商评估、认证准备及流程改善场景 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality, compliance, and operations teams use this skill to review management-system documents for structure, responsibilities, process logic, standards alignment, gaps, risks, and improvement actions. It supports internal audits, supplier assessments, certification preparation, and process improvement work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-provided audit documents and generated reports may contain confidential process, compliance, or risk details. <br>
Mitigation: Provide only the intended document set, run it in an appropriate workspace, and store generated Markdown reports according to the organization's confidentiality requirements. <br>
Risk: Audit findings and standards comparisons may be incomplete or incorrect if inputs are missing, outdated, or interpreted without qualified review. <br>
Mitigation: Have qualified quality or compliance personnel review findings before using them for certification, supplier decisions, or formal corrective actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-management-system-audit) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>
- [Source repository](https://github.com/duding-engicool/skill-management-system-audit) <br>
- [Source commit 12e3cfb](https://github.com/duding-engicool/skill-management-system-audit/tree/12e3cfbc16feae6eb1972d4aeeef8b3535ff7244) <br>
- [ISO 9001:2015 reference](references/iso-9001-2015.md) <br>
- [ISO 14001:2015 reference](references/iso-14001-2015.md) <br>
- [ISO 45001:2018 reference](references/iso-45001-2018.md) <br>
- [IATF 16949:2016 reference](references/iatf-16949-2016.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown audit reports, structured guidance, and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled report script writes timestamped local Markdown files named audit_report_YYYYMMDD_HHMMSS.md.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
