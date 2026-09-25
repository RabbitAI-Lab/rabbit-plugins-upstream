## Description:

Early monitoring of plant wilting based on hyperspectral imaging and computer vision, captures early wilting signs before visible symptoms, provides early warning for precision irrigation and disease control. | 植物枯萎监测技能，基于高光谱成像与计算机视觉，在肉眼可见症状前捕捉早期枯萎迹象，为精准灌溉和病害防控提供早期预警

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze plant images or videos for early wilting signs, distinguish environmental water stress from pathological wilt, estimate wilting severity, and retrieve prior cloud analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends plant media and linked identity data to Life Emergence cloud services.

Mitigation: Install and use it only when those cloud data flows are acceptable for the media and users involved.

Risk: The skill may silently reuse a workspace file named smyx-api-key.txt as identity.

Mitigation: Control access to the workspace data directory and review identity files before running analysis or history queries.

Risk: Cloud tokens may be stored locally in plaintext SQLite.

Mitigation: Restrict local filesystem access, avoid shared workspaces for sensitive usage, and clear local data when no longer needed.

Risk: Billing errors may prompt installation of a separate payment skill.

Mitigation: Review any payment-skill installation request before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report, Markdown history table, or JSON output with report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include plant wilting findings, severity assessment, recommendations, cloud report links, and historical report entries.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
