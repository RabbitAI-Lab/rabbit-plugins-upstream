## Description: <br>
Helps metrology administrators and laboratory leads maintain measuring-instrument ledgers, calculate next calibration dates, flag overdue items, and produce management reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Metrology administrators, laboratory supervisors, and quality teams use this skill to add, update, query, and review measuring-instrument records, calculate calibration due dates, identify overdue instruments, and prepare inspection or send-out calibration plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated metrology_report files may overwrite existing reports if the destination is not checked first. <br>
Mitigation: Confirm the output location and whether an existing metrology_report file should be replaced before generating reports. <br>
Risk: Users may over-rely on calculated due dates or default cycles as a substitute for certificates or enterprise metrology rules. <br>
Mitigation: Treat calculated dates and default cycles as planning aids, and verify final calibration status against actual certificates and company procedures. <br>
Risk: Optional Word or Excel exports can create additional files beyond the default Markdown report. <br>
Mitigation: Generate Word or Excel files only after the user explicitly requests those formats. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/duding-engicool/skills/skill-metrology-management) <br>
- [Server-Resolved Source Repository](https://github.com/duding-engicool/skill-metrology-management) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown management ledger by default, with optional Word or Excel files after user confirmation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output is metrology_report.md; optional exports are metrology_report.docx and metrology_report.xlsx.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
