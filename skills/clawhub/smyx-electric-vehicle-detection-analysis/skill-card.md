## Description:

Automatically detects electric motorcycles and e-bikes in restricted areas based on computer vision, supports real-time detection for video streams and images, counts illegal parking or driving instances, and triggers violation alerts for parks, communities, and organizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security, facilities, and operations teams use this skill to analyze camera footage or images for electric motorcycles and e-bikes in restricted areas. It returns violation counts, warning levels, management suggestions, and report links that support safety management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload videos, images, or URLs to an external cloud service for analysis.

Mitigation: Install and run it only where the media handling model is approved for the footage, location, and privacy requirements.

Risk: The skill silently creates or reuses an internal identity, queries cloud-stored report history, and may store service tokens in the local workspace.

Mitigation: Confirm that automatic identity association and local token storage are acceptable, and clear or rotate local credentials according to organizational policy.

Risk: Computer vision results can miscount vehicles or misclassify violations.

Mitigation: Use the output as a management aid and require human review before enforcement, safety, or disciplinary action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)
- [电动车智能检测分析 API 文档](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown reports and JSON results with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection counts, violation level, risk score, management warnings, management suggestions, and links to cloud-hosted reports.]

## Skill Version(s):

9.9.13 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
