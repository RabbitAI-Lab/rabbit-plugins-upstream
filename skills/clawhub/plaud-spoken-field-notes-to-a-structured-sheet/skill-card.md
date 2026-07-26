## Description: <br>
Turns spoken Plaud site-visit recordings into structured Google Sheets rows, extracting only stated values and flagging blanks or skipped recordings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Field staff, contractors, inspectors, and service teams use this skill to convert Plaud dictation from site visits into spreadsheet rows for measurements, specs, punch lists, service notes, or quote preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spoken notes and transcripts may contain sensitive information that is processed through Plaud and stored in Google Sheets. <br>
Mitigation: Use only with appropriate consent, Plaud and Google Sheets access controls, and retention settings; avoid highly sensitive, regulated, or confidential recordings unless those controls are suitable. <br>
Risk: Extracted spreadsheet rows can be incomplete or need review before they are used for quotes, inspections, or service records. <br>
Mitigation: Review the run summary and any flagged blank cells before acting on the row; the workflow leaves missing values empty rather than guessing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/plaud-spoken-field-notes-to-a-structured-sheet) <br>
- [AgentPMT workflow page](https://www.agentpmt.com/agent-workflow-skills/plaud-spoken-field-notes-to-a-structured-sheet) <br>
- [Get Users Current Time / Date skill](https://clawhub.ai/agentpmt/get-users-current-time-date) <br>
- [Plaud skill](https://clawhub.ai/agentpmt/plaud) <br>
- [Google Sheets skill](https://clawhub.ai/agentpmt/google-sheets) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, API Calls, Configuration] <br>
**Output Format:** [Markdown instructions with JSON tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Appends extracted rows to Google Sheets and summarizes captured, skipped, or incomplete recordings.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
