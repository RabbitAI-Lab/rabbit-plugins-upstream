## Description:

Analyzes office workstation video to identify prolonged sitting and posture-warning signals such as forward head angle, back curvature, shoulder asymmetry, and close screen distance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, workplace health teams, and developers use this skill to analyze office workstation video or report history for prolonged sitting and posture warning signals. It is intended for behavior guidance and workplace-health reminders, not diagnosis or rehabilitation planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace video, report metadata, generated user IDs, and tokens may be sent to configured LifeEmergence cloud services.

Mitigation: Use only with clear notice and consent from recorded employees or subjects, approved video sources, and an accepted cloud data-sharing path.

Risk: The skill may silently create or reuse local identities and store token-related state locally.

Mitigation: Prefer explicit authenticated identity handling and document how operators can inspect or delete data/smyx-common-claw.db and data/smyx-api-key.txt.

Risk: Posture and prolonged-sitting results could be mistaken for medical diagnosis or rehabilitation advice.

Mitigation: Present outputs as visual workplace-health reminders only, and direct users with existing neck or back discomfort to qualified professionals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-office-worker-posture-warning-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown report text with JSON-structured analysis content and report links; optional file output when --output is supplied.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts mp4, avi, and mov local video files up to 10 MB or video URLs; can query historical reports from the configured cloud API.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
