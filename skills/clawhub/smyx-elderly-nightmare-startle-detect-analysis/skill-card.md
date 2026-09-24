## Description:

Using a fixed bedroom camera with infrared night vision and microphone audio, this skill analyzes elderly nighttime sleep video to detect sudden sitting-up, screams, arm-thrashing, and related abnormal sleep events, then records event timing, frequency, duration, and caregiver-facing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and developers use this skill to submit fixed-camera nighttime sleep video or a report-query request and receive structured sleep-event analysis, history lookup results, and non-diagnostic recommendations for follow-up with appropriate clinicians.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads highly sensitive bedroom video and audio to cloud APIs and generates sleep-health reports.

Mitigation: Use only with explicit consent from the monitored person, confirm the cloud provider, retention and deletion terms, and access controls before installation or use.

Risk: The skill silently creates or reuses local identity tokens for report association.

Mitigation: Use a dedicated workspace and review local token storage and access controls before handling real personal data.

Risk: Outputs can be mistaken for medical diagnosis or treatment guidance.

Mitigation: Treat results as behavioral observations only; do not use them for diagnosis, medication changes, or replacing clinician review.

## Reference(s):

- [Skill API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON sleep-event report with event counts, timelines, risk signal level, recommendations, and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the generated report to a user-specified output file.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
