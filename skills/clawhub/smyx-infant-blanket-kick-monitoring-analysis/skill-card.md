## Description:

Identifies babies kicking off blankets or exposing their bodies during sleep and alerts parents to cover them up to prevent catching a cold. | 婴儿蹬被监测技能，识别婴儿夜间睡觉踢开被子、身体裸露，及时提醒家长给宝宝盖被保暖，预防着凉感冒

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers use this skill to analyze infant sleep images or videos for blanket-kicking or body-exposure events and produce alerts, structured reports, and report links. It can also query cloud-stored historical monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant sleep videos or images may be uploaded to cloud services for analysis.

Mitigation: Install only after confirming the publisher and service endpoint are trusted, and review retention and deletion expectations before using real household media.

Risk: The skill may query cloud-stored analysis history and silently create or reuse an internal account identifier.

Mitigation: Confirm that cloud history access matches the intended user context and avoid sharing workspaces where cached identity state could expose another user's reports.

Risk: Authentication tokens may be cached in a local workspace database.

Mitigation: Restrict workspace access, inspect local credential storage before deployment, and remove cached tokens when the skill is no longer needed.

Risk: Monitoring results are advisory and may miss unsafe sleep conditions or produce incorrect alerts.

Mitigation: Use outputs only as supplemental reminders and maintain direct caregiver supervision and safe sleep practices.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and JSON analysis results, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local media files, public media URLs, or historical-report list requests; default detail output is json.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
