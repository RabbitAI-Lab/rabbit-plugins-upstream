## Description:

Analyzes thermal-imaging video of multi-person gatherings to compare each person's forehead or facial surface temperature against the group average and flag relative temperature anomalies for thermometer recheck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen thermal-camera video from family, meeting, classroom, or care-facility gatherings for relative surface-temperature anomalies. The output is an early screening aid and should not be used as a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Thermal videos may contain identifiable people, health information, children, employees, or guests and are uploaded for remote analysis.

Mitigation: Use the skill only with participant consent, trusted publisher and backend services, and verified configurable endpoints; avoid submitting unnecessary sensitive footage.

Risk: The skill may silently create or reuse a local user identity and store session tokens in the workspace data directory.

Mitigation: Run it in an isolated workspace, review local data storage before and after use, and remove account or token data when retention is not required.

Risk: Relative thermal screening can be affected by camera type, calibration, distance, occlusion, recent exercise, hot drinks, sunlight, air conditioning, or nearby heat sources.

Mitigation: Use only suitable thermal-imaging input under stable conditions and confirm any anomaly with a calibrated thermometer and appropriate professional review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-thermal-fever-screening-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Thermal fever screening API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Files]

**Output Format:** [Markdown text with embedded JSON analysis results, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a requested file; history queries return server-side report records.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
