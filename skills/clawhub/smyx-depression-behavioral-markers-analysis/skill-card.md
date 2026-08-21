## Description:

Analyzes fixed home-camera video for long immobility and appetite-change behavior markers, then produces a structured behavioral-change report for caregiver or community-care review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and community care staff use this skill to review multi-day home video for extended lying-in-bed duration, reduced eating activity, and related behavioral-change alerts. The skill is framed as a behavioral-observation aid and not as a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home-camera video and mental-health context may be sent to remote services.

Mitigation: Use only with informed consent from the recorded person, confirm where the remote API sends data, and avoid private or signed video URLs unless sharing them is intended.

Risk: Persistent identity records and server-side reports may retain sensitive household or health information.

Mitigation: Review account linkage, retention, deletion, and report-access controls before deployment.

Risk: Behavioral-change outputs may be mistaken for depression diagnosis or treatment advice.

Mitigation: Present results only as behavioral observations, avoid diagnostic labels or medication advice, and route concerning results to family, community doctors, or qualified clinicians.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python CLI commands and JSON-style structured report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include behavior metrics, alert labels, recommendations, and report export links returned by the remote analysis service.]

## Skill Version(s):

1.0.11 (source: server release metadata; SKILL.md frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
