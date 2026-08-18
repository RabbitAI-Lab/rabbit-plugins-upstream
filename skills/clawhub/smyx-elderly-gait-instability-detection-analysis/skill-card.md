## Description:

Using fixed-camera video of an elderly person walking in a straight line, this skill estimates gait metrics such as step length, gait speed, trunk sway, and cadence to report gait stability and fall-risk level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and health-management developers use this skill to analyze walking videos for objective gait indicators, fall-risk screening, historical report lookup, and follow-up guidance. The output is an auxiliary screening report and is not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends gait videos and report queries to the publisher's cloud service and works with sensitive health-related content.

Mitigation: Use it only with informed consent from the recorded person or guardian, avoid treating outputs as diagnosis, and follow appropriate privacy handling for videos and reports.

Risk: The server security review says the skill silently creates or reuses a local identity and stores authentication data for health-related reports.

Mitigation: Review or clear the workspace data directory on shared machines and install only when this identity and token behavior is acceptable.

## Reference(s):

- [Elderly gait instability API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-gait-instability-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include gait metrics, fall-risk level, risk factors, alert text, history tables, and cloud report URLs.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
