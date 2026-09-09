## Description:

Analyzes child study-area posture video to estimate spinal curvature and head tilt, generate structured posture findings, and produce voice-reminder text when poor posture persists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze child posture videos from study desks, smart lamps, or classrooms, return visual posture estimates and reminder text, and retrieve historical posture reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child posture videos and report metadata are sent to the publisher's backend.

Mitigation: Use only with explicit guardian consent, clear retention/deletion terms, and HTTPS-only endpoints.

Risk: The security review flags unsafe token transport and storage choices.

Mitigation: Review credential handling before installation and avoid shared machines unless local token storage is protected or disabled.

Risk: Posture angles are visual estimates and are not medical assessments.

Mitigation: Present results as habit-correction reminders and route medical concerns to qualified clinicians.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON-formatted posture analysis report with report links and voice-reminder text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs; documented input limit is 10 MB and historical report queries return structured records.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
