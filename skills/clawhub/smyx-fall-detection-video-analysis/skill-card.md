## Description:

Detects whether anyone has fallen within a target area using video stream analysis, intended for safety monitoring of older adults living alone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users can provide a local video or video URL to request fall detection and review a structured result. Developers can use the report listing workflow to retrieve prior analysis reports; results are intended as safety alerts and require human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private reports may be mixed across users, and video may be uploaded even when export-only behavior is requested.

Mitigation: Use a separate workspace and account for each user, and have the publisher address sender isolation and export-only behavior before using private footage.

Risk: Login credentials may be retained or sent to an unintended destination.

Mitigation: Have the publisher address token storage and restrict credential destinations before supplying credentials.

Risk: Cloud report retention and access are unclear, and this bundle is not suitable as the sole source of continuous emergency alarms.

Mitigation: Clarify cloud retention and report access, and pair alerts with independent human or emergency monitoring.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Files]

**Output Format:** [Structured analysis report with results, risk guidance, and report links; Markdown table for report listings; optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report detail can be basic, standard, or JSON. Detection results are advisory and need human confirmation.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
