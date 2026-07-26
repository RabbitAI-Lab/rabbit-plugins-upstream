## Description: <br>
Provides end-to-end support for Layered Process Audits, including LPA knowledge lookup, checklist generation, audit result analysis, and report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality engineers, production supervisors, and audit managers use this skill to prepare LPA checklists, analyze audit result JSON, identify issue patterns, and generate structured audit reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect file paths may cause scripts to read the wrong audit data or write reports to unintended locations. <br>
Mitigation: Review input and output paths before running the scripts. <br>
Risk: Untrusted or malformed audit JSON can lead to misleading analysis or report content. <br>
Mitigation: Use trusted JSON inputs and review generated reports before relying on them. <br>
Risk: Some advertised resources are empty in this version. <br>
Mitigation: Check the included reference and script files before depending on unavailable resources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-lpa-audit) <br>
- [Source repository](https://github.com/duding-engicool/skill-lpa-audit) <br>
- [Audit level standards](references/audit_levels.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples plus JSON analysis and HTML report file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts read checklist and audit-result JSON and write generated artifacts to user-selected output paths.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter declares 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
