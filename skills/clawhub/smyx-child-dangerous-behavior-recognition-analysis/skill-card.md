## Description:

Analyzes child-monitoring videos for hazardous behaviors and provides risk alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and childcare staff can analyze video files or URLs for hazardous child behaviors, review risk reports, and request historical reports. Confirm consent and cloud-processing arrangements before using it with children’s footage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child-monitoring videos or URLs are sent to lifeemergence.com cloud services; consent, retention, and report access controls are unclear.

Mitigation: Review cloud-processing terms and independently establish consent, retention, and report-access controls before using real footage.

Risk: The skill silently creates or reuses local identity records and stored tokens.

Mitigation: Inspect local credential handling and define token access and cleanup procedures before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured report or Markdown table for historical reports; optional JSON output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk findings, recommendations, and report links when available]

## Skill Version(s):

1.0.15 (source: server-resolved release; bundled frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
