## Description:

Analyzes in-cabin driver face video or images for visible facial flushing and abnormal sweating signals, then returns structured visual health-risk reminders without making a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and vehicle-safety teams use this skill to analyze driver DMS camera media for visible facial flushing, sweat-glare area, and related warning indicators. It supports driver-facing alerts, fleet event records, and historical report review while remaining an auxiliary visual reminder rather than a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive driver face media and health-related visual indicators through remote services.

Mitigation: Use only with explicit driver or employee consent, confirm the backend environment before sending media, and follow applicable privacy and retention requirements.

Risk: The skill can automatically create or reuse identity records and store local tokens.

Mitigation: Review local identity and token storage before deployment and require an operational process to disable, rotate, or delete stored credentials and records.

Risk: Remote URL inputs may cause backend services to fetch arbitrary media locations.

Mitigation: Restrict inputs to trusted media sources and avoid arbitrary remote URLs.

Risk: Visual flushing and sweating signals can be affected by lighting, tinted glass, masks, camera quality, and individual skin differences.

Mitigation: Treat outputs as auxiliary visual alerts only and require professional medical evaluation for health decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-flushing-sweat-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Driver flushing and sweat API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown status text with structured JSON analysis fields and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a user-specified file and may query cloud report history.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
