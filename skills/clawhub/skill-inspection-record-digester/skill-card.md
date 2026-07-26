## Description: <br>
Inspection Record Digester turns user-provided inspection table images for quality checks, equipment checks, or audits into reviewed structured records, a Markdown analysis report, and CSV data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, quality teams, equipment teams, and audit reviewers use this skill to convert photos, scans, screenshots, or PDF page images of inspection records into cleaned records and summary analysis. It is intended for batches of inspection, equipment check, and audit tables where ambiguous fields must be reviewed by the user before analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Inspection records may contain sensitive operational or audit information. <br>
Mitigation: Provide only files the agent is allowed to read, and review outputs before sharing or storing them. <br>
Risk: Low-confidence visual recognition can produce incorrect records if ambiguous fields are accepted without review. <br>
Mitigation: Require user confirmation or correction for low-confidence or missing fields before cleaning, analysis, or report generation. <br>
Risk: The package references helper files or scripts that may be missing from the release artifact. <br>
Mitigation: Confirm the referenced schemas, review guidance, and digest script are present or implemented before relying on end-to-end execution. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/duding-engicool/skill-inspection-record-digester) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-inspection-record-digester) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, csv, shell commands, guidance] <br>
**Output Format:** [Markdown report, CSV records, structured intermediate data, and a concise conversational summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation for low-confidence or missing fields before analysis; CSV output is intended to use UTF-8 with BOM for Chinese Excel compatibility.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
