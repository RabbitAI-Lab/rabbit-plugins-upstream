## Description:

Automatically identifies wet clothing and abnormal excretion from images or video and notifies caregivers with structured care alerts for incontinent elderly people, bedridden patients, and infants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, care organizations, and developers use this skill to analyze care images or videos for damp clothing, abnormal excretion, and related incontinence alerts. It can also retrieve cloud-stored historical care reports for authorized review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload intimate patient or infant media and query cloud-stored care history through remote services.

Mitigation: Install only for authorized care workflows with consent, access controls, and a trusted publisher and backend.

Risk: The skill automatically creates or reuses identity records and can persist account tokens in a local workspace database.

Mitigation: Run it in a controlled workspace, restrict local file access, and clear or rotate stored credentials when the deployment is no longer needed.

Risk: Care alerts and analysis results may be incomplete or incorrect and are not a substitute for professional medical or caregiver judgment.

Mitigation: Require a human caregiver or clinician to confirm alerts before making care decisions.

Risk: Configured service endpoints and cloud report storage create data-governance and retention obligations.

Mitigation: Review endpoint configuration, backend trust, retention practices, and applicable privacy requirements before deployment.

## Reference(s):

- [智能失禁状态提醒分析 API 文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown care reports, Markdown historical-report tables, or JSON analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a file; accepts local media paths or media URLs and supports basic, standard, and JSON detail levels.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
