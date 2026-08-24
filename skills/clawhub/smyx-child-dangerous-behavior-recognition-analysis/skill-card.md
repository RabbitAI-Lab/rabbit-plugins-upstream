## Description:

Detects climbing, playing with fire, touching power sources, and dangerous actions near windows, providing real-time alerts for child safety supervision in homes, kindergartens, and nurseries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to analyze child-monitoring videos or URLs for hazardous behavior, generate structured risk reports, and query cloud-stored historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child-safety videos or URLs may be processed through the provider's cloud services.

Mitigation: Use the skill only when the operator accepts the provider's media processing, retention, and deletion practices for sensitive child-safety footage.

Risk: The skill can create or reuse a local identity tied to cloud-stored reports.

Mitigation: Review identity handling and cloud report association before deployment, and avoid exposing internal identity values in user-facing outputs.

Risk: Bundled common configuration may select development or private-network endpoints.

Mitigation: Review and update configuration endpoints before use in production or customer-facing environments.

Risk: Account tokens may be persisted with incomplete disclosure.

Mitigation: Confirm token storage, rotation, and deletion practices before installing or running the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown summaries, JSON analysis results, report links, and optional output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs, configurable alert threshold, basic/standard/json detail levels, and historical report listing.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
