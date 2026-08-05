## Description: <br>
Routes work-report requests by identifying the report type, audience, purpose, and time range, then asks for missing facts instead of producing unsupported conclusions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and managers use this skill to classify ambiguous work-report requests and route daily, weekly, monthly, midyear, annual, project, escalation, decision, meeting-summary, and multi-skill requests to the appropriate specialized skill. When facts are insufficient, it asks follow-up questions and avoids generating a complete report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Work-report inputs can include sensitive company, customer, schedule, risk, owner, or deadline details. <br>
Mitigation: Provide only information appropriate for the report audience and redact sensitive details that are not needed for routing or report clarification. <br>
Risk: Incomplete facts can lead to misleading report conclusions if a downstream user treats routing guidance as a complete report. <br>
Mitigation: Use the skill's parameter checks and follow-up questions before asking any specialized report skill to produce final text. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with routing decisions, parameter status tables, follow-up questions, or limited project-report structure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes to related zayn report skills when appropriate and stops after routing so only one skill produces final text.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
