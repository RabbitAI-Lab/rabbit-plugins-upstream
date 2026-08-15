## Description:

Analyzes fixed-camera home or kindergarten drop-off videos to detect crying expressions, clinging or resistance behaviors, and produce a mild/moderate/severe separation-anxiety assessment with supportive guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, teachers, and school operators can use this skill to review child drop-off footage for visual signs of crying, clinging, and resistance, then receive structured observations and calming recommendations. It is intended as an assistive observation tool, not as a psychological diagnosis or prescription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child and parent video may be processed by external cloud APIs and retained in report history.

Mitigation: Use only with appropriate guardian and school consent, upload only necessary footage, and avoid deployment where cloud processing or report-history retention is unacceptable.

Risk: The skill can create or reuse an internal user identity, store reusable tokens locally, and retrieve report history tied to that identity.

Mitigation: Install only in controlled workspaces, restrict filesystem access, remove or rotate local tokens when no longer needed, and review history lookup behavior before use.

Risk: Automated behavior analysis may produce incorrect assessments or be mistaken for clinical judgment.

Mitigation: Treat outputs as assistive observations, review results with caregivers or teachers, and seek qualified child mental-health support for persistent or severe concerns.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown report with structured JSON fields, behavior metrics, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a user-specified local file.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
