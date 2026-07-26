## Description: <br>
Helps independent teachers turn schedules, student records, homework, parent communication, and lesson-package status into a seven-section daily dashboard with risk flags and top priorities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Independent teachers use this skill to review daily classes, preparation tasks, homework follow-up, parent communication, lesson-package renewal points, and the three most important actions for the day. It is intended as a planning and triage dashboard, not as an automatic messaging or record-writing system. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation phrases may route generic planning requests into a dashboard that reads student workspace data. <br>
Mitigation: Narrow activation to explicit independent-teacher workspace requests or ask a clarification question before reading student, parent, course-package, or schedule data. <br>
Risk: The dashboard may expose sensitive student or family information if raw workspace fields are copied directly. <br>
Mitigation: Use aliases, summarize parent and lesson notes within the stated 500-character limits, and omit real names, contact details, family conflict, medical details, and payment information. <br>
Risk: Suggested follow-up could be mistaken for an authorized external action or record update. <br>
Mitigation: Keep messages, lesson-unit consumption, parent communication, renewal suggestions, and cross-skill sharing as teacher-confirmed actions only. <br>


## Reference(s): <br>
- [Dashboard template](references/dashboard-template.md) <br>
- [Daily dashboard block templates](references/daily-dashboard-block-templates.md) <br>
- [Daily dashboard full sample](references/daily-dashboard-full-sample.md) <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style daily dashboard with structured text sections and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses student aliases, concise summaries, risk labels with field-based rationale, and teacher-confirmed follow-up actions.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
