## Description:

Study Abroad Assistant - 留学助理 helps agents support U.S. graduate school applicants in CS, EE, data, and related fields with competitiveness assessment, planning, school tiering, professor shortlists, essay feedback, outreach drafts, and progress reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External applicants and advising agents use this skill to structure U.S. graduate admissions work: profile assessment, application timelines, school selection, professor outreach preparation, essay feedback, and decision reporting. It is intended as guidance and workflow support, not a guarantee of admission or a substitute for official university, legal, visa, or immigration advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applicant profile, school-selection, essay/outreach, report, and application-tracking data may be sent to the disclosed cloud engine.

Mitigation: Use the skill only when this data flow is acceptable, avoid unnecessary sensitive details, and remind users that cloud processing is part of the main workflow.

Risk: The local ~/.study-abroad directory can contain an anonymous identifier and registered API key.

Mitigation: Protect the directory on shared machines, remove it when no longer needed, and rely on the existing 0600 permission behavior for saved API keys.

Risk: Local collection workflows can retain emails, real names, or confidential admissions records.

Mitigation: Do not enter personal or confidential admissions records into local collection files unless retention is intended; clean or redact retained records as needed.

Risk: Admissions recommendations, professor shortlists, deadlines, and generated drafts can be incomplete or outdated.

Mitigation: Verify program facts, faculty status, deadlines, and final application materials against official university sources before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/study-abroad-assistant)
- [ComplianceHub study engine](https://compliancehub.cn/api/study)
- [ComplianceHub account page](https://compliancehub.cn/account.html?skill=study-abroad-assistant)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and structured text sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-drafted essay feedback or outreach text that should be reviewed and finalized by the user.]

## Skill Version(s):

1.1.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
