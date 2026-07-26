## Description: <br>
辅助FMEA 2019版分析；帮助用户完成失效模式识别、RPN计算、风险等级评估与预防措施跟踪；支持DFMEA、PFMEA、SFMEA全场景 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality, reliability, and engineering teams use this skill to structure FMEA analysis, identify failure modes, calculate RPN scores, assess risk levels, and track preventive or corrective actions across DFMEA, PFMEA, and SFMEA workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: FMEA project details may be saved in a local fmea_output/ folder when the tracker script is used. <br>
Mitigation: Use a private workspace for confidential engineering or product-risk data and review generated files before sharing. <br>
Risk: Risk rankings and recommendations depend on the supplied severity, occurrence, and detection scores. <br>
Mitigation: Have qualified reviewers confirm inputs, assumptions, and resulting actions before using them for quality or safety decisions. <br>


## Reference(s): <br>
- [FMEA 2019 format guide](references/fmea_format.md) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-fmea-assistant) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-fmea-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown, shell commands, code, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; helper scripts return JSON and can export CSV or JSON project files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The tracker script creates local project records and exports under fmea_output/ in the current working directory.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
