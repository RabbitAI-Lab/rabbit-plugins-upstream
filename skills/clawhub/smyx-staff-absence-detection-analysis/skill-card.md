## Description:

Real-time monitoring of personnel on-duty status in specific areas based on computer vision and human pose estimation, automatically detects abnormal statuses such as leaving posts and absent from work, supports custom threshold settings, and triggers early warning immediately when abnormality is detected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and site operations managers use this skill to analyze workplace images or videos for on-duty status, leave-post events, absence duration, and historical monitoring reports. It is intended for authorized post supervision workflows in factories, security rooms, service windows, and similar staffed areas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace monitoring images, videos, and report metadata may be sent to configured cloud services.

Mitigation: Use the skill only for authorized workplace surveillance workflows, verify the configured service endpoints, and review retention and deletion practices before production use.

Risk: Account identity or session state may be created or reused silently.

Mitigation: Review identity handling, local token or database storage, and report-history access controls before deployment, especially on shared systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-staff-absence-detection-analysis)
- [Staff absence monitoring API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON analysis report with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include structured monitoring results, absence statistics, historical report listings, and report links returned by the configured cloud service.]

## Skill Version(s):

1.0.13 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
