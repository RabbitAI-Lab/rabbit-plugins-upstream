## Description: <br>
量产阶段质量拦截与异常遏制升级助手；基于异常分级与升级阈值生成围堵/升级流程卡与跟踪看板，区别于 NPI 新品质量门与 Safe Launch 安全投产。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality managers, SQEs, production quality engineers, and line quality owners use this skill during mass-production exceptions to decide escalation level, define containment actions, and create a follow-up board for closure tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated escalation and containment recommendations may be incomplete if severity, batch scope, customer exposure, or loss data are missing. <br>
Mitigation: Confirm the critical missing fields before acting, and treat any pending rows in the board as unresolved until enterprise owners supply the data. <br>
Risk: The artifact describes a scripts/build_report.py renderer, but that script is not included in the inspected artifact. <br>
Mitigation: Use the skill for guidance unless the renderer is supplied elsewhere, and decide an explicit report output directory before generating local files. <br>
Risk: The skill produces recommendations and boards for quality escalation, not formal approval or root-cause closure. <br>
Mitigation: Keep final escalation approval, release decisions, signatures, and 8D/CAPA closure in the responsible enterprise process. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/duding-engicool/skill-mass-production-quality-gate) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-mass-production-quality-gate) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Files, Configuration] <br>
**Output Format:** [Markdown and plain text quality escalation cards, containment checklists, and tracking-board content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May mark missing operational inputs as pending confirmation; artifact evidence claims a local report renderer, but the inspected package does not include scripts/build_report.py.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
