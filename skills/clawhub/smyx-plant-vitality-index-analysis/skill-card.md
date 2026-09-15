## Description:

Analyzes plant images or video with optional growth and environment data to return a 0-100 vitality score, grade, trend, sub-scores, alerts, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze plant media for smart planters, plant factories, home gardening, and plant-monitoring platforms. It can also retrieve cloud-hosted historical vitality reports for trend review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images or videos, report history, and a generated user identifier may be sent to the publisher's cloud service.

Mitigation: Review the publisher, data-sharing expectations, and consent requirements before installation or use.

Risk: The security evidence flags development/plain-HTTP service settings and recommends HTTPS production endpoints.

Mitigation: Correct defaults to approved HTTPS production hosts and restrict authenticated requests to those hosts before normal use.

Risk: The security evidence flags local token storage.

Mitigation: Avoid plaintext token storage and review local credential handling before deployment.

Risk: The security evidence flags a YAML dependency issue.

Mitigation: Fix the package dependency before normal users rely on the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Plant Vitality API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON analysis reports with command examples and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns vitality score, grade, trend, sub-scores, alert hints, and export/report URLs when available.]

## Skill Version(s):

1.0.11 (source: server release metadata; SKILL.md frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
