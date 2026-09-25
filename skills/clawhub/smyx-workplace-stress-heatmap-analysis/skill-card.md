## Description:

Analyzes fixed-camera workplace video or images to produce anonymous, zone-level group stress indices, heatmap colors, trend signals, manager suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, HR, workplace health, and facilities teams use this skill to review anonymous, area-level stress heatmaps from office-camera footage and identify zones that may need workload, environment, or wellbeing follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes workplace video and sends analysis requests to cloud services, which can involve sensitive employee data even when outputs are intended to be anonymous and aggregate.

Mitigation: Deploy only with explicit employee notice and consent, documented data-processing terms, and clear retention and deletion policies for uploaded video, reports, and report links.

Risk: The security evidence flags user identity, credentials, cloud traffic, and local token/profile persistence as areas requiring review.

Mitigation: Confirm the vendor and configured endpoints before installation, require HTTPS production endpoints, and remove or protect any local token or profile persistence before using real workplace video.

Risk: Small groups or poorly scoped workstation zones could make aggregate stress outputs functionally identifiable.

Mitigation: Enforce the documented minimum-sample behavior so zones with fewer than three observable people return only insufficient-sample status and no stress index.

Risk: Visual stress cues such as frowning or posture can be ambiguous and should not be treated as individual diagnosis or performance evidence.

Mitigation: Use outputs only as area-level operational signals, combine them with voluntary employee feedback where appropriate, and prohibit individual profiling, diagnosis, or performance evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Workplace stress heatmap API documentation](artifact/references/api_doc.md)
- [Common analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files]

**Output Format:** [Markdown or JSON text, with optional saved output files and report export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs zone-level aggregate stress metrics, heatmap colors, trend summaries, manager suggestions, and historical report records.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
