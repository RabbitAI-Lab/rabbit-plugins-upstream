## Description:

Identifies sleep stages including falling asleep, light sleep, deep sleep, and REM; monitors body movement, nighttime awakenings, and sleep apnea, suitable for sleep monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to submit sleep-monitoring video files or URLs for cloud-backed sleep quality analysis, including sleep stages, body movement, nighttime awakenings, apnea indicators, structured report output, and history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload bedroom or sleep-monitoring media and report data to cloud services.

Mitigation: Use only non-sensitive test media unless the publisher documents the backend data flow and obtains explicit user approval for cloud submission.

Risk: The security evidence reports silent identity management and persistent reusable tokens in the workspace.

Mitigation: Review token storage and identity behavior before installation, and isolate or clear the workspace after testing.

Risk: The security evidence reports default insecure or private HTTP development endpoints.

Mitigation: Require HTTPS endpoints and destination allowlists before using the skill with personal or health-sensitive data.

Risk: Sleep quality and apnea indicators may be health-sensitive and are described as reference information rather than a medical diagnosis.

Mitigation: Present outputs as informational only and direct users to qualified medical professionals for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown text containing structured JSON report data and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save report output to a user-specified file; default detail level is json; supported video inputs are mp4, avi, and mov up to 10 MB.]

## Skill Version(s):

1.0.14 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
