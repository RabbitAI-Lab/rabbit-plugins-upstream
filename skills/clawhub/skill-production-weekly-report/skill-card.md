## Description: <br>
Generates structured HTML weekly reports for production management from spoken input, Word documents, or Excel workbooks, with four-week history tracking and refusal when required data is missing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Production managers and operations teams use this skill to turn weekly production metrics, completed work, issues, next-week plans, and coordination needs into a standardized HTML weekly report. The skill can parse user-provided Word and Excel files, read recent local report history, and archive the generated report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads production files supplied by the user and stores generated report copies in local weekly report directories. <br>
Mitigation: Run it only in a controlled workspace, review input and output paths before executing helper scripts, and keep sensitive source files and generated reports under appropriate access controls. <br>
Risk: Incomplete or ambiguous production data can lead to misleading weekly reports. <br>
Mitigation: Use the documented minimum data checks and refuse report generation until core metrics, completed work, and next-week plans are provided. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-production-weekly-report) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>
- [Server-resolved GitHub repository](https://github.com/duding-engicool/skill-production-weekly-report) <br>
- [Production weekly report format](references/report_format.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, HTML files, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON parser output, and generated standalone HTML report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads user-provided production files and recent local report history, writes the weekly report to ./weekly_reports/, and archives a copy under ./weekly_reports/history/.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
