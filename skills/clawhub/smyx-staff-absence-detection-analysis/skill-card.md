## Description:

Real-time monitoring of personnel on-duty status in specific areas based on computer vision and human pose estimation, automatically detects abnormal statuses such as leaving posts and absent from work, supports custom threshold settings, and triggers early warning immediately when abnormality is detected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, safety, and facility-management teams use this skill to analyze workplace video or images for staff presence, post status, abnormal absence duration, and related historical reports. It is intended for authorized personnel monitoring in settings such as factories, security rooms, and service windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive workplace images or videos and identity-linked report data to configured Life Emergence cloud services.

Mitigation: Use only where personnel monitoring is authorized, and confirm retention, deletion, endpoint allowlist, and data-handling terms with the publisher before deployment.

Risk: The skill can silently create or reuse a local identity and store authentication tokens in a workspace SQLite database.

Mitigation: Run it in a controlled workspace, restrict access to local data files, and review token storage, rotation, and cleanup procedures before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-staff-absence-detection-analysis)
- [Personnel Absence Monitoring API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports, JSON analysis results, and shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection status, absence counts and durations, confidence and absence thresholds, report links, and historical report tables.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
