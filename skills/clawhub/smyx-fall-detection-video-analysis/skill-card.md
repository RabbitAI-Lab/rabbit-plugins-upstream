## Description:

Detects possible falls in video footage of a target area and returns an analysis report for safety monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and home-safety operators can use the skill to review video footage for possible falls and receive structured findings and safety guidance. Detection results are intended as alerts for human follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private video may be uploaded even when export-only behavior is requested.

Mitigation: Avoid private footage until export behavior is corrected, and confirm who can access uploaded videos and how they can be deleted.

Risk: The skill may create accounts automatically and retain login credentials, while account separation is unclear.

Mitigation: Confirm credential handling and account isolation before use.

Risk: Alarm delivery may not be reliable enough to support urgent monitoring on its own.

Mitigation: Verify alert delivery end to end and require human confirmation of reported falls.

## Reference(s):

- [Fall detection API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report with fall findings, safety guidance, and report links when available; historical reports can be listed in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are safety alerts for human follow-up and do not replace on-site confirmation.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
