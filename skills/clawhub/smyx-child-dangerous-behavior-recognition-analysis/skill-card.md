## Description:

Detects climbing, playing with fire, touching power sources, and dangerous actions near windows, providing real-time alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and safety supervisors use this skill to analyze child monitoring videos or video URLs for hazardous behaviors and produce structured safety reports, alerts, recommendations, and report links. It is intended as an aid for homes, kindergartens, and nurseries, not as a replacement for human supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child video files or video URLs are sent to the configured cloud service.

Mitigation: Use only with appropriate consent, retention rules, access controls, and legal authority; prefer explicit confirmation before uploads.

Risk: Report history is fetched from the cloud and local identity or token state may be created or reused in the workspace.

Mitigation: Review workspace identity state and confirm authorization before history lookups, especially in homes, schools, kindergartens, or nurseries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown or JSON structured analysis reports with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can output basic, standard, or JSON detail levels and can save results to a local output file.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
